#!/usr/bin/env python3
"""
3D GRIT static site generator (zero-dependency, Python 3.9+).

Reads content/site.json + content/registry.json, renders every published
Markdown post (content/posts/<slug>.md) through templates/post.html, rebuilds
the /blog listing, and regenerates sitemap.xml. The served site stays static;
this only runs when content changes.

To add a post:
  1. Add an entry to content/registry.json (type: blog|article|showreel,
     status: "published", an extensionless canonicalPath, title, description...).
  2. Drop content/posts/<slug>.md with the body (Markdown).
  3. Run:  python tools/generate.py

Only status == "published" posts with a matching .md are emitted and listed.
Canonicals/links stay extensionless (Cloudflare 308-strips .html).
"""

import json
import re
import html
import datetime
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parent.parent
CONTENT = ROOT / "content"
POSTS_DIR = CONTENT / "posts"
TPL_DIR = ROOT / "templates"

POST_TYPES = {"blog", "article", "showreel"}
KICKER = {"blog": "Breakdown", "article": "Guide", "showreel": "Reel"}

# R2 public bucket that serves the demo videos (matches assets/js/site.js).
VIDEO_BASE = "https://pub-e32d0586a45344c98cee1a56fa11418b.r2.dev/"


def tool_name(item):
    """Short display name from the SEO title: 'Retopology: Quad-Draw | 3D GRIT' -> 'Retopology'."""
    t = item["title"].split(" | ")[0]
    return t.split(":")[0].strip() if ":" in t else t.strip()


def tool_jsonld(item, canonical, default_img, base, name):
    tier = item.get("tier", "free")
    available = item.get("availability", "available") == "available"
    app = {
        "@type": "SoftwareApplication",
        "name": name,
        "applicationCategory": "DesignApplication",
        "operatingSystem": "Windows, macOS, Linux",
        "description": item["description"],
        "url": canonical,
        "image": default_img,
        "offers": {
            "@type": "Offer",
            "price": "0" if tier == "free" else "0",
            "priceCurrency": "USD",
            "availability": "https://schema.org/InStock" if available else "https://schema.org/PreOrder",
            "url": canonical,
        },
        "publisher": {"@type": "Organization", "name": "3D GRIT", "url": base + "/"},
    }
    breadcrumb = {
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": base + "/"},
            {"@type": "ListItem", "position": 2, "name": "Tools", "item": base + "/#ecosystem"},
            {"@type": "ListItem", "position": 3, "name": name, "item": canonical},
        ],
    }
    graph = [app, breadcrumb]
    if item.get("video"):
        graph.append({
            "@type": "VideoObject",
            "name": name + " demo",
            "description": item["description"],
            "thumbnailUrl": default_img,
            "uploadDate": item.get("date"),
            "contentUrl": VIDEO_BASE + quote(item["video"]),
        })
    return {"@context": "https://schema.org", "@graph": graph}


