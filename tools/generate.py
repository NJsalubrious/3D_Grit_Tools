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

ROOT = Path(__file__).resolve().parent.parent
CONTENT = ROOT / "content"
POSTS_DIR = CONTENT / "posts"
TPL_DIR = ROOT / "templates"

POST_TYPES = {"blog", "article", "showreel"}
KICKER = {"blog": "Breakdown", "article": "Guide", "showreel": "Reel"}


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
            f'<h3>{text(it["title"])}</h3>'
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
    })
    write(ROOT / "blog" / "index.html", listing)
    print(f"  list   /blog  ->  blog/index.html  ({len(published_posts)} posts)")

    # ---- sitemap ----
    today = datetime.date.today().isoformat()
    urls = [(base + "/", today, "weekly", "1.0"),
            (blog_canonical, today, "weekly", "0.7")]
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
    print(f"\nDone. {len(published_posts)} post(s) generated.")


if __name__ == "__main__":
    main()
