/* ============================================================
   3D GRIT — trackable layer
   One consistent event schema for every page and CTA.
   Endpoint: <meta name="grit:endpoint"> if present, else /api/track
   (same-origin via the Cloudflare worker route — no CORS).
   Every event carries the registry item id (data-item) so each
   piece of content is individually measurable.
   ============================================================ */
(function () {
  "use strict";

  var meta = document.querySelector('meta[name="grit:endpoint"]');
  var ENDPOINT = (meta && meta.content) || "/api/track";

  function send(payload) {
    payload.path = location.pathname;
    payload.ref = document.referrer || null;
    payload.ts = new Date().toISOString();
    var body = JSON.stringify(payload);
    try {
      if (navigator.sendBeacon) {
        navigator.sendBeacon(ENDPOINT, new Blob([body], { type: "application/json" }));
        return;
      }
      fetch(ENDPOINT, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: body,
        keepalive: true
      });
    } catch (e) {
      /* analytics must never break the page */
    }
  }

  // Public API — programmatic events (e.g. form submits, hub interactions)
  window.GRIT = window.GRIT || {};
  window.GRIT.track = function (event, extra) {
    var p = { event: event };
    if (extra) for (var k in extra) if (extra.hasOwnProperty(k)) p[k] = extra[k];
    send(p);
  };

  function wire() {
    // Declarative tracking on any [data-track] element
    document.querySelectorAll("[data-track]").forEach(function (el) {
      el.addEventListener("click", function () {
        send({
          event: el.getAttribute("data-track"),
          tool: el.getAttribute("data-tool") || null,
          itemId: el.getAttribute("data-item") || null,
          label: el.getAttribute("data-label") || (el.textContent || "").trim().slice(0, 80) || null
        });
      });
    });

    // Baseline page view
    send({ event: "page_view", itemId: (document.body && document.body.getAttribute("data-page-id")) || null });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", wire);
  } else {
    wire();
  }
})();