# Brand-glyph SVG paths (viewBox 0 0 24 24, fill=currentColor). Order = display order.
SOCIAL_ICONS = {
    "instagram": ("Instagram", "M12 0C8.74 0 8.333.015 7.053.072 5.775.132 4.905.333 4.14.63c-.789.306-1.459.717-2.126 1.384S.935 3.35.63 4.14C.333 4.905.131 5.775.072 7.053.012 8.333 0 8.74 0 12s.015 3.667.072 4.947c.06 1.277.261 2.148.558 2.913.306.788.717 1.459 1.384 2.126.667.666 1.336 1.079 2.126 1.384.766.296 1.636.499 2.913.558C8.333 23.988 8.74 24 12 24s3.667-.015 4.947-.072c1.277-.06 2.148-.262 2.913-.558.788-.306 1.459-.718 2.126-1.384.666-.667 1.079-1.335 1.384-2.126.296-.765.499-1.636.558-2.913.06-1.28.072-1.687.072-4.947s-.015-3.667-.072-4.947c-.06-1.277-.262-2.149-.558-2.913-.306-.789-.718-1.459-1.384-2.126C21.319 1.347 20.651.935 19.86.63c-.765-.297-1.636-.499-2.913-.558C15.667.012 15.26 0 12 0Zm0 2.16c3.203 0 3.585.016 4.85.071 1.17.055 1.805.249 2.227.415.562.217.96.477 1.382.896.419.42.679.819.896 1.381.164.422.36 1.057.413 2.227.057 1.266.07 1.646.07 4.85s-.015 3.585-.074 4.85c-.061 1.17-.256 1.805-.421 2.227-.224.562-.479.96-.899 1.382-.419.419-.824.679-1.38.896-.42.164-1.065.36-2.235.413-1.274.057-1.649.07-4.859.07-3.211 0-3.586-.015-4.859-.074-1.171-.061-1.816-.256-2.236-.421-.569-.224-.96-.479-1.379-.899-.421-.419-.69-.824-.9-1.38-.165-.42-.359-1.065-.42-2.235-.045-1.26-.061-1.649-.061-4.844 0-3.196.016-3.586.061-4.861.061-1.17.255-1.814.42-2.234.21-.57.479-.96.9-1.381.419-.419.81-.689 1.379-.898.42-.166 1.051-.361 2.221-.421 1.275-.045 1.65-.06 4.859-.06l.045.03Zm0 3.678c-3.405 0-6.162 2.76-6.162 6.162 0 3.405 2.76 6.162 6.162 6.162 3.405 0 6.162-2.76 6.162-6.162 0-3.405-2.76-6.162-6.162-6.162ZM12 16c-2.21 0-4-1.79-4-4s1.79-4 4-4 4 1.79 4 4-1.79 4-4 4Zm7.846-10.405c0 .795-.646 1.44-1.44 1.44-.795 0-1.44-.646-1.44-1.44 0-.794.646-1.439 1.44-1.439.793-.001 1.44.645 1.44 1.439Z"),
    "x": ("X", "M18.901 1.153h3.68l-8.04 9.19L24 22.846h-7.406l-5.8-7.584-6.638 7.584H.474l8.6-9.83L0 1.154h7.594l5.243 6.932ZM17.61 20.644h2.039L6.486 3.24H4.298Z"),
    "youtube": ("YouTube", "M23.498 6.186a3.016 3.016 0 0 0-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 0 0 .502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 0 0 2.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 0 0 2.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.545 15.568V8.432L15.818 12l-6.273 3.568z"),
    "facebook": ("Facebook", "M9.101 23.691v-7.98H6.627v-3.667h2.474v-1.58c0-4.085 1.848-5.978 5.858-5.978.401 0 .955.042 1.468.103a8.68 8.68 0 0 1 1.141.195v3.325a8.623 8.623 0 0 0-.653-.036 26.805 26.805 0 0 0-.733-.009c-.707 0-1.259.096-1.675.309a1.686 1.686 0 0 0-.679.622c-.258.42-.374.995-.374 1.752v1.297h3.919l-.386 2.103-.287 1.564h-3.246v8.245C19.396 23.238 24 18.179 24 12.044c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.628 3.874 10.35 9.101 11.647Z"),
}


def social_html(site):
    soc = site.get("social", {})
    out = []
    for key in ("instagram", "x", "youtube", "facebook"):
        url = soc.get(key)
        if not url:
            continue
        label, path = SOCIAL_ICONS[key]
        out.append(
            f'<a href="{attr(url)}" target="_blank" rel="noopener" '
            f'aria-label="3D GRIT on {label}" data-track="social_click" data-label="{key}">'
            f'<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="{path}"/></svg></a>'
        )
    return '<div class="social-row">' + "".join(out) + "</div>" if out else ""


# ---------------------------------------------------------------- helpers
def attr(s):
    """Escape for an HTML attribute value."""
    return html.escape(str(s), quote=True)


def text(s):
    """Escape for HTML text content."""
    return html.escape(str(s), quote=False)


def human_date(d):
    try:
        dt = datetime.date.fromisoformat(d)
        return f"{dt.strftime('%B')} {dt.day}, {dt.year}"
    except Exception:
        return d


# ---------------------------------------------------------------- markdown
def _inline(s):
    codes = []

    def stash(m):
        codes.append(m.group(1))
        return f"\x00{len(codes) - 1}\x00"

    s = re.sub(r"`([^`]+)`", stash, s)          # pull code spans out first
    s = html.escape(s, quote=False)             # escape &, <, >
    s = re.sub(r"!\[([^\]]*)\]\(([^)\s]+)\)",
               lambda m: f'<img src="{m.group(2)}" alt="{m.group(1)}" loading="lazy">', s)
    s = re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)",
               lambda m: f'<a href="{m.group(2)}">{m.group(1)}</a>', s)
    s = re.sub(r"\*\*(.+?)\*\*", "\x01\\1\x02", s)
    s = re.sub(r"\*(.+?)\*", r"<em>\1</em>", s)
    s = s.replace("\x01", "<strong>").replace("\x02", "</strong>")
    s = re.sub(r"\x00(\d+)\x00",
               lambda m: f"<code>{html.escape(codes[int(m.group(1))])}</code>", s)
    return s


