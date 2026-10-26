# McGrath Translations

Website for Steven McGrath, ATA-certified Russian to English translator.

The pages are Jinja templates rendered by a small Flask app, then "frozen" to
plain HTML so the site can be hosted for free on any static host.

## Edit and preview

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python steves_site.py            # http://localhost:5000, reloads on save
```

| What                     | Where                                   |
| ------------------------ | --------------------------------------- |
| Page text                | `templates/*.html`                      |
| Sidebar, menu, `<head>`  | `templates/base.html`                   |
| Site styles              | `static/css/site.css`                   |
| Theme (Bootstrap)        | `static/css/styles.css` — avoid editing |
| Images                   | `static/images/`                        |

Each page can set its own `{% block title %}` and `{% block description %}`
(used by search engines and link previews).

## Build

```bash
python freeze.py                 # writes the static site to build/
python -m http.server -d build   # optional: check the built output
```

## Deploy

Pushing to `master` runs `.github/workflows/deploy.yml`, which builds the site
and publishes it to GitHub Pages.

One-time setup:

1. On GitHub: **Settings → Pages → Source: GitHub Actions**.
2. Custom domain: add a `CNAME` file in the repo root containing the domain
   (e.g. `www.mcgrathtranslations.com`), set the same domain under
   **Settings → Pages**, and point the domain's DNS at GitHub Pages.

The `build/` folder also works as-is on Netlify or Cloudflare Pages
(build command `pip install -r requirements.txt && python freeze.py`,
output directory `build`).
