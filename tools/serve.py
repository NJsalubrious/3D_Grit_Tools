#!/usr/bin/env python3
"""
3D GRIT local preview server.

Plain `python -m http.server` can't resolve the site's extensionless URLs
(e.g. /blog/bipedal-rig-foundations), but Cloudflare Pages does (it 308-strips
.html). This dev server mirrors that: a bare path with no file falls back to
<path>.html, so local preview matches production link behavior exactly.

Usage:  python tools/serve.py [port]   (default 8080)
Then open http://127.0.0.1:8080/
"""

import os
import sys
import http.server
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8080


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *a, **k):
        super().__init__(*a, directory=str(ROOT), **k)

    def translate_path(self, path):
        p = super().translate_path(path)
        if os.path.isdir(p) or os.path.exists(p):
            return p
        if os.path.isfile(p + ".html"):       # extensionless -> .html (like Cloudflare)
            return p + ".html"
        return p

    def end_headers(self):
        self.send_header("Cache-Control", "no-store")  # always serve fresh during dev
        super().end_headers()


if __name__ == "__main__":
    os.chdir(ROOT)
    with http.server.ThreadingHTTPServer(("127.0.0.1", PORT), Handler) as httpd:
        print(f"3D GRIT preview -> http://127.0.0.1:{PORT}/  (Ctrl+C to stop)")
        httpd.serve_forever()
