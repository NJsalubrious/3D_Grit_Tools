
1. You are only working in 3DGRIT_NEW (which is the root)
2. 3DGRIT_NEW needs to be a a self enclosed sandbox
3. 3DGRIT is reference and will not be touched. it will remain the source of truth for all information.

we are going to remake 3DGRIT with all the information it contains but with the information contained in this folder:   

DIR:  PixelStortionGit\3DGRIT_NEW\RND


Read very very thoroughly: 

1. 3D GRIT KEYWORDS
2. Strategic Blueprint for 3DGRIT
3. Strategic Intelligence Report - Architecting a Content Ingestion Pipeline
4. Strategic Keyword Opportunities in the Blender Add-on Ecosystem
5. Strategic Keyword Opportunities in the Blender Add-on Ecosystem Rigging

This one is just an idea and if it isn't a good fit we won't do it but the reason for considering it is that the content I will be making to show of the tools is non - negotiable and fits the psychologically realistic, crime fiction genre and so making the website to ''happy'' will no doubt not fit the content i will eventually have on the site. the balance needs to be struck because we don't wan it to be too dark but we need too feel real - like a special effects company site mite feel if they mostly produce effects for gritty thrillers.

5. The Strategic Application of Dark Narrative Branding in Digital Product Marketing




Notes
The groundwork: a registry-driven, indexable, trackable foundation
Everything past and future becomes a registered content item. One source of truth, and from it flow nav, listings, sitemap, structured data, and tracking. Adding anything later (a tool, an SEO article, a showreel, an engine-found AI film) is "register it once, it appears everywhere."

1. Content registry (the spine)
A content/ folder of JSON manifests, generalizing the reference's posts.json into a site-wide index. Every item, hand-authored or engine-fed, carries the same core fields:

id, slug, type (tool / article / showreel / blog / hub-item / asset), title, description
canonicalPath (extensionless, per your Cloudflare setup), date, tags, keywordTarget
status (candidate / approved / published)
hub-items add: source, creatorCredit, toolsUsed, whyInteresting, curationScore (the "more positive recommendations, more credence" weighting from the pipeline doc)
sitt-geo-engine stays unwired for now, but the hub schema is shaped to receive its Gemini Flash output later. Engine writes candidates, you approve, approved items publish.

2. Indexable layer
Every content item is its own static, crawlable HTML page (the indexable unit), listed in sitemap.xml.
robots.txt pointing to the sitemap.
Per-page meta: title, description, extensionless canonical and og:url (honoring your known Cloudflare 308 behavior), Open Graph, Twitter card.
JSON-LD per type: Organization, Product (tools), Article (SEO posts), VideoObject / CreativeWork (showreels, hub films), BreadcrumbList.
A tiny on-demand generator script (run manually, keeps the served site buildless) reads the registry and emits sitemap.xml, so the registry and sitemap never drift.
3. Trackable layer
Stable id/slug per item so each is individually measurable.
Extend the existing data-track + worker.js pattern: page views plus key interactions, one consistent event schema, every page and CTA wired in. Worker upgraded to persist (Cloudflare D1/KV) rather than only logging.
4. What Phase 1 (Home) delivers on top of this
The grounded-grit Home page, built as the first consumer of the registry: hero, ecosystem overview, showcase, social proof, CTA. It proves the foundation (meta, JSON-LD, canonical, tracking, sitemap entry) end to end on one real page before we expand to tool pages, pricing, the SEO article layer, and the 3D-meets-AI hub.

That is the foundation I would scaffold inside 3DGRIT_NEW: content/ registry, index.html (Home), robots.txt, sitemap.xml + generator, shared css/ and js/ (including the tracking module), and the upgraded worker.js.

Ready to scaffold this on your go, or tell me what to adjust in the foundation first.

Noted, and it's an important framing: the hub is top-of-funnel. Genuinely interesting "3D meets AI" content makes 3D GRIT a destination animators return to, and those animators are exactly the buyers for the rigging and SFX tools. That is precisely why "indexable and trackable" matters: indexable so the hub content ranks and animators actually find it, trackable so you can see what draws them and what converts. Let me capture that rationale.

Edit c:\Users\jones\.claude\projects\c--PixelStortionGit\memory\project_3dgrit_new_sandbox.md
Modified
That's captured. The groundwork plan already serves this directly: the hub becomes a registered content type whose items each get their own indexable, structured-data-rich page (so they rank and pull animators in via search), and the tracking layer measures the full draw-to-convert funnel from hub visitor to tool download.

The foundation is fully specced and aligned with your direction:

Registry-driven content spine (hand-authored + future sitt-geo-engine hub entries)
Indexable: per-item static pages, sitemap, extensionless canonicals, JSON-LD
Trackable: consistent event schema across every page and CTA, persisted via the worker
Phase 1: grounded-grit Home page as the first consumer that proves it end to end
I'm holding here for your go-ahead to scaffold it inside 3DGRIT_NEW, since you wanted the plan reviewed before any code. Say the word and I'll start, or tell me what to adjust in the foundation first.

phase 1
I've read the full transcript. Let me verify the current state on disk before continuing, since the crash hit right as I was about to scaffold.

Read C:\Users\jones\.claude\projects\c--PixelStortionGit\memory\project_3dgrit_new_sandbox.md
Globpattern: "3DGRIT_NEW/**/*"
Found 7 files
Globpattern: "**/sitt-geo-engine*/**/*"
Found 101 files
Confirmed the full picture. Let me record the one new fact from the tail of that chat (the engine backup), then sync you on where we are.

Read C:\Users\jones\.claude\projects\c--PixelStortionGit\memory\project_sitt_geo_engine_deferred.md
Edit C:\Users\jones\.claude\projects\c--PixelStortionGit\memory\project_sitt_geo_engine_deferred.md
Added 2 lines
Fully re-synced. Here's the verified state:

Nothing was lost. The crash hit before any code was written. 3DGRIT_NEW/ still contains only RND/ (your 6 docs) + an empty root file. All decisions and context survived in memory.

Confirmed on disk:

Reference docs: 3DGRIT_NEW/RND/ (noted — same place I read them from).
sitt-geo-engine - Copy/ exists alongside the live engine; recorded it as the frozen reference-only backup for the future hub integration.
Everything that's locked (from the corrupted chat):

Stack: hand-written multi-page static, no build step (Cloudflare Pages).
Tone: grounded grit (dark pro-SaaS skeleton; darkness via voice/type/showreels, no SCP gimmicks).
Posts: each is its own indexable page, looks good via one shared template, easy to create via Markdown + a tiny on-demand generator.
Groundwork first: content registry (JSON) → drives nav/sitemap/listings/JSON-LD; full indexability (crawlable HTML, sitemap.xml, robots.txt, extensionless canonicals, OG/Twitter, JSON-LD); tracking on every page/CTA via data-track + upgraded worker.js.
Hub = top-of-funnel audience magnet (sitt-geo-engine-fed later; registry shaped to receive it now, not wired yet).
Phase 1 deliverable: grounded-grit Home page as the first consumer that proves the foundation end-to-end.
That's exactly where we stopped: about to scaffold Phase 1. Say go and I'll scaffold the foundation + Home now, or tell me what to adjust first.

continue
Reading the reference site content and strategy docs so the Home page carries accurate copy, palette, and voice, and loading task tracking.

Read C:\PixelStortionGit\3DGRIT\index_3dGritBase.html
Let me finish reading the reference: the rest of the HTML, the worker, and the blog manifest.

Read C:\PixelStortionGit\3DGRIT\index_3dGritBase.html (lines 991-1278)
Read C:\PixelStortionGit\3DGRIT\worker.js
Read C:\PixelStortionGit\3DGRIT\_old\blog\posts.json
I have the full reference now. Let me set up tracking and do one quick check for any existing domain/canonical hints before I write canonicals.

Update Todos

Check reference for domain/canonical hints

Create content registry + site config (content/site.json, content/registry.json)

Write shared grounded-grit stylesheet (assets/css/grit.css)

Write tracking + site-behavior JS (assets/js/track.js, site.js)

Build the grounded-grit Home page (index.html) with full SEO head + JSON-LD + data-track

Add indexability files (robots.txt, sitemap.xml seeded with Home)

Upgrade the analytics/forms worker (worker.js)
Grep "(canonical|og:url|3dgrit\.com|https?://[a-z0-9.-]*grit|pixelstortion\.com)" (in C:\PixelStortionGit\3DGRIT)
1 line of output
No domain hints exist in the reference, so I'll centralize the base URL in site.json (one-line change later) and flag it for you. Scaffolding the foundation now.

Update Todos

Check reference for domain/canonical hints

Create content registry + site config (content/site.json, content/registry.json)

Write shared grounded-grit stylesheet (assets/css/grit.css)

Write tracking + site-behavior JS (assets/js/track.js, site.js)

Build the grounded-grit Home page (index.html) with full SEO head + JSON-LD + data-track

Add indexability files (robots.txt, sitemap.xml seeded with Home)

