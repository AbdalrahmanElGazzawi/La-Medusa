# La Medusa static site builder — run: python3 build.py
# Emits plain HTML into the repo root (parent of builder/). No runtime dependencies.
import os
from common import page, DOMAIN
import pages_en
import pages_ar

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def write(path, content):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(content)
    print("wrote", path)

def build():
    for slug, meta in pages_en.PAGES.items():
        html = page(slug, "en", meta["title"], meta["desc"], meta["body"], meta.get("jsonld", ""))
        write(os.path.join(slug, "index.html") if slug else "index.html", html)
    for slug, meta in pages_ar.PAGES.items():
        html = page(slug, "ar", meta["title"], meta["desc"], meta["body"], meta.get("jsonld", ""))
        write(os.path.join("ar", slug, "index.html") if slug else "ar/index.html", html)

    slugs = list(pages_en.PAGES.keys())
    urls = ""
    for s in slugs:
        urls += f"<url><loc>{DOMAIN}/{s}</loc><xhtml:link rel=\"alternate\" hreflang=\"ar\" href=\"{DOMAIN}/ar/{s}\"/><xhtml:link rel=\"alternate\" hreflang=\"en\" href=\"{DOMAIN}/{s}\"/></url>\n"
        urls += f"<url><loc>{DOMAIN}/ar/{s}</loc><xhtml:link rel=\"alternate\" hreflang=\"en\" href=\"{DOMAIN}/{s}\"/><xhtml:link rel=\"alternate\" hreflang=\"ar\" href=\"{DOMAIN}/ar/{s}\"/></url>\n"
    sitemap = f'''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">
{urls}</urlset>'''
    write("sitemap.xml", sitemap)
    write("robots.txt", f"User-agent: *\nAllow: /\nSitemap: {DOMAIN}/sitemap.xml\n")

if __name__ == "__main__":
    build()
    print("done")