def render_markdown(md):
    lines = md.replace("\r\n", "\n").split("\n")
    out, i, n = [], 0, len(md.replace("\r\n", "\n").split("\n"))
    block_start = r"^(#{1,6}\s|\s*[-*]\s|\s*\d+\.\s|>|```)"
    while i < n:
        line = lines[i]
        if not line.strip():
            i += 1
            continue
        if line.strip().startswith("```"):
            i += 1
            code = []
            while i < n and not lines[i].strip().startswith("```"):
                code.append(lines[i])
                i += 1
            i += 1
            out.append("<pre><code>" + html.escape("\n".join(code)) + "</code></pre>")
            continue
        m = re.match(r"(#{1,6})\s+(.*)", line)
        if m:
            lv = len(m.group(1))
            out.append(f"<h{lv}>{_inline(m.group(2).strip())}</h{lv}>")
            i += 1
            continue
        if re.match(r"^(---+|\*\*\*+)$", line.strip()):
            out.append("<hr>")
            i += 1
            continue
        if line.lstrip().startswith(">"):
            quote = []
            while i < n and lines[i].lstrip().startswith(">"):
                quote.append(re.sub(r"^\s*>\s?", "", lines[i]))
                i += 1
            out.append("<blockquote>" + _inline(" ".join(quote)) + "</blockquote>")
            continue
        if re.match(r"^\s*[-*]\s+", line):
            items = []
            while i < n and re.match(r"^\s*[-*]\s+", lines[i]):
                items.append(re.sub(r"^\s*[-*]\s+", "", lines[i]))
                i += 1
            out.append("<ul>" + "".join(f"<li>{_inline(x)}</li>" for x in items) + "</ul>")
            continue
        if re.match(r"^\s*\d+\.\s+", line):
            items = []
            while i < n and re.match(r"^\s*\d+\.\s+", lines[i]):
                items.append(re.sub(r"^\s*\d+\.\s+", "", lines[i]))
                i += 1
            out.append("<ol>" + "".join(f"<li>{_inline(x)}</li>" for x in items) + "</ol>")
            continue
        para = []
        while (i < n and lines[i].strip()
               and not re.match(block_start, lines[i])
               and not re.match(r"^(---+|\*\*\*+)$", lines[i].strip())):
            para.append(lines[i].strip())
            i += 1
        out.append("<p>" + _inline(" ".join(para)) + "</p>")
    return "\n".join(out)


# ---------------------------------------------------------------- rendering
def fill(template, mapping):
    for k, v in mapping.items():
        template = template.replace("{{" + k + "}}", v)
    return template


def jsonld_block(obj):
    s = json.dumps(obj, ensure_ascii=False, separators=(",", ":"))
    return s.replace("<", "\\u003c")  # never let a "</script>" escape the tag


def article_jsonld(item, canonical, default_img):
    node = {
        "@type": "BlogPosting" if item["type"] == "blog" else "Article",
        "headline": item["title"],
        "description": item["description"],
        "datePublished": item.get("date"),
        "url": canonical,
        "mainEntityOfPage": canonical,
        "image": item.get("thumbnail") or default_img,
        "author": {"@type": "Organization", "name": "3D GRIT"},
        "publisher": {"@type": "Organization", "name": "3D GRIT"},
    }
    if item.get("video"):
        video = {
            "@type": "VideoObject",
            "name": item["title"],
            "description": item["description"],
            "thumbnailUrl": item.get("thumbnail") or default_img,
            "uploadDate": item.get("date"),
            "embedUrl": item["video"],
        }
        return {"@context": "https://schema.org", "@graph": [node, video]}
    node["@context"] = "https://schema.org"
    return node