Upgrade the analytics/forms worker (worker.js)
Write C:\PixelStortionGit\3DGRIT_NEW\content\site.json
46 lines
{
  "_meta": {
    "purpose": "Global site configuration. Single source of truth for brand, base URL, navigation, and footer. Read by the (future) generator and used to keep every page's <head>, nav, and footer consistent.",
    "baseUrlNote": "PROVISIONAL — confirm the real production domain. Canonicals/og:url/sitemap are built from baseUrl and MUST stay extensionless (Cloudflare strips .html via 308). Change in one place here."
  },
  "baseUrl": "https://3dgrit.com",
  "brand": {
    "name": "3D GRIT",
    "nameHtml": "3D&nbsp;<span>GRIT</span>",
    "tagline": "Tools with weight.",
    "studio": "PixelStortion",
    "description": "A modular auto-rigging and pipeline toolkit for Blender, built by artists who ship. Rigging, Maya-muscle-memory bridges, retopology, and a feed of the most interesting work happening where 3D meets AI.",
    "twitter": "",
    "ogImage": "/assets/img/og-default.png"
  },
  "nav": [
    { "label": "Home", "href": "/" },
    { "label": "Tools", "href": "/#ecosystem" },
    { "label": "Features", "href": "/#features" },
    { "label": "Showcase", "href": "/#showcase" },
    { "label": "Contact", "href": "/#contact" }
  ],
  "footer": {
    "blurb": "Professional auto-rigging and pipeline tools for independent creators and studios. Built for Blender artists, by Blender artists.",
    "columns": [
      {
        "heading": "Tools",
        "links": [
          { "label": "Auto-Rigging Framework", "href": "/#ecosystem" },
          { "label": "MayaForBlender", "href": "/#ecosystem" },
          { "label": "Retopology", "href": "/#ecosystem" }
        ]
      },
      {
        "heading": "Resources",
        "links": [
          { "label": "Documentation", "href": "/#" },
          { "label": "Tutorials", "href": "/#" },
          { "label": "Showcase", "href": "/#showcase" }
        ]
      }
    ],
    "legal": "© 2026 3D GRIT — a PixelStortion studio. All rights reserved."
  }
}
Write C:\PixelStortionGit\3DGRIT_NEW\content\registry.json
180 lines
{
  "_meta": {
    "purpose": "The content spine. Every piece of content on 3D GRIT — pages, tools, blog posts, showreels, and engine-fed hub items — is registered here exactly once. The generator reads this to emit indexable pages, listings, and sitemap.xml. Add an item here and it flows everywhere.",
    "rules": [
      "canonicalPath is ALWAYS extensionless (Cloudflare 308-strips .html). The generator writes <slug>.html but links/canonicals use the extensionless path.",
      "Only items with status 'published' AND an existing page are written to sitemap.xml.",
      "status: published (live) | draft (authored, not live) | planned (backlog) | candidate (engine-suggested, awaiting approval).",
      "Every item carries a stable id and slug so it is independently trackable in analytics."
    ],
    "types": {
      "page": "Top-level site page (home, pricing, contact).",
      "tool": "A product in the ecosystem. Extra fields: tier (free|pro), availability (available|soon), keywordTarget.",
      "blog": "Tutorial / dev-log post. Extra fields: video, thumbnail, subtitle, excerpt.",
      "article": "Long-tail SEO article targeting a specific intent query. Extra field: keywordTarget.",
      "showreel": "Crime-fiction / SFX reel. Extra fields: video, thumbnail, credits.",
      "hub-item": "An engine-curated '3D meets AI' entry (film, workflow, tool). Extra fields: source, creatorCredit, toolsUsed[], whyInteresting, curationScore (0-1, higher = more positive signal), status starts at 'candidate'. Designed to receive sitt-geo-engine (Gemini Flash) output later; NOT wired yet."
    }
  },
  "items": [
    {
      "id": "home",
      "type": "page",
      "slug": "index",
      "title": "3D GRIT — Auto-Rigging & Pipeline Tools for Blender",
      "description": "A modular auto-rigging framework and pipeline toolkit for Blender. Build bipeds, quadrupeds, and mechanical rigs in seconds. Maya-muscle-memory bridges, retopology, and game-ready assets.",
      "canonicalPath": "/",
      "status": "published",
      "date": "2026-05-29",
      "tags": ["blender", "rigging", "pipeline", "vfx"],
      "keywordTarget": "blender auto rigging framework"
    },

    {
      "id": "auto-rigging-framework",
      "type": "tool",
      "slug": "auto-rigging-framework",
      "title": "Auto-Rigging Framework — 3D GRIT",
      "description": "The core of 3D GRIT. Modular bone components, IK/FK switching, and weight tools to build complex bipeds, quadrupeds, and mechanical rigs in seconds.",
      "canonicalPath": "/tools/auto-rigging-framework",
      "status": "planned",
      "tier": "free",
      "availability": "available",
      "date": "2026-05-29",
      "tags": ["rigging", "blender", "ik-fk", "weights"],
      "keywordTarget": "blender auto rigging addon"
    },
    {
      "id": "auto-rig-pro-face",
      "type": "tool",
      "slug": "auto-rig-pro-face",
      "title": "Auto-Rig Pro & Face Rig — 3D GRIT",
      "description": "Facial blend-shape rigs, quadruped expansions, advanced constraint systems, and studio-grade export pipelines.",
      "canonicalPath": "/tools/auto-rig-pro-face",
      "status": "planned",
      "tier": "pro",
      "availability": "soon",
      "date": "2026-05-29",
      "tags": ["rigging", "facial", "blendshapes", "pro"],
      "keywordTarget": "blender facial rig blendshapes"
    },
    {
      "id": "mayaforblender",
      "type": "tool",
      "slug": "mayaforblender",
      "title": "MayaForBlender — 3D GRIT",
      "description": "The essential pipeline bridge. Alt-navigation, QWER manipulation hotkeys, and Outliner hierarchy sync — your Maya muscle memory, preserved in Blender.",
      "canonicalPath": "/tools/mayaforblender",
      "status": "planned",
      "tier": "free",
      "availability": "available",
      "date": "2026-05-29",
      "tags": ["maya", "blender", "keymap", "workflow"],
      "keywordTarget": "maya keymap for blender"
    },
    {
      "id": "mayaforblender-pro",
      "type": "tool",
      "slug": "mayaforblender-pro",
      "title": "MayaForBlender Pro — 3D GRIT",
      "description": "Full shelf mapping, marking menus, custom viewport overlays, and production pipeline integrations.",
      "canonicalPath": "/tools/mayaforblender-pro",
      "status": "planned",
      "tier": "pro",
      "availability": "soon",
      "date": "2026-05-29",
      "tags": ["maya", "blender", "pro", "workflow"],
      "keywordTarget": "maya marking menus in blender"
    },
    {
      "id": "retopology-tool",
      "type": "tool",
      "slug": "retopology-tool",
      "title": "Retopology Tool — 3D GRIT",
      "description": "Quad-draw retopology with auto-merge vertices, snapping, and face-aware topology flow. Clean meshes, fast.",
      "canonicalPath": "/tools/retopology-tool",
      "status": "planned",
      "tier": "free",
      "availability": "available",
      "date": "2026-05-29",
      "tags": ["retopology", "blender", "topology", "game-ready"],
      "keywordTarget": "blender quad draw retopology addon"
    },
    {
      "id": "retopology-pro",
      "type": "tool",
      "slug": "retopology-pro",
      "title": "Retopology Pro — 3D GRIT",
      "description": "Automated quad-flow suggestions, LOD generation, and batch retopology for game-ready asset pipelines.",
      "canonicalPath": "/tools/retopology-pro",
      "status": "planned",
      "tier": "pro",
      "availability": "soon",
      "date": "2026-05-29",
      "tags": ["retopology", "blender", "pro", "lod"],
      "keywordTarget": "automatic retopology blender"
    },

    {
      "id": "bipedal-rig-foundations",
      "type": "blog",
      "slug": "bipedal-rig-foundations",
      "title": "Bipedal Rig Foundations",
      "subtitle": "Building the skeletal architecture from scratch",
      "description": "The first pass at a production-grade bipedal rig. Skeleton hierarchy, IK/FK switching foundations, and why most auto-riggers miss the point.",
      "excerpt": "The first pass at a production-grade bipedal rig. Skeleton hierarchy, IK/FK switching foundations, and why most auto-riggers miss the point.",
      "canonicalPath": "/blog/bipedal-rig-foundations",
      "status": "planned",
      "date": "2026-04-20",
      "tags": ["rigging", "bipedal", "blender"],
      "thumbnail": "https://img.youtube.com/vi/EwoU5QGHSfc/maxresdefault.jpg",
      "video": "https://www.youtube.com/embed/EwoU5QGHSfc"
    },
    {
      "id": "automated-facial-rigging-blendshapes",
      "type": "blog",
      "slug": "automated-facial-rigging-blendshapes",
      "title": "Automated Facial Rigging",
      "subtitle": "Generating blendshapes to drive bones",
      "description": "Auto-generating a full suite of facial blendshapes from a single input shape, and wiring them directly to the underlying bone structure.",
      "excerpt": "Auto-generating a full suite of facial blendshapes from a single input shape, and wiring them directly to the underlying bone structure.",
      "canonicalPath": "/blog/automated-facial-rigging-blendshapes",
      "status": "planned",
      "date": "2026-04-19",
      "tags": ["rigging", "facial", "blender", "automation"],
      "thumbnail": "https://img.youtube.com/vi/xg_fJ5Va_4k/maxresdefault.jpg",
      "video": "https://www.youtube.com/embed/xg_fJ5Va_4k"
    },
    {
      "id": "dynamic-control-shape-switching",
      "type": "blog",
      "slug": "dynamic-control-shape-switching",
      "title": "Dynamic Control Shapes",
      "subtitle": "Switching control types on the fly",
      "description": "Building a custom tool panel to automatically swap control curves based on context, visibility needs, and animator preference.",
      "excerpt": "Building a custom tool panel to automatically swap control curves based on context, visibility needs, and animator preference.",
      "canonicalPath": "/blog/dynamic-control-shape-switching",
      "status": "planned",
      "date": "2026-04-18",
      "tags": ["tools", "ui", "blender"],
      "thumbnail": "https://img.youtube.com/vi/2gn7QxH5Rlk/maxresdefault.jpg",
      "video": "https://www.youtube.com/embed/2gn7QxH5Rlk"
    },
    {
      "id": "basic-ik-fk-auto-clavicle",
      "type": "blog",
      "slug": "basic-ik-fk-auto-clavicle",
      "title": "Auto Clavicle / FK IK",
      "subtitle": "Cracking the shoulder complex",
      "description": "An early prototype building out the foundational FK/IK limb logic and solving the notoriously difficult automatic clavicle rotation in Blender.",
      "excerpt": "An early prototype building out the foundational FK/IK limb logic and solving the notoriously difficult automatic clavicle rotation in Blender.",
      "canonicalPath": "/blog/basic-ik-fk-auto-clavicle",
      "status": "planned",
      "date": "2026-03-15",
      "tags": ["rigging", "bipedal", "blender"],
      "thumbnail": "https://img.youtube.com/vi/axuYejqu9Os/maxresdefault.jpg",
      "video": "https://www.youtube.com/embed/axuYejqu9Os"
    }
  ]
}
Config spine done. Now the shared grounded-grit stylesheet.

Update Todos

Check reference for domain/canonical hints

Create content registry + site config (content/site.json, content/registry.json)

Write shared grounded-grit stylesheet (assets/css/grit.css)

Write tracking + site-behavior JS (assets/js/track.js, site.js)

Build the grounded-grit Home page (index.html) with full SEO head + JSON-LD + data-track

Add indexability files (robots.txt, sitemap.xml seeded with Home)

Upgrade the analytics/forms worker (worker.js)
Write C:\PixelStortionGit\3DGRIT_NEW\assets\css\grit.css
445 lines
/* ============================================================
   3D GRIT — shared stylesheet (grounded grit)
   Dark professional-SaaS skeleton. Grit lives in tone, type,
   grain and vignette — not gimmicks. Used by every page.
   ============================================================ */

