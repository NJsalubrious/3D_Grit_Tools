/**
 * 3D GRIT — edge worker (analytics + form intents)
 *
 * Routes (same-origin, mounted at /api/* on the Cloudflare Pages domain):
 *   POST /api/track   — every event from assets/js/track.js (consistent schema)
 *
 * Persistence is optional and progressive:
 *   - If a KV namespace is bound as GRIT_EVENTS, events are stored there.
 *   - Otherwise the event is logged (visible in `wrangler tail`).
 *
 * Bindings (wrangler.toml):
 *   [[kv_namespaces]] binding = "GRIT_EVENTS"  id = "..."
 *   [vars] ALLOWED_ORIGIN = "https://3dgrit.com"   # optional; defaults to "*"
 */

const MAX_BODY_BYTES = 8 * 1024;

function corsHeaders(env) {
  return {
    "Access-Control-Allow-Origin": (env && env.ALLOWED_ORIGIN) || "*",
    "Access-Control-Allow-Methods": "POST, OPTIONS",
    "Access-Control-Allow-Headers": "Content-Type",
  };
}

function json(body, status, env) {
  return new Response(JSON.stringify(body), {
    status,
    headers: { "Content-Type": "application/json", ...corsHeaders(env) },
  });
}

export default {
  async fetch(request, env, ctx) {
    if (request.method === "OPTIONS") {
      return new Response(null, { headers: corsHeaders(env) });
    }
    if (request.method !== "POST") {
      return new Response("Method Not Allowed", { status: 405, headers: corsHeaders(env) });
    }

    const url = new URL(request.url);
    if (!url.pathname.startsWith("/api/")) {
      return new Response("Not Found", { status: 404, headers: corsHeaders(env) });
    }

    let data;
    try {
      const raw = await request.text();
      if (raw.length > MAX_BODY_BYTES) return json({ error: "payload too large" }, 413, env);
      data = JSON.parse(raw);
    } catch (e) {
      return json({ error: "bad request" }, 400, env);
    }

    if (!data || typeof data.event !== "string" || !data.event) {
      return json({ error: "missing event" }, 422, env);
    }

    // Server-stamped fields (don't trust the client for these)
    const record = {
      event: data.event.slice(0, 64),
      tool: data.tool ? String(data.tool).slice(0, 64) : null,
      itemId: data.itemId ? String(data.itemId).slice(0, 96) : null,
      label: data.label ? String(data.label).slice(0, 120) : null,
      path: data.path ? String(data.path).slice(0, 256) : null,
      ref: data.ref ? String(data.ref).slice(0, 256) : null,
      email: data.email ? String(data.email).slice(0, 256) : null,
      name: data.name ? String(data.name).slice(0, 120) : null,
      subject: data.subject ? String(data.subject).slice(0, 160) : null,
      message: data.message ? String(data.message).slice(0, 4000) : null,
      ts: new Date().toISOString(),
      ip: request.headers.get("CF-Connecting-IP") || null,
      country: (request.cf && request.cf.country) || null,
    };

    try {
      if (env && env.GRIT_EVENTS) {
        const key = `evt:${record.ts}:${crypto.randomUUID()}`;
        // store the write so it survives the early response
        ctx.waitUntil(env.GRIT_EVENTS.put(key, JSON.stringify(record)));
      } else {
        console.log("[GRIT] event", record.event, record.itemId || record.tool || "", record.path || "");
      }
    } catch (e) {
      console.error("[GRIT] persist failed", e);
    }

    return json({ status: "ok" }, 200, env);
  },
};