def write(path, content):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def main():
    site = json.loads((CONTENT / "site.json").read_text(encoding="utf-8"))
    registry = json.loads((CONTENT / "registry.json").read_text(encoding="utf-8"))
    base = site["baseUrl"].rstrip("/")
    default_img = base + site["brand"].get("ogImage", "/assets/img/og-default.png")
    post_tpl = (TPL_DIR / "post.html").read_text(encoding="utf-8")
    list_tpl = (TPL_DIR / "blog_index.html").read_text(encoding="utf-8")
    tool_tpl = (TPL_DIR / "tool.html").read_text(encoding="utf-8")
    social = social_html(site)

    # ---- homepage gate: coming-soon splash vs the live full site ----
    mode = (site.get("mode") or "coming-soon").strip().lower()
    home_src = "coming-soon.html" if mode == "coming-soon" else "preview.html"
    src_path = ROOT / home_src
    if src_path.exists():
        write(ROOT / "index.html", src_path.read_text(encoding="utf-8"))
        print(f"  home   mode={mode}  ->  index.html (from {home_src})")
    else:
        print(f"  home   WARNING: source '{home_src}' not found; index.html left as-is")

    items = registry["items"]
    published_posts = []
    skipped = []

    for item in items:
        if item.get("type") not in POST_TYPES:
            continue
        md_path = POSTS_DIR / (item["slug"] + ".md")
        if item.get("status") != "published":
            if md_path.exists():
                skipped.append((item["slug"], "status=" + str(item.get("status"))))
            continue
        if not md_path.exists():
            skipped.append((item["slug"], "missing .md"))
            continue

        canonical = base + item["canonicalPath"]
        body = render_markdown(md_path.read_text(encoding="utf-8"))
        video_html = ""
        if item.get("video"):
            video_html = (
                f'<div class="post-video"><iframe src="{attr(item["video"])}" '
                f'title="{attr(item["title"])}" loading="lazy" '
                f'allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" '
                f'allowfullscreen></iframe></div>'
            )
        tags_html = "".join(f'<span class="post-tag">{text(t)}</span>' for t in item.get("tags", []))
        og_image = item.get("thumbnail") or default_img

        page = fill(post_tpl, {
            "TITLE": attr(item["title"] + " | 3D GRIT"),
            "OG_TITLE": attr(item["title"]),
            "DESCRIPTION": attr(item["description"]),
            "CANONICAL": attr(canonical),
            "OG_IMAGE": attr(og_image),
            "JSONLD": jsonld_block(article_jsonld(item, canonical, default_img)),
            "PAGE_ID": attr(item["id"]),
            "KICKER": text(KICKER.get(item["type"], "Post")),
            "HEADING": text(item["title"]),
            "SUBTITLE": text(item.get("subtitle") or item["description"]),
            "DATE": attr(item.get("date", "")),
            "DATE_HUMAN": text(human_date(item.get("date", ""))),
            "TAGS": tags_html,
            "VIDEO": video_html,
            "BODY": body,
            "BACK_HREF": "/blog",
            "BACK_LABEL": "All breakdowns",
            "SOCIAL": social,
        })
        out_path = ROOT / (item["canonicalPath"].strip("/") + ".html")
        write(out_path, page)
        published_posts.append(item)
        print(f"  post   {item['canonicalPath']}  ->  {out_path.relative_to(ROOT)}")

    # ---- blog listing ----
    published_posts.sort(key=lambda x: x.get("date", ""), reverse=True)
    cards = []
    for it in published_posts:
        thumb = it.get("thumbnail", "")
        cards.append(
            f'<a class="blog-card" href="{attr(it["canonicalPath"])}" '
            f'data-track="blog_card" data-item="{attr(it["id"])}">'
            f'<div class="blog-card-thumb" style="background-image:url(\'{attr(thumb)}\')"></div>'
            f'<div class="blog-card-body"><span class="date">{text(human_date(it.get("date","")))}</span>'
            f'<h2>{text(it["title"])}</h2>'
            f'<p>{text(it.get("excerpt") or it["description"])}</p></div></a>'
        )
    blog_canonical = base + "/blog"
    listing = fill(list_tpl, {
        "TITLE": attr("Breakdowns | 3D GRIT Blog"),
        "DESCRIPTION": attr("Rigging, pipeline, and 3D-meets-AI breakdowns from the 3D GRIT team."),
        "CANONICAL": attr(blog_canonical),
        "OG_IMAGE": attr(default_img),
        "JSONLD": jsonld_block({
            "@context": "https://schema.org", "@type": "Blog",
            "url": blog_canonical, "name": "3D GRIT Blog",
        }),
        "CARDS": "\n        ".join(cards) if cards else "<p style='color:var(--ink-dim)'>No posts yet.</p>",
        "SOCIAL": social,
    })
    write(ROOT / "blog" / "index.html", listing)
    print(f"  list   /blog  ->  blog/index.html  ({len(published_posts)} posts)")

    # ---- tool pages (the indexable "money pages") ----
    published_tools = []
    for item in items:
        if item.get("type") != "tool":
            continue
        if item.get("status") != "published":
            skipped.append((item["slug"], "tool status=" + str(item.get("status"))))
            continue
        canonical = base + item["canonicalPath"]
        name = tool_name(item)
        tier = item.get("tier", "free")
        available = item.get("availability", "available") == "available"

        if available:
            badge, badge_class = ("Free", "badge-free") if tier == "free" else ("Available", "badge-pro")
        else:
            badge, badge_class = ("Coming Soon", "badge-pro")

        video_html = ""
        if item.get("video"):
            vurl = VIDEO_BASE + quote(item["video"])
            video_html = (
                f'<div class="post-video"><video src="{attr(vurl)}" controls playsinline '
                f'preload="none" poster="{attr(default_img)}"></video></div>'
            )

        if tier == "free" and available:
            cta = (f'<a href="/#ecosystem" class="btn-primary" data-track="download_free" '
                   f'data-tool="{attr(item["id"])}" data-item="{attr(item["id"])}">Get Started Free</a>')
        else:
            cta = (f'<a href="/#ecosystem" class="btn-primary" data-track="waitlist_click" '
                   f'data-tool="{attr(item["id"])}" data-item="{attr(item["id"])}">Join the Waitlist</a>')

        tags_html = "".join(f'<span class="post-tag">{text(t)}</span>' for t in item.get("tags", []))

        page = fill(tool_tpl, {
            "TITLE": attr(item["title"]),
            "OG_TITLE": attr(name),
            "DESCRIPTION": attr(item["description"]),
            "CANONICAL": attr(canonical),
            "OG_IMAGE": attr(default_img),
            "JSONLD": jsonld_block(tool_jsonld(item, canonical, default_img, base, name)),
            "PAGE_ID": attr(item["id"]),
            "HEADING": text(name),
            "BADGE": text(badge),
            "BADGE_CLASS": attr(badge_class),
            "TAGS": tags_html,
            "VIDEO": video_html,
            "BODY": f"<p>{text(item['description'])}</p>",
            "CTA": cta,
            "SOCIAL": social,
        })
        out_path = ROOT / (item["canonicalPath"].strip("/") + ".html")
        write(out_path, page)
        published_tools.append(item)
        print(f"  tool   {item['canonicalPath']}  ->  {out_path.relative_to(ROOT)}")

    # ---- sitemap ----
    today = datetime.date.today().isoformat()
    urls = [(base + "/", today, "weekly", "1.0")]
    for it in published_tools:
        urls.append((base + it["canonicalPath"], it.get("date", today), "monthly", "0.8"))
    urls.append((blog_canonical, today, "weekly", "0.7"))
    for it in published_posts:
        urls.append((base + it["canonicalPath"], it.get("date", today), "monthly", "0.6"))
    rows = "\n".join(
        f"  <url>\n    <loc>{u}</loc>\n    <lastmod>{lm}</lastmod>\n"
        f"    <changefreq>{cf}</changefreq>\n    <priority>{pr}</priority>\n  </url>"
        for (u, lm, cf, pr) in urls
    )
    sitemap = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        "<!-- Generated by tools/generate.py from content/registry.json. "
        "URLs are extensionless (Cloudflare 308-strips .html). Do not edit by hand. -->\n"
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        f"{rows}\n</urlset>\n"
    )
    write(ROOT / "sitemap.xml", sitemap)
    print(f"  sitemap  {len(urls)} urls  ->  sitemap.xml")

    if skipped:
        print("\nskipped:")
        for slug, why in skipped:
            print(f"  - {slug}: {why}")
    print(f"\nDone. {len(published_tools)} tool page(s), {len(published_posts)} post(s) generated.")


if __name__ == "__main__":
    main()
