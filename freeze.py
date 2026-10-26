"""Render the Flask site to plain static files in build/.

    python freeze.py

Each route becomes <route>/index.html (so /about keeps working on any static
host), static/ is copied as-is, and 404.html is written for hosts that use it
(GitHub Pages, Netlify, Cloudflare Pages).
"""
import pathlib
import shutil

from steves_site import app

ROOT = pathlib.Path(__file__).parent
BUILD = ROOT / "build"


def page_routes():
    for rule in app.url_map.iter_rules():
        if "GET" in rule.methods and not rule.arguments and rule.endpoint != "static":
            yield rule.rule


def main():
    if BUILD.exists():
        shutil.rmtree(BUILD)
    BUILD.mkdir()

    client = app.test_client()
    for route in sorted(page_routes()):
        resp = client.get(route)
        if resp.status_code != 200:
            raise SystemExit(f"{route} returned {resp.status_code}")
        out = BUILD / route.lstrip("/") / "index.html"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_bytes(resp.data)
        print(f"  {route:<12} -> {out.relative_to(ROOT)}")

    resp = client.get("/__missing__")
    (BUILD / "404.html").write_bytes(resp.data)

    shutil.copytree(ROOT / "static", BUILD / "static")
    # Browsers request /favicon.ico from the site root.
    shutil.copy(ROOT / "static" / "images" / "favicon.ico", BUILD / "favicon.ico")
    # Tell GitHub Pages not to run Jekyll over the output.
    (BUILD / ".nojekyll").touch()

    cname = ROOT / "CNAME"
    if cname.exists():
        shutil.copy(cname, BUILD / "CNAME")

    print(f"Built {BUILD}")


if __name__ == "__main__":
    main()