/* ===== Tokens ===== */
:root {
  --slate-50:  #f8fafc; --slate-100: #f1f5f9; --slate-200: #e2e8f0;
  --slate-300: #cbd5e1; --slate-400: #94a3b8; --slate-500: #64748b;
  --slate-600: #475569; --slate-700: #334155; --slate-800: #1e293b;
  --slate-900: #0f172a; --slate-950: #020617;

  --cyan-400:  #22d3ee; --cyan-500:  #06b6d4; --cyan-600: #0891b2;
  --cyan-900:  #164e63;
  --blue-600:  #2563eb;

  /* grounded-grit warm accent — used sparingly for tension, never loud */
  --ember-500: #d97746; --ember-600: #b45309;

  --red-500:   #ef4444; --yellow-500: #eab308; --green-400: #4ade80;

  --bg:        var(--slate-950);
  --ink:       var(--slate-300);
  --ink-dim:   var(--slate-400);
  --line:      var(--slate-800);
  --accent:    var(--cyan-400);

  --maxw: 1280px;
  --font-sans: 'Inter', system-ui, -apple-system, sans-serif;
  --font-mono: 'JetBrains Mono', ui-monospace, monospace;
}

/* ===== Reset & base ===== */
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
html { scroll-behavior: smooth; }
body {
  font-family: var(--font-sans);
  background: var(--bg);
  color: var(--ink);
  line-height: 1.6;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  position: relative;
  overflow-x: hidden;
}
::selection { background: var(--cyan-500); color: #fff; }
a { text-decoration: none; color: inherit; }
button { cursor: pointer; border: none; font-family: inherit; }
input, textarea { font-family: inherit; }
ul, ol { list-style: none; }
img { max-width: 100%; display: block; }

/* ===== Grounded-grit atmosphere: vignette + faint film grain ===== */
/* Cheap, fixed, pointer-transparent. Sets a filmic, slightly heavy mood. */
body::before {
  content: ""; position: fixed; inset: 0; z-index: 1; pointer-events: none;
  background: radial-gradient(120% 90% at 50% 0%, transparent 55%, rgba(2,6,23,.55) 100%);
}
body::after {
  content: ""; position: fixed; inset: 0; z-index: 1; pointer-events: none;
  opacity: .035; mix-blend-mode: overlay;
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='140' height='140'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='2' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E");
}
/* keep interactive layers above the atmosphere */
nav, main, footer, .modal-overlay { position: relative; z-index: 2; }

@media (prefers-reduced-motion: reduce) {
  html { scroll-behavior: auto; }
  .animate-in { opacity: 1 !important; transform: none !important; }
}

/* ===== Utilities ===== */
.container { max-width: var(--maxw); margin: 0 auto; padding: 0 1.5rem; }
.mono { font-family: var(--font-mono); }
.sr-only { position: absolute; width: 1px; height: 1px; overflow: hidden; clip: rect(0,0,0,0); white-space: nowrap; }
.accent { color: var(--accent); }

/* ===== NAV ===== */
#main-nav {
  position: fixed; top: 0; left: 0; width: 100%; z-index: 100;
  padding: 1.5rem 0; transition: all .3s ease;
}
#main-nav.scrolled {
  background: rgba(2,6,23,.92);
  backdrop-filter: blur(12px); -webkit-backdrop-filter: blur(12px);
  border-bottom: 1px solid var(--line);
  padding: 1rem 0;
}
.nav-inner { display: flex; justify-content: space-between; align-items: center; }
.nav-logo { display: flex; align-items: center; gap: .6rem; }
.nav-logo-text { font-size: 1.5rem; font-weight: 800; letter-spacing: .15em; color: #fff; }
.nav-logo-text span { color: var(--accent); }
.nav-links { display: flex; align-items: center; gap: 2rem; }
.nav-links a {
  font-size: .8rem; font-weight: 600; color: var(--ink);
  text-transform: uppercase; letter-spacing: .12em; transition: color .2s;
}
.nav-links a:hover { color: var(--accent); }
.nav-actions { display: flex; align-items: center; gap: 1.5rem; }

.btn-primary {
  background: var(--cyan-500); color: var(--slate-950);
  padding: .6rem 1.5rem; font-weight: 800; font-size: .8rem;
  text-transform: uppercase; letter-spacing: .15em; transition: all .25s;
}
.btn-primary:hover { background: var(--cyan-400); box-shadow: 0 0 20px rgba(6,182,212,.4); }

.mobile-toggle { display: none; background: none; color: var(--ink); }
.mobile-menu {
  display: none; position: absolute; top: 100%; left: 0; width: 100%;
  background: var(--slate-900); border-bottom: 1px solid var(--line);
  padding: 1.5rem; flex-direction: column; gap: 1rem;
}
.mobile-menu.open { display: flex; }
.mobile-menu a { font-size: 1.1rem; font-weight: 500; color: var(--ink); transition: color .2s; }
.mobile-menu a:hover { color: var(--accent); }
.mobile-menu .btn-primary { width: 100%; text-align: center; padding: .8rem; margin-top: .5rem; }

@media (max-width: 768px) {
  .nav-links, .nav-actions { display: none; }
  .mobile-toggle { display: block; }
}

/* ===== HERO ===== */
.hero {
  position: relative; min-height: 100vh; display: flex; align-items: center;
  padding-top: 5rem; overflow: hidden; background: var(--slate-950);
}
.hero-grid-bg {
  position: absolute; inset: 0; z-index: 0; opacity: .18; pointer-events: none;
  background-image:
    linear-gradient(rgba(6,182,212,.1) 1px, transparent 1px),
    linear-gradient(90deg, rgba(6,182,212,.1) 1px, transparent 1px);
  background-size: 40px 40px;
  -webkit-mask-image: radial-gradient(100% 80% at 50% 30%, #000 40%, transparent 100%);
          mask-image: radial-gradient(100% 80% at 50% 30%, #000 40%, transparent 100%);
}
.hero-gradient-overlay {
  position: absolute; inset: 0; z-index: 0;
  background: linear-gradient(to bottom, transparent, rgba(2,6,23,.8), var(--slate-950));
}
.hero-content {
  position: relative; z-index: 10; display: grid;
  grid-template-columns: 1fr 1fr; gap: 3rem; align-items: center;
}
@media (max-width: 1024px) { .hero-content { grid-template-columns: 1fr; } }

.hero-left { display: flex; flex-direction: column; gap: 2rem; }
.hero-badge {
  display: inline-flex; align-self: flex-start; align-items: center; gap: .5rem;
  padding: .35rem .9rem; border: 1px solid rgba(6,182,212,.3);
  border-radius: 999px; background: rgba(22,78,99,.3); backdrop-filter: blur(4px);
  font-size: .7rem; font-weight: 700; color: var(--accent);
  text-transform: uppercase; letter-spacing: .15em;
}
.hero h1 { font-size: clamp(2.8rem, 6vw, 4.6rem); font-weight: 900; color: #fff; line-height: 1.05; letter-spacing: -.01em; }
.hero h1 .gradient-text {
  background: linear-gradient(135deg, var(--cyan-400), var(--blue-600));
  -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;
}
.hero-desc {
  font-size: 1.1rem; color: var(--ink-dim); max-width: 560px; line-height: 1.8;
  border-left: 2px solid rgba(6,182,212,.5); padding-left: 1.5rem;
}
.hero-kicker {
  font-family: var(--font-mono); font-size: .8rem; letter-spacing: .25em;
  text-transform: uppercase; color: var(--ember-500);
}
.hero-buttons { display: flex; flex-wrap: wrap; gap: 1rem; }
.hero-buttons .btn-primary { padding: 1rem 2rem; display: inline-flex; align-items: center; gap: .5rem; }
.btn-outline {
  border: 1px solid var(--slate-700); background: none; color: var(--ink);
  padding: 1rem 2rem; font-weight: 800; font-size: .8rem; text-transform: uppercase;
  letter-spacing: .15em; transition: all .25s; display: inline-flex; align-items: center; gap: .5rem;
}
.btn-outline:hover { border-color: var(--accent); color: var(--accent); }

/* Hero visual mock */
.hero-visual { position: relative; }
.hero-visual-glow {
  position: absolute; inset: -4px;
  background: linear-gradient(135deg, var(--cyan-500), var(--blue-600));
  border-radius: 12px; filter: blur(20px); opacity: .25; transition: opacity 1s;
}
.hero-visual:hover .hero-visual-glow { opacity: .5; }
.hero-visual-frame {
  position: relative; background: var(--slate-900); border: 1px solid var(--line);
  border-radius: 12px; padding: .5rem; box-shadow: 0 25px 50px -12px rgba(0,0,0,.5);
}
.mock-window { background: var(--slate-950); border-radius: 8px; overflow: hidden; aspect-ratio: 16/10; display: flex; flex-direction: column; }
.mock-titlebar { height: 32px; background: var(--slate-800); display: flex; align-items: center; padding: 0 1rem; gap: .5rem; border-bottom: 1px solid var(--slate-700); }
.mock-dot { width: 10px; height: 10px; border-radius: 50%; }
.mock-dot.red { background: var(--red-500); }
.mock-dot.yellow { background: var(--yellow-500); }
.mock-dot.green { background: #22c55e; }
.mock-filename { margin-left: 1rem; font-size: .7rem; color: var(--ink-dim); }
.mock-body { display: flex; flex: 1; position: relative; }
.mock-sidebar { width: 25%; border-right: 1px solid var(--line); padding: 1rem; display: flex; flex-direction: column; gap: .6rem; }
.mock-sidebar-line { height: 8px; border-radius: 4px; background: var(--slate-800); }
.mock-sidebar-item { display: flex; align-items: center; gap: .5rem; }
.mock-sidebar-check { width: 12px; height: 12px; border: 1px solid rgba(6,182,212,.5); border-radius: 2px; flex-shrink: 0; }
.mock-viewport { flex: 1; background: var(--slate-900); display: flex; align-items: center; justify-content: center; position: relative; overflow: hidden; }
.mock-gridlines { position: absolute; inset: 0; display: grid; grid-template-columns: repeat(6,1fr); grid-template-rows: repeat(6,1fr); opacity: .1; }
.mock-gridlines div { border: 1px solid var(--slate-700); }
.mock-figure { position: relative; width: 100px; height: 150px; border: 2px solid rgba(6,182,212,.5); border-radius: 50%; display: flex; align-items: center; justify-content: center; }
.mock-head { position: absolute; top: -28px; left: 50%; transform: translateX(-50%); width: 50px; height: 50px; border: 2px solid var(--cyan-400); border-radius: 50%; background: rgba(15,23,42,.5); backdrop-filter: blur(4px); }
.mock-spine { width: 2px; height: 100%; background: rgba(6,182,212,.5); }
.mock-arms { position: absolute; top: 33%; left: 50%; transform: translateX(-50%); width: 150px; height: 2px; background: rgba(6,182,212,.5); }
.mock-info { position: absolute; top: 8px; right: 8px; background: rgba(30,41,59,.8); padding: .5rem; border-radius: 4px; border: 1px solid var(--slate-700); font-size: 9px; color: #fff; line-height: 1.4; }
.mock-info .active { color: var(--green-400); }
.mock-info .enabled { color: var(--cyan-400); }

/* ===== Section common ===== */
.section { padding: 6rem 0; }
.section-title { text-align: center; margin-bottom: 4rem; }
.section-title h2 { font-size: clamp(1.8rem, 4vw, 3rem); font-weight: 900; color: #fff; text-transform: uppercase; letter-spacing: .15em; }
.section-title .subtitle { display: block; color: var(--cyan-500); font-size: clamp(1.1rem, 3vw, 1.8rem); margin-top: .25rem; }
.section-divider { width: 96px; height: 4px; background: var(--cyan-500); margin: 1.5rem auto 0; position: relative; }
.section-divider::after { content: ""; position: absolute; inset: 0; background: var(--ember-500); width: 28px; }

/* ===== ECOSYSTEM (bento) ===== */
#ecosystem { padding: 6rem 0; background: var(--slate-950); }
.bento-grid { display: grid; grid-template-columns: repeat(6, 1fr); gap: 1.25rem; }
@media (max-width: 1024px) { .bento-grid { grid-template-columns: repeat(4, 1fr); } }
@media (max-width: 640px)  { .bento-grid { grid-template-columns: 1fr; } }

.ecosystem-card {
  position: relative; padding: 2rem; overflow: hidden;
  background: var(--slate-900); border: 1px solid var(--line); border-radius: 16px;
  transition: all .35s; display: flex; flex-direction: column; justify-content: flex-end;
}
.ecosystem-card:hover { border-color: rgba(6,182,212,.4); box-shadow: 0 8px 40px -12px rgba(6,182,212,.15); }

.card-flagship { grid-column: span 4; grid-row: span 2; min-height: 420px; }
@media (max-width: 1024px) { .card-flagship { grid-column: span 4; } }
@media (max-width: 640px)  { .card-flagship { grid-column: span 1; min-height: 320px; } }
.card-flagship .card-video-wrap { position: absolute; inset: 0; z-index: 0; border-radius: 16px; overflow: hidden; }
.card-flagship .card-video-wrap video { width: 100%; height: 100%; object-fit: cover; opacity: .35; }
.card-flagship .card-video-wrap .video-placeholder {
  width: 100%; height: 100%;
  background: linear-gradient(135deg, var(--slate-800) 0%, var(--slate-950) 100%);
  display: flex; align-items: center; justify-content: center;
  color: var(--slate-600); font-size: .8rem; letter-spacing: .1em; text-align: center; padding: 1rem;
}
.card-flagship .card-body { position: relative; z-index: 1; }

.card-companion { grid-column: span 2; }
@media (max-width: 640px) { .card-companion { grid-column: span 1; } }
.card-muted { opacity: .62; border-style: dashed; }
.card-muted:hover { opacity: .9; }
.card-medium { grid-column: span 3; }
@media (max-width: 1024px) { .card-medium { grid-column: span 2; } }
@media (max-width: 640px)  { .card-medium { grid-column: span 1; } }
.card-small { grid-column: span 3; }
@media (max-width: 1024px) { .card-small { grid-column: span 2; } }
@media (max-width: 640px)  { .card-small { grid-column: span 1; } }

.card-tier-badge {
  display: inline-flex; align-self: flex-start; padding: .25rem .65rem; border-radius: 999px;
  font-size: .6rem; font-weight: 800; text-transform: uppercase; letter-spacing: .15em; margin-bottom: .75rem;
}
.badge-free { background: rgba(34,211,238,.15); color: var(--cyan-400); border: 1px solid rgba(34,211,238,.3); }
.badge-pro  { background: rgba(99,102,241,.15); color: #818cf8; border: 1px solid rgba(99,102,241,.3); }
.badge-soon { background: rgba(217,119,70,.12); color: var(--ember-500); border: 1px solid rgba(217,119,70,.3); }

.ecosystem-card h3 { font-size: 1.25rem; font-weight: 800; color: #fff; margin-bottom: .5rem; transition: color .3s; }
.ecosystem-card:hover h3 { color: var(--accent); }
.ecosystem-card .card-desc { font-size: .85rem; color: var(--ink-dim); line-height: 1.7; margin-bottom: 1.25rem; }

.btn-ecosystem {
  display: inline-flex; align-items: center; gap: .5rem; padding: .7rem 1.5rem;
  font-weight: 800; font-size: .75rem; text-transform: uppercase; letter-spacing: .15em;
  transition: all .25s; border: none; cursor: pointer; font-family: inherit; align-self: flex-start;
}
.btn-eco-primary { background: var(--cyan-500); color: var(--slate-950); }
.btn-eco-primary:hover { background: var(--cyan-400); box-shadow: 0 0 20px rgba(6,182,212,.4); }
.btn-eco-outline { background: none; border: 1px solid var(--slate-600); color: var(--ink-dim); }
.btn-eco-outline:hover { border-color: var(--accent); color: var(--accent); }

/* ===== FEATURES ===== */
#features { background: var(--slate-950); }
.features-grid { display: grid; grid-template-columns: repeat(3,1fr); gap: 1.5rem; }
@media (max-width: 1024px) { .features-grid { grid-template-columns: repeat(2,1fr); } }
@media (max-width: 640px)  { .features-grid { grid-template-columns: 1fr; } }

.feature-card {
  position: relative; padding: 1.5rem; overflow: hidden;
  background: var(--slate-900); border: 1px solid var(--line); border-radius: 12px; transition: all .35s;
}
.feature-card:hover { border-color: rgba(6,182,212,.5); box-shadow: 0 5px 30px -10px rgba(6,182,212,.15); }
.feature-card .bg-icon { position: absolute; top: 0; right: 0; padding: 1rem; opacity: .07; transition: opacity .3s; }
.feature-card:hover .bg-icon { opacity: .18; }
.feature-card .bg-icon svg { width: 64px; height: 64px; color: var(--cyan-400); }
.feature-icon-wrap {
  width: 48px; height: 48px; border-radius: 12px; background: var(--slate-800);
  display: flex; align-items: center; justify-content: center; margin-bottom: 1rem; transition: background .3s;
}
.feature-card:hover .feature-icon-wrap { background: rgba(6,182,212,.15); }
.feature-icon-wrap svg { width: 24px; height: 24px; color: var(--cyan-400); }
.feature-card h3 { font-size: 1.15rem; font-weight: 700; color: #fff; margin-bottom: .5rem; transition: color .3s; }
.feature-card:hover h3 { color: var(--accent); }
.feature-card p { font-size: .875rem; color: var(--ink-dim); line-height: 1.7; }

.features-disclosure { margin-top: 3rem; }
.features-disclosure summary {
  cursor: pointer; list-style: none; display: flex; align-items: center; justify-content: center;
  gap: .5rem; padding: 1rem 2rem; border: 1px solid var(--slate-700); border-radius: 8px;
  background: var(--slate-900); color: var(--ink); font-weight: 700; font-size: .8rem;
  text-transform: uppercase; letter-spacing: .12em; transition: all .3s; margin-bottom: 2rem;
}
.features-disclosure summary:hover { border-color: var(--accent); color: var(--accent); }
.features-disclosure summary::-webkit-details-marker { display: none; }
.features-disclosure[open] summary .expand-icon { transform: rotate(180deg); }
.expand-icon { transition: transform .3s; display: inline-flex; }

/* ===== SHOWCASE ===== */
#showcase {
  padding: 5rem 0; background: var(--slate-900);
  border-top: 1px solid var(--line); border-bottom: 1px solid var(--line);
}
.showcase-card {
  background: var(--slate-950); border: 1px solid var(--line); border-radius: 16px; overflow: hidden;
  box-shadow: 0 25px 50px -12px rgba(0,0,0,.5); display: flex; flex-direction: row;
}
@media (max-width: 768px) { .showcase-card { flex-direction: column; } }
.showcase-video { flex: 1; aspect-ratio: 16/9; background: #000; position: relative; cursor: pointer; }
.showcase-video:hover .play-circle { transform: translate(-50%,-50%) scale(1.12); }
.play-circle {
  position: absolute; top: 50%; left: 50%; transform: translate(-50%,-50%);
  width: 80px; height: 80px; border-radius: 50%; background: rgba(6,182,212,.2);
  border: 1px solid rgba(6,182,212,.5); backdrop-filter: blur(4px);
  display: flex; align-items: center; justify-content: center; transition: transform .3s;
}
.play-circle svg { width: 32px; height: 32px; color: var(--cyan-400); margin-left: 4px; }
.showcase-video-info { position: absolute; bottom: 0; left: 0; right: 0; padding: 1.5rem; background: linear-gradient(to top, rgba(0,0,0,.9), transparent); }
.showcase-video-info h3 { font-size: 1.25rem; font-weight: 700; color: #fff; }
.showcase-video-info p { font-size: .8rem; color: var(--cyan-400); }
.showcase-steps {
  width: 380px; background: var(--slate-900); padding: 2rem; border-left: 1px solid var(--line);
  display: flex; flex-direction: column; justify-content: center;
}
@media (max-width: 768px) { .showcase-steps { width: 100%; border-left: none; border-top: 1px solid var(--line); } }
.showcase-steps h4 { font-weight: 700; color: #fff; text-transform: uppercase; letter-spacing: .12em; margin-bottom: 1.5rem; display: flex; align-items: center; gap: .5rem; font-size: .95rem; }
.showcase-steps h4 svg { width: 20px; height: 20px; color: var(--cyan-400); }
.steps-list { display: flex; flex-direction: column; gap: 1.25rem; }
.step-item { display: flex; align-items: center; gap: 1rem; color: var(--ink); font-size: .9rem; }
.step-num { width: 32px; height: 32px; border-radius: 6px; flex-shrink: 0; background: var(--slate-800); border: 1px solid var(--slate-700); display: flex; align-items: center; justify-content: center; font-weight: 800; color: var(--cyan-500); font-size: .85rem; }
.btn-outline-full { margin-top: 2rem; width: 100%; text-align: center; border: 1px solid var(--cyan-500); background: none; color: var(--cyan-400); padding: .8rem; font-weight: 800; font-size: .75rem; text-transform: uppercase; letter-spacing: .15em; transition: all .25s; }
.btn-outline-full:hover { background: var(--cyan-500); color: var(--slate-950); }

/* ===== ASSETS ===== */
#assets { background: var(--slate-950); }
.assets-grid { display: flex; align-items: center; gap: 4rem; }
@media (max-width: 768px) { .assets-grid { flex-direction: column; } }
.assets-info { flex: 1; display: flex; flex-direction: column; gap: 1.25rem; }
.assets-info h2 { font-size: 2.2rem; font-weight: 900; color: #fff; }
.assets-info p { font-size: 1.1rem; color: var(--ink-dim); line-height: 1.8; }
.assets-list { display: flex; flex-direction: column; gap: .6rem; margin-bottom: 1rem; }
.assets-list li { display: flex; align-items: center; gap: .5rem; color: var(--ink); }
.assets-list li svg { width: 16px; height: 16px; color: var(--cyan-500); flex-shrink: 0; }
.btn-shop {
  display: inline-block; background: var(--cyan-600); color: #fff; padding: .8rem 2rem; font-weight: 800;
  text-transform: uppercase; letter-spacing: .15em; transition: all .25s; font-size: .85rem;
  box-shadow: 0 10px 15px -3px rgba(0,0,0,.3); align-self: flex-start;
}
.btn-shop:hover { background: var(--cyan-500); }
.assets-visual { flex: 1; position: relative; }
.assets-glow { position: absolute; inset: 0; background: rgba(6,182,212,.2); filter: blur(60px); border-radius: 50%; }
.assets-frame { position: relative; background: var(--slate-900); border: 1px solid var(--line); padding: .5rem; border-radius: 16px; box-shadow: 0 25px 50px -12px rgba(0,0,0,.5); transform: rotate(3deg); transition: transform .5s; }
.assets-frame:hover { transform: rotate(0deg); }
.assets-thumb { aspect-ratio: 1/1; border-radius: 12px; overflow: hidden; position: relative; background: linear-gradient(135deg, var(--slate-800), var(--slate-950)); display: flex; align-items: center; justify-content: center; }
.assets-thumb-radial { position: absolute; inset: 0; opacity: .5; background: radial-gradient(circle at center, rgba(6,182,212,.2) 0%, transparent 70%); }
.assets-label { position: absolute; bottom: 1rem; right: 1rem; font-size: .65rem; color: var(--slate-600); }
.assets-shape { width: 160px; height: 210px; background: var(--slate-800); border-radius: 24px 24px 0 0; position: relative; }
.assets-shape .bar { position: absolute; top: 40px; left: 0; right: 0; height: 6px; background: rgba(22,78,99,.5); }
.assets-shape .arm-l { position: absolute; top: 65px; left: -35px; width: 60px; height: 120px; background: var(--slate-700); border-radius: 50%; transform: rotate(-12deg); }
.assets-shape .arm-r { position: absolute; top: 65px; right: -35px; width: 60px; height: 120px; background: var(--slate-700); border-radius: 50%; transform: rotate(12deg); }

/* ===== CONTACT ===== */
#contact { padding: 6rem 0; background: var(--slate-900); border-top: 1px solid var(--line); }
.contact-wrap { max-width: 720px; margin: 0 auto; text-align: center; }
.contact-wrap h2 { font-size: 2rem; font-weight: 900; color: var(--cyan-400); text-transform: uppercase; letter-spacing: .2em; }
.contact-divider { width: 64px; height: 4px; background: #fff; margin: 1.5rem auto 3rem; }
.contact-form { display: flex; flex-direction: column; gap: 1.25rem; text-align: left; }
.form-row { display: grid; grid-template-columns: 1fr 1fr; gap: 1.25rem; }
@media (max-width: 640px) { .form-row { grid-template-columns: 1fr; } }
.form-group label { display: block; margin-bottom: .5rem; font-size: .7rem; font-weight: 700; color: var(--ink-dim); text-transform: uppercase; letter-spacing: .12em; }
.form-group input, .form-group textarea {
  width: 100%; background: var(--slate-950); border: 1px solid var(--line); color: #fff;
  padding: .75rem; outline: none; transition: border-color .2s; font-size: .95rem;
}
.form-group input:focus, .form-group textarea:focus { border-color: var(--cyan-500); }
.form-group textarea { resize: vertical; }
.btn-submit {
  width: 100%; padding: 1rem; background: var(--cyan-600); color: #fff; font-weight: 800;
  text-transform: uppercase; letter-spacing: .15em; transition: background .25s; font-size: .85rem;
  box-shadow: 0 10px 15px -3px rgba(0,0,0,.3);
}
.btn-submit:hover { background: var(--cyan-500); }
.form-status { font-size: .85rem; margin-top: .25rem; min-height: 1.2em; text-align: center; }
.form-status.ok { color: var(--green-400); }
.form-status.err { color: var(--red-500); }

/* ===== FOOTER ===== */
footer { background: var(--slate-950); padding: 3rem 0; border-top: 1px solid var(--slate-900); }
.footer-grid { display: grid; grid-template-columns: 2fr 1fr 1fr; gap: 2rem; }
@media (max-width: 768px) { .footer-grid { grid-template-columns: 1fr; text-align: center; } .footer-brand { align-items: center; } }
.footer-brand { display: flex; flex-direction: column; gap: 1rem; }
.footer-brand-logo { display: flex; align-items: center; gap: .5rem; }
.footer-brand-logo span { font-size: 1.25rem; font-weight: 800; color: #fff; letter-spacing: .15em; }
.footer-brand-logo span em { font-style: normal; color: var(--cyan-400); }
.footer-brand p { font-size: .85rem; color: var(--slate-500); max-width: 340px; }
.footer-col h4 { font-size: .8rem; font-weight: 700; color: #fff; text-transform: uppercase; letter-spacing: .12em; margin-bottom: 1rem; }
.footer-col ul { display: flex; flex-direction: column; gap: .5rem; }
.footer-col a { font-size: .85rem; color: var(--ink-dim); transition: color .2s; }
.footer-col a:hover { color: var(--accent); }
.footer-bottom { margin-top: 3rem; padding-top: 2rem; border-top: 1px solid var(--slate-900); display: flex; justify-content: space-between; align-items: center; font-size: .7rem; color: var(--slate-600); }
@media (max-width: 768px) { .footer-bottom { flex-direction: column; gap: .5rem; text-align: center; } }

/* ===== MODAL ===== */
.modal-overlay {
  position: fixed; inset: 0; z-index: 1000; background: rgba(2,6,23,.85);
  backdrop-filter: blur(8px); -webkit-backdrop-filter: blur(8px);
  display: flex; align-items: center; justify-content: center;
  opacity: 0; pointer-events: none; transition: opacity .3s ease;
}
.modal-overlay.active { opacity: 1; pointer-events: auto; }
.modal-content { background: var(--slate-900); border: 1px solid var(--slate-700); border-radius: 12px; width: 100%; max-width: 420px; padding: 2.5rem; position: relative; transform: translateY(20px); transition: transform .3s ease; box-shadow: 0 25px 50px -12px rgba(0,0,0,.5); }
.modal-overlay.active .modal-content { transform: translateY(0); }
.modal-close { position: absolute; top: 1rem; right: 1rem; background: none; color: var(--slate-500); transition: color .2s; }
.modal-close:hover { color: var(--accent); }
.modal-header { margin-bottom: 1.5rem; text-align: center; }
.modal-header h3 { font-size: 1.2rem; color: #fff; margin-bottom: .5rem; }
.modal-header p { font-size: .85rem; color: var(--ink-dim); line-height: 1.6; }
.modal-form .form-group input { text-align: center; margin-bottom: 1rem; }
.modal-success { text-align: center; padding: 1rem 0; }
.modal-success svg { margin: 0 auto 1rem; }
.modal-success h4 { color: #fff; font-size: 1.2rem; margin-bottom: .5rem; }
.modal-success p { color: var(--cyan-400); font-size: .85rem; }

/* ===== Animations ===== */
.animate-in { opacity: 0; transform: translateY(30px); transition: opacity .6s ease, transform .6s ease; }
.animate-in.visible { opacity: 1; transform: translateY(0); }
Now the trackable layer and page behaviors.

Update Todos

Check reference for domain/canonical hints

Create content registry + site config (content/site.json, content/registry.json)

Write shared grounded-grit stylesheet (assets/css/grit.css)

Write tracking + site-behavior JS (assets/js/track.js, site.js)

Build the grounded-grit Home page (index.html) with full SEO head + JSON-LD + data-track

Add indexability files (robots.txt, sitemap.xml seeded with Home)

Upgrade the analytics/forms worker (worker.js)
Write C:\PixelStortionGit\3DGRIT_NEW\assets\js\track.js
67 lines
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
Write C:\PixelStortionGit\3DGRIT_NEW\assets\js\site.js
105 lines
/* ============================================================
   3D GRIT — shared page behaviors
   Nav background, mobile menu, scroll-reveal, soft-gate modal,
   and contact form submit. Loaded on every page.
   ============================================================ */
(function () {
  "use strict";

  // --- Scroll-based nav background ---
  var nav = document.getElementById("main-nav");
  if (nav) {
    window.addEventListener("scroll", function () {
      nav.classList.toggle("scrolled", window.scrollY > 20);
    });
  }

  // --- Mobile menu ---
  var mobileToggle = document.getElementById("mobile-toggle");
  var mobileMenu = document.getElementById("mobile-menu");
  if (mobileToggle && mobileMenu) {
    mobileToggle.addEventListener("click", function () { mobileMenu.classList.toggle("open"); });
    mobileMenu.querySelectorAll("a").forEach(function (link) {
      link.addEventListener("click", function () { mobileMenu.classList.remove("open"); });
    });
  }

  // --- Scroll-reveal ---
  if ("IntersectionObserver" in window) {
    var observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) { entry.target.classList.add("visible"); observer.unobserve(entry.target); }
      });
    }, { threshold: 0.15 });
    document.querySelectorAll(".animate-in").forEach(function (el) { observer.observe(el); });
  } else {
    document.querySelectorAll(".animate-in").forEach(function (el) { el.classList.add("visible"); });
  }

  // --- Soft-gate modal (opens on any download_free CTA) ---
  var modal = document.getElementById("capture-modal");
  if (modal) {
    var modalClose = document.getElementById("modal-close-btn");
    var captureForm = document.getElementById("capture-form");
    var successState = document.getElementById("modal-success-state");
    var modalHeader = modal.querySelector(".modal-header");
    var pendingTool = null;

    document.querySelectorAll('[data-track="download_free"]').forEach(function (btn) {
      btn.addEventListener("click", function (e) {
        e.preventDefault();
        pendingTool = btn.getAttribute("data-tool") || null;
        modal.classList.add("active");
        modal.setAttribute("aria-hidden", "false");
      });
    });

    var closeModal = function () {
      modal.classList.remove("active");
      modal.setAttribute("aria-hidden", "true");
      setTimeout(function () {
        if (captureForm) captureForm.style.display = "block";
        if (modalHeader) modalHeader.style.display = "block";
        if (successState) successState.style.display = "none";
        if (captureForm) captureForm.reset();
      }, 300);
    };

    if (modalClose) modalClose.addEventListener("click", closeModal);
    modal.addEventListener("click", function (e) { if (e.target === modal) closeModal(); });
    document.addEventListener("keydown", function (e) { if (e.key === "Escape" && modal.classList.contains("active")) closeModal(); });

    if (captureForm) {
      captureForm.addEventListener("submit", function (e) {
        e.preventDefault();
        var email = document.getElementById("capture-email").value;
        if (window.GRIT && window.GRIT.track) {
          window.GRIT.track("email_capture", { tool: pendingTool, email: email });
        }
        if (captureForm) captureForm.style.display = "none";
        if (modalHeader) modalHeader.style.display = "none";
        if (successState) successState.style.display = "block";
        setTimeout(closeModal, 3000);
      });
    }
  }

  // --- Contact form ---
  var contactForm = document.getElementById("contact-form");
  if (contactForm) {
    var status = document.getElementById("contact-status");
    contactForm.addEventListener("submit", function (e) {
      e.preventDefault();
      var data = {
        name: document.getElementById("contact-name").value,
        email: document.getElementById("contact-email").value,
        subject: document.getElementById("contact-subject").value,
        message: document.getElementById("contact-message").value
      };
      if (window.GRIT && window.GRIT.track) window.GRIT.track("contact_submit", data);
      if (status) { status.textContent = "Message sent. We'll be in touch."; status.className = "form-status ok"; }
      contactForm.reset();
    });
  }
})();
The centerpiece: the grounded-grit Home page with full SEO head, JSON-LD, and registry-tied tracking.

Update Todos

Check reference for domain/canonical hints

Create content registry + site config (content/site.json, content/registry.json)

Write shared grounded-grit stylesheet (assets/css/grit.css)

Write tracking + site-behavior JS (assets/js/track.js, site.js)

Build the grounded-grit Home page (index.html) with full SEO head + JSON-LD + data-track

Add indexability files (robots.txt, sitemap.xml seeded with Home)

Upgrade the analytics/forms worker (worker.js)
Write C:\PixelStortionGit\3DGRIT_NEW\index.html
499 lines
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">

  <!-- ===== Primary meta ===== -->
  <title>3D GRIT — Auto-Rigging &amp; Pipeline Tools for Blender</title>
  <meta name="description" content="A modular auto-rigging framework and pipeline toolkit for Blender. Build bipeds, quadrupeds, and mechanical rigs in seconds. Maya-muscle-memory bridges, retopology, and game-ready assets.">
  <link rel="canonical" href="https://3dgrit.com/">

  <!-- ===== Open Graph ===== -->
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="3D GRIT">
  <meta property="og:title" content="3D GRIT — Auto-Rigging &amp; Pipeline Tools for Blender">
  <meta property="og:description" content="A modular auto-rigging framework and pipeline toolkit for Blender. Tools with weight.">
  <meta property="og:url" content="https://3dgrit.com/">
  <meta property="og:image" content="https://3dgrit.com/assets/img/og-default.png">

  <!-- ===== Twitter ===== -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="3D GRIT — Auto-Rigging &amp; Pipeline Tools for Blender">
  <meta name="twitter:description" content="A modular auto-rigging framework and pipeline toolkit for Blender. Tools with weight.">
  <meta name="twitter:image" content="https://3dgrit.com/assets/img/og-default.png">

  <!-- ===== Tracking endpoint (same-origin worker route) ===== -->
  <meta name="grit:endpoint" content="/api/track">

  <!-- ===== Fonts (non-blocking) ===== -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@400;700&display=swap" rel="stylesheet" media="print" onload="this.media='all'">
  <noscript><link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@400;700&display=swap" rel="stylesheet"></noscript>

  <link rel="stylesheet" href="/assets/css/grit.css">

  <!-- ===== Structured data ===== -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@graph": [
      {
        "@type": "Organization",
        "@id": "https://3dgrit.com/#org",
        "name": "3D GRIT",
        "url": "https://3dgrit.com/",
        "description": "A modular auto-rigging and pipeline toolkit for Blender, built by artists who ship.",
        "logo": "https://3dgrit.com/assets/img/og-default.png",
        "parentOrganization": { "@type": "Organization", "name": "PixelStortion" }
      },
      {
        "@type": "WebSite",
        "@id": "https://3dgrit.com/#website",
        "url": "https://3dgrit.com/",
        "name": "3D GRIT",
        "publisher": { "@id": "https://3dgrit.com/#org" }
      }
    ]
  }
  </script>
</head>

<body data-page-id="home">
  <!-- ===== NAVIGATION ===== -->
  <nav id="main-nav">
    <div class="container nav-inner">
      <div class="nav-logo">
        <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="var(--cyan-400)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16Z"/><path d="m3.3 7 8.7 5 8.7-5"/><path d="M12 22V12"/></svg>
        <span class="nav-logo-text">3D <span>GRIT</span></span>
      </div>

      <div class="nav-links">
        <a href="#home">Home</a>
        <a href="#ecosystem">Tools</a>
        <a href="#features">Features</a>
        <a href="#showcase">Showcase</a>
        <a href="#contact">Contact</a>
      </div>

      <div class="nav-actions">
        <a href="#ecosystem" class="btn-primary" data-track="nav_cta" data-label="Get the tools">Get the Tools</a>
      </div>

      <button class="mobile-toggle" id="mobile-toggle" aria-label="Toggle menu">
        <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><line x1="4" x2="20" y1="12" y2="12"/><line x1="4" x2="20" y1="6" y2="6"/><line x1="4" x2="20" y1="18" y2="18"/></svg>
      </button>
    </div>

    <div class="mobile-menu" id="mobile-menu">
      <a href="#home">Home</a>
      <a href="#ecosystem">Tools</a>
      <a href="#features">Features</a>
      <a href="#showcase">Showcase</a>
      <a href="#contact">Contact</a>
      <a href="#ecosystem" class="btn-primary">Get the Tools</a>
    </div>
  </nav>

  <main>
  <!-- ===== HERO ===== -->
  <section class="hero" id="home">
    <div class="hero-grid-bg"></div>
    <div class="hero-gradient-overlay"></div>

    <div class="container hero-content">
      <div class="hero-left">
        <span class="hero-kicker">Tools with weight</span>
        <h1>
          AUTOMATE YOUR<br>
          <span class="gradient-text">RIGGING PIPELINE</span>
        </h1>
        <p class="hero-desc">
          A modular auto-rigging framework for Blender, built by artists who ship.
          Bipeds, quadrupeds, and custom mechanical rigs in seconds, not hours —
          then the bridges, retopology, and assets to carry them through production.
        </p>
        <div class="hero-buttons">
          <a href="#ecosystem" class="btn-primary" data-track="hero_cta" data-label="Get started">
            Get Started <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m9 18 6-6-6-6"/></svg>
          </a>
          <a href="#showcase" class="btn-outline" data-track="hero_demo" data-label="Watch demo">
            Watch Demo <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polygon points="6 3 20 12 6 21 6 3"/></svg>
          </a>
        </div>
      </div>

      <!-- Hero visual mock-up -->
      <div class="hero-visual">
        <div class="hero-visual-glow"></div>
        <div class="hero-visual-frame">
          <div class="mock-window">
            <div class="mock-titlebar">
              <div class="mock-dot red"></div>
              <div class="mock-dot yellow"></div>
              <div class="mock-dot green"></div>
              <span class="mock-filename mono">3D_Grit_Auto_Rigger.py</span>
            </div>
            <div class="mock-body">
              <div class="mock-sidebar">
                <div class="mock-sidebar-line" style="width:75%"></div>
                <div class="mock-sidebar-line" style="width:50%;margin-bottom:.8rem"></div>
                <div class="mock-sidebar-item"><div class="mock-sidebar-check"></div><div class="mock-sidebar-line" style="width:100%"></div></div>
                <div class="mock-sidebar-item"><div class="mock-sidebar-check"></div><div class="mock-sidebar-line" style="width:100%"></div></div>
                <div class="mock-sidebar-item"><div class="mock-sidebar-check"></div><div class="mock-sidebar-line" style="width:100%"></div></div>
                <div class="mock-sidebar-item"><div class="mock-sidebar-check"></div><div class="mock-sidebar-line" style="width:100%"></div></div>
                <div class="mock-sidebar-item"><div class="mock-sidebar-check"></div><div class="mock-sidebar-line" style="width:100%"></div></div>
                <div class="mock-sidebar-item"><div class="mock-sidebar-check"></div><div class="mock-sidebar-line" style="width:100%"></div></div>
              </div>
              <div class="mock-viewport">
                <div class="mock-gridlines">
                  <div></div><div></div><div></div><div></div><div></div><div></div>
                  <div></div><div></div><div></div><div></div><div></div><div></div>
                  <div></div><div></div><div></div><div></div><div></div><div></div>
                  <div></div><div></div><div></div><div></div><div></div><div></div>
                  <div></div><div></div><div></div><div></div><div></div><div></div>
                  <div></div><div></div><div></div><div></div><div></div><div></div>
                </div>
                <div class="mock-figure">
                  <div class="mock-head"></div>
                  <div class="mock-spine"></div>
                  <div class="mock-arms"></div>
                  <div class="mock-info mono">
                    Bone_L_001 <span class="active">ACTIVE</span><br>
                    IK_Solver: <span class="enabled">ENABLED</span>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- ===== ECOSYSTEM (Bento) ===== -->
  <section id="ecosystem">
    <div class="container">
      <div class="section-title">
        <h2>The Ecosystem<span class="subtitle">— Tools &amp; Pipeline —</span></h2>
        <div class="section-divider"></div>
      </div>

      <div class="bento-grid">

        <!-- Flagship: Auto-Rigging Framework -->
        <div class="ecosystem-card card-flagship animate-in">
          <div class="card-video-wrap">
            <div class="video-placeholder mono">[ AUTO-RIG DEMO REEL — DROP .MP4 HERE ]</div>
          </div>
          <div class="card-body">
            <span class="card-tier-badge badge-free">Free Starter</span>
            <h3 class="mono">Auto-Rigging Framework</h3>
            <p class="card-desc">
              The core of 3D GRIT. Build complex bipeds, quadrupeds, and custom mechanical rigs in seconds.
              Modular bone components, IK/FK switching, and weight tools included.
            </p>
            <button class="btn-ecosystem btn-eco-primary" data-track="download_free" data-tool="auto_rig_basic" data-item="auto-rigging-framework">
              Get Started Free
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m9 18 6-6-6-6"/></svg>
            </button>
          </div>
        </div>

        <!-- Companion: Auto-Rig Pro -->
        <div class="ecosystem-card card-companion card-muted animate-in">
          <span class="card-tier-badge badge-pro">Pro — Coming Soon</span>
          <h3 class="mono">Auto-Rig Pro &amp; Face Rig</h3>
          <p class="card-desc">
            Facial blend-shape rigs, quadruped expansions, advanced constraint systems, and studio-grade export pipelines.
          </p>
          <button class="btn-ecosystem btn-eco-outline" data-track="waitlist_click" data-tool="auto_rig_pro" data-item="auto-rig-pro-face">
            Join Pro Waitlist
          </button>
        </div>

        <!-- MayaForBlender (Free) -->
        <div class="ecosystem-card card-medium animate-in">
          <span class="card-tier-badge badge-free">Free</span>
          <h3 class="mono">MayaForBlender</h3>
          <p class="card-desc">
            The essential pipeline bridge. Alt-navigation, QWER manipulation hotkeys,
            and Outliner hierarchy sync — your Maya muscle memory, preserved.
          </p>
          <button class="btn-ecosystem btn-eco-primary" data-track="download_free" data-tool="maya_bridge_basic" data-item="mayaforblender">
            Download Free Basic
          </button>
        </div>

        <!-- MayaForBlender Pro -->
        <div class="ecosystem-card card-small card-muted animate-in">
          <span class="card-tier-badge badge-pro">Pro — Coming Soon</span>
          <h3 class="mono">MayaForBlender Pro</h3>
          <p class="card-desc">
            Full shelf mapping, marking menus, custom viewport overlays, and production pipeline integrations.
          </p>
          <button class="btn-ecosystem btn-eco-outline" data-track="waitlist_click" data-tool="maya_bridge_pro" data-item="mayaforblender-pro">
            Join Waitlist
          </button>
        </div>

        <!-- Retopology (Free) -->
        <div class="ecosystem-card card-medium animate-in">
          <span class="card-tier-badge badge-free">Free</span>
          <h3 class="mono">Retopology Tool</h3>
          <p class="card-desc">
            Quad-draw retopology with auto-merge vertices, snapping, and face-aware topology flow. Clean meshes, fast.
          </p>
          <button class="btn-ecosystem btn-eco-primary" data-track="download_free" data-tool="retopo_basic" data-item="retopology-tool">
            Download Free Basic
          </button>
        </div>

        <!-- Retopology Pro -->
        <div class="ecosystem-card card-small card-muted animate-in">
          <span class="card-tier-badge badge-pro">Pro — Coming Soon</span>
          <h3 class="mono">Retopology Pro</h3>
          <p class="card-desc">
            Automated quad-flow suggestions, LOD generation, and batch retopology for game-ready asset pipelines.
          </p>
          <button class="btn-ecosystem btn-eco-outline" data-track="waitlist_click" data-tool="retopo_pro" data-item="retopology-pro">
            Join Waitlist
          </button>
        </div>

      </div>
    </div>
  </section>

  <!-- ===== FEATURES ===== -->
  <section id="features" class="section">
    <div class="container">
      <div class="section-title">
        <h2>3D GRIT Rig<span class="subtitle">— Auto-Rig Features —</span></h2>
        <div class="section-divider"></div>
      </div>

      <details class="features-disclosure" open>
        <summary>
          <span class="expand-icon">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m6 9 6 6 6-6"/></svg>
          </span>
          Auto-Rig Features
        </summary>

        <div class="features-grid">
          <div class="feature-card animate-in">
            <div class="bg-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m12.83 2.18a2 2 0 0 0-1.66 0L2.6 6.08a1 1 0 0 0 0 1.83l8.58 3.91a2 2 0 0 0 1.66 0l8.58-3.9a1 1 0 0 0 0-1.83Z"/><path d="m22.54 12.43-8.58 3.91a2 2 0 0 1-1.66 0L3.72 12.43"/><path d="m22.54 16.43-8.58 3.91a2 2 0 0 1-1.66 0L3.72 16.43"/></svg></div>
            <div class="feature-icon-wrap"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m12.83 2.18a2 2 0 0 0-1.66 0L2.6 6.08a1 1 0 0 0 0 1.83l8.58 3.91a2 2 0 0 0 1.66 0l8.58-3.9a1 1 0 0 0 0-1.83Z"/><path d="m22.54 12.43-8.58 3.91a2 2 0 0 1-1.66 0L3.72 12.43"/><path d="m22.54 16.43-8.58 3.91a2 2 0 0 1-1.66 0L3.72 16.43"/></svg></div>
            <h3 class="mono">Modular Components</h3>
            <p>Rig bipeds, quadrupeds, and custom creatures with a single click using a smart component library.</p>
          </div>
          <div class="feature-card animate-in">
            <div class="bg-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 3v16h16"/><path d="m5 19 6-6"/><path d="m2 6 3-3 3 3"/><path d="m18 16 3 3-3 3"/></svg></div>
            <div class="feature-icon-wrap"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 3v16h16"/><path d="m5 19 6-6"/><path d="m2 6 3-3 3 3"/><path d="m18 16 3 3-3 3"/></svg></div>
            <h3 class="mono">Bone Alignment Tool</h3>
            <p>Precise control over placement and orientation of bones. Snap, align, and distribute with mathematical accuracy.</p>
          </div>
          <div class="feature-card animate-in">
            <div class="bg-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 7h-9"/><path d="M14 17H5"/><circle cx="17" cy="17" r="3"/><circle cx="7" cy="7" r="3"/></svg></div>
            <div class="feature-icon-wrap"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 7h-9"/><path d="M14 17H5"/><circle cx="17" cy="17" r="3"/><circle cx="7" cy="7" r="3"/></svg></div>
            <h3 class="mono">Weight Saving Tools</h3>
            <p>Advanced skin weight utilities to save, copy, and mirror weights across different meshes seamlessly.</p>
          </div>
          <div class="feature-card animate-in">
            <div class="bg-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M15.6 2.7a10 10 0 0 1 5.7 5.7"/><circle cx="12" cy="12" r="2"/><path d="M13.4 2.1a10 10 0 0 0-9.3 9.3"/><path d="m2 2 20 20"/></svg></div>
            <div class="feature-icon-wrap"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M15.6 2.7a10 10 0 0 1 5.7 5.7"/><circle cx="12" cy="12" r="2"/><path d="M13.4 2.1a10 10 0 0 0-9.3 9.3"/><path d="m2 2 20 20"/></svg></div>
            <h3 class="mono">Control Curve Tool</h3>
            <p>Choose from a huge library of curve shapes for bone display. Customize aesthetics instantly.</p>
          </div>
          <div class="feature-card animate-in">
            <div class="bg-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect width="16" height="20" x="4" y="2" rx="2"/><line x1="8" x2="16" y1="6" y2="6"/><line x1="16" x2="16" y1="14" y2="18"/><path d="M16 10h.01"/><path d="M12 10h.01"/><path d="M8 10h.01"/><path d="M12 14h.01"/><path d="M8 14h.01"/><path d="M12 18h.01"/><path d="M8 18h.01"/></svg></div>
            <div class="feature-icon-wrap"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect width="16" height="20" x="4" y="2" rx="2"/><line x1="8" x2="16" y1="6" y2="6"/><line x1="16" x2="16" y1="14" y2="18"/><path d="M16 10h.01"/><path d="M12 10h.01"/><path d="M8 10h.01"/><path d="M12 14h.01"/><path d="M8 14h.01"/><path d="M12 18h.01"/><path d="M8 18h.01"/></svg></div>
            <h3 class="mono">Math Expression Tools</h3>
            <p>Animate bones with complex math expressions by simply choosing from a library of presets.</p>
          </div>
          <div class="feature-card animate-in">
            <div class="bg-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect width="16" height="16" x="4" y="4" rx="2"/><rect width="6" height="6" x="9" y="9" rx="1"/><path d="M15 2v2"/><path d="M15 20v2"/><path d="M2 15h2"/><path d="M2 9h2"/><path d="M20 15h2"/><path d="M20 9h2"/><path d="M9 2v2"/><path d="M9 20v2"/></svg></div>
            <div class="feature-icon-wrap"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect width="16" height="16" x="4" y="4" rx="2"/><rect width="6" height="6" x="9" y="9" rx="1"/><path d="M15 2v2"/><path d="M15 20v2"/><path d="M2 15h2"/><path d="M2 9h2"/><path d="M20 15h2"/><path d="M20 9h2"/><path d="M9 2v2"/><path d="M9 20v2"/></svg></div>
            <h3 class="mono">Animation Presets</h3>
            <p>Library of starting animations. Drag and drop walk cycles, runs, and idles to kickstart your scene.</p>
          </div>
        </div>
      </details>
    </div>
  </section>

  <!-- ===== SHOWCASE ===== -->
  <section id="showcase">
    <div class="container">
      <div class="showcase-card">
        <div class="showcase-video" data-track="showcase_play" data-label="Nath's Bipedal Auto Rig Demo">
          <div class="play-circle">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polygon points="6 3 20 12 6 21 6 3"/></svg>
          </div>
          <div class="showcase-video-info">
            <h3>Nath's Bipedal Auto Rig Demo</h3>
            <p class="mono">Python &amp; Blender API Integration</p>
          </div>
        </div>
        <div class="showcase-steps">
          <h4>
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12.22 2h-.44a2 2 0 0 0-2 2v.18a2 2 0 0 1-1 1.73l-.43.25a2 2 0 0 1-2 0l-.15-.08a2 2 0 0 0-2.73.73l-.22.38a2 2 0 0 0 .73 2.73l.15.1a2 2 0 0 1 1 1.72v.51a2 2 0 0 1-1 1.74l-.15.09a2 2 0 0 0-.73 2.73l.22.38a2 2 0 0 0 2.73.73l.15-.08a2 2 0 0 1 2 0l.43.25a2 2 0 0 1 1 1.73V20a2 2 0 0 0 2 2h.44a2 2 0 0 0 2-2v-.18a2 2 0 0 1 1-1.73l.43-.25a2 2 0 0 1 2 0l.15.08a2 2 0 0 0 2.73-.73l.22-.39a2 2 0 0 0-.73-2.73l-.15-.08a2 2 0 0 1-1-1.74v-.5a2 2 0 0 1 1-1.74l.15-.09a2 2 0 0 0 .73-2.73l-.22-.38a2 2 0 0 0-2.73-.73l-.15.08a2 2 0 0 1-2 0l-.43-.25a2 2 0 0 1-1-1.73V4a2 2 0 0 0-2-2z"/><circle cx="12" cy="12" r="3"/></svg>
            Workflow
          </h4>
          <ol class="steps-list">
            <li class="step-item"><span class="step-num mono">1</span> Give character a name</li>
            <li class="step-item"><span class="step-num mono">2</span> Create position locators</li>
            <li class="step-item"><span class="step-num mono">3</span> Position the locators</li>
            <li class="step-item"><span class="step-num mono">4</span> Generate rig</li>
            <li class="step-item"><span class="step-num mono">5</span> Bind skin &amp; animate</li>
          </ol>
          <a href="#ecosystem" class="btn-outline-full" data-track="docs_click" data-label="Read documentation">Read Documentation</a>
        </div>
      </div>
    </div>
  </section>

  <!-- ===== ASSETS ===== -->
  <section id="assets" class="section">
    <div class="container">
      <div class="assets-grid">
        <div class="assets-info">
          <h2>Game Ready Assets</h2>
          <p>
            Pre-rigged, game-ready characters optimized for Unity and Unreal Engine.
            Fully compatible with the Grit framework.
          </p>
          <ul class="assets-list">
            <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 6 9 17l-5-5"/></svg> Low-poly optimized</li>
            <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 6 9 17l-5-5"/></svg> 4K PBR textures</li>
            <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 6 9 17l-5-5"/></svg> Full facial rig</li>
            <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 6 9 17l-5-5"/></svg> Root-motion compatible</li>
          </ul>
          <a href="#contact" class="btn-shop" data-track="assets_shop" data-label="Shop assets">Shop Assets Now</a>
        </div>

        <div class="assets-visual">
          <div class="assets-glow"></div>
          <div class="assets-frame">
            <div class="assets-thumb">
              <div class="assets-thumb-radial"></div>
              <span class="assets-label mono">ORC_WARRIOR_V2.FBX</span>
              <div class="assets-shape">
                <div class="bar"></div>
                <div class="arm-l"></div>
                <div class="arm-r"></div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- ===== CONTACT ===== -->
  <section id="contact">
    <div class="container">
      <div class="contact-wrap">
        <h2>Contact</h2>
        <div class="contact-divider"></div>

        <form class="contact-form" id="contact-form">
          <div class="form-row">
            <div class="form-group">
              <label for="contact-name">Name</label>
              <input type="text" id="contact-name" name="name" required>
            </div>
            <div class="form-group">
              <label for="contact-email">Email</label>
              <input type="email" id="contact-email" name="email" required>
            </div>
          </div>
          <div class="form-group">
            <label for="contact-subject">Subject</label>
            <input type="text" id="contact-subject" name="subject">
          </div>
          <div class="form-group">
            <label for="contact-message">Message</label>
            <textarea id="contact-message" name="message" rows="5" required></textarea>
          </div>
          <button type="submit" class="btn-submit">Submit Message</button>
          <p class="form-status" id="contact-status" role="status" aria-live="polite"></p>
        </form>
      </div>
    </div>
  </section>
  </main>

  <!-- ===== FOOTER ===== -->
  <footer>
    <div class="container">
      <div class="footer-grid">
        <div class="footer-brand">
          <div class="footer-brand-logo">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="var(--cyan-400)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16Z"/><path d="m3.3 7 8.7 5 8.7-5"/><path d="M12 22V12"/></svg>
            <span>3D <em>GRIT</em></span>
          </div>
          <p>Professional auto-rigging and pipeline tools for independent creators and studios. Built for Blender artists, by Blender artists.</p>
        </div>

        <div class="footer-col">
          <h4>Tools</h4>
          <ul>
            <li><a href="#ecosystem">Auto-Rigging Framework</a></li>
            <li><a href="#ecosystem">MayaForBlender</a></li>
            <li><a href="#ecosystem">Retopology</a></li>
          </ul>
        </div>

        <div class="footer-col">
          <h4>Resources</h4>
          <ul>
            <li><a href="#features">Features</a></li>
            <li><a href="#showcase">Showcase</a></li>
            <li><a href="#contact">Contact</a></li>
          </ul>
        </div>
      </div>

      <div class="footer-bottom">
        <p>© 2026 3D GRIT — a PixelStortion studio. All rights reserved.</p>
        <p>Tools with weight.</p>
      </div>
    </div>
  </footer>

  <!-- ===== SOFT-GATE MODAL ===== -->
  <div class="modal-overlay" id="capture-modal" aria-hidden="true" role="dialog" aria-modal="true" aria-labelledby="capture-modal-title">
    <div class="modal-content">
      <button class="modal-close" id="modal-close-btn" aria-label="Close">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>
      </button>

      <div class="modal-header">
        <h3 class="mono" id="capture-modal-title">Access Unlocked</h3>
        <p>Enter your email to receive the download link and join the priority waitlist for Pro updates.</p>
      </div>

      <form class="modal-form" id="capture-form">
        <div class="form-group">
          <input type="email" id="capture-email" placeholder="artist@studio.com" required>
        </div>
        <button type="submit" class="btn-submit">Send Download Link</button>
      </form>

      <div class="modal-success" id="modal-success-state" style="display:none;">
        <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="var(--cyan-400)" stroke-width="2" aria-hidden="true"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg>
        <h4>Link Sent!</h4>
        <p>Check your inbox. Your download is ready.</p>
      </div>
    </div>
  </div>

  <!-- ===== SCRIPTS ===== -->
  <script src="/assets/js/track.js" defer></script>
  <script src="/assets/js/site.js" defer></script>
</body>
</html>
Home page done. Now the indexability files and the upgraded worker.

Update Todos

Check reference for domain/canonical hints

Create content registry + site config (content/site.json, content/registry.json)

Write shared grounded-grit stylesheet (assets/css/grit.css)

Write tracking + site-behavior JS (assets/js/track.js, site.js)

Build the grounded-grit Home page (index.html) with full SEO head + JSON-LD + data-track

Add indexability files (robots.txt, sitemap.xml seeded with Home)

Upgrade the analytics/forms worker (worker.js)
Write C:\PixelStortionGit\3DGRIT_NEW\robots.txt
5 lines
User-agent: *
Allow: /

Sitemap: https://3dgrit.com/sitemap.xml
Write C:\PixelStortionGit\3DGRIT_NEW\sitemap.xml
11 lines
<?xml version="1.0" encoding="UTF-8"?>
<!-- Generated from content/registry.json — only status:published items with a live page are listed. URLs are extensionless (Cloudflare 308-strips .html). -->
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://3dgrit.com/</loc>
    <lastmod>2026-05-29</lastmod>
    <changefreq>weekly</changefreq>
    <priority>1.0</priority>
  </url>
</urlset>
Write C:\PixelStortionGit\3DGRIT_NEW\worker.js
92 lines
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
All files are written. Let me add an inline SVG favicon (avoids a 404 and adds polish), then verify the full tree.

Edit C:\PixelStortionGit\3DGRIT_NEW\index.html
Added 1 line
Update Todos

Check reference for domain/canonical hints

Create content registry + site config (content/site.json, content/registry.json)

Write shared grounded-grit stylesheet (assets/css/grit.css)

Write tracking + site-behavior JS (assets/js/track.js, site.js)

Build the grounded-grit Home page (index.html) with full SEO head + JSON-LD + data-track

Add indexability files (robots.txt, sitemap.xml seeded with Home)

Upgrade the analytics/forms worker (worker.js)
Let me verify the tree and that both JSON files parse cleanly.

Globpattern: "3DGRIT_NEW/**/*"
Found 16 files
PowerShell
IN
{
  "command": "\"site.json\",\"registry.json\" | ForEach-Object { try { Get-Content \"C:\\PixelStortionGit\\3DGRIT_NEW\\content\\$_\" -Raw | ConvertFrom-Json | Out-Null; \"$_ OK\" } catch { \"$_ FAILED: $($_.Exception.Message)\" } }; try { [xml](Get-Content \"C:\\PixelStortionGit\\3DGRIT_NEW\\sitemap.xml\" -Raw) | Out-Null; \"sitemap.xml OK\" } catch { \"sitemap.xml FAILED\" }",
  "description": "Validate JSON config files and sitemap XML parse"
}
OUT
site.json OK
registry.json OK
sitemap.xml OK
Tree is complete and all data files parse. One correctness check before I report: CSS var() does not work inside SVG presentation attributes (a latent bug carried from the reference), so any stroke="var(--cyan-400)" renders black/invisible on the dark bg. Let me find them.

Grep "(stroke|fill)="var\(" (in C:\PixelStortionGit\3DGRIT_NEW\index.html)
3 lines of output
All three are brand marks (nav logo, footer logo, modal checkmark). Replacing the var() with the literal cyan hex so they actually render.

Edit C:\PixelStortionGit\3DGRIT_NEW\index.html
Modified
Fixed. Phase 1 is scaffolded and validated. Here's what now lives in 3DGRIT_NEW/:


3DGRIT_NEW/
├── index.html              Home page (grounded grit) — first consumer of the foundation
├── robots.txt              allow-all + sitemap pointer
├── sitemap.xml             seeded with "/" (only published, live pages)
├── worker.js               edge worker: /api/track + form intents, KV-ready
├── content/
│   ├── site.json           global config: brand, baseUrl, nav, footer
│   └── registry.json       the content spine — Home + 6 tools + 4 blog posts registered
└── assets/
    ├── css/grit.css        shared grounded-grit stylesheet
    └── js/
        ├── track.js        trackable layer (one event schema, ties events to registry ids)
        └── site.js         nav, mobile menu, scroll-reveal, soft-gate modal, contact form
How the groundwork holds together

Registry-driven: every item (Home, tools, blog) is registered once in registry.json with status + extensionless canonicalPath. The schema already includes the hub-item shape (source, creatorCredit, toolsUsed, whyInteresting, curationScore) so sitt-geo-engine output drops in later — not wired now.
Indexable: crawlable HTML, per-page meta + OG/Twitter, JSON-LD (Organization + WebSite), extensionless canonical, robots + sitemap. Sitemap lists only Home because only Home is live — that's the honesty rule (pages flip into the sitemap as they're published).
Trackable: track.js wires every [data-track] CTA, stamps each event with the registry data-item id, and posts to the worker via sendBeacon. Every ecosystem CTA is already tagged.
Fixed a latent bug from the reference: the brand-mark SVGs used stroke="var(--cyan-400)", which is invalid in SVG attributes (CSS vars only work in CSS) — they'd have rendered black on the dark bg. Switched to the literal hex.

Flags before you treat this as final:

Domain is provisional — I used https://3dgrit.com for canonical/OG/robots/sitemap. Confirm the real domain. Heads-up: since the site is buildless, that string is currently hardcoded in 4 files (index.html, robots.txt, sitemap.xml, site.json). The next-phase generator will template it to one place.
og:image points to /assets/img/og-default.png, which doesn't exist yet — drop a 1200×630 share image there.
Worker must be routed at /api/* on the domain; bind a KV namespace GRIT_EVENTS for persistence, else it just logs.
Video placeholders (flagship card + showcase) carry over from the reference — no .mp4/embed yet.
I have not visually verified in a browser (no browser here). To preview: serve from the 3DGRIT_NEW root — py -m http.server 8080 — then open http://localhost:8080/ (the absolute /assets/... paths need a server, not file://).
Natural next phase: the tool pages + the Markdown-post generator/template (that's what proves the "indexable + good-looking + easy to create" trio end-to-end and migrates the 4 blog posts). Want me to preview-serve it first, or move to the generator?