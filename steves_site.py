"""McGrath Translations site.

Flask is used for templating and local preview only. `python freeze.py`
renders every page to plain HTML in build/, which is what gets deployed
(see .github/workflows/deploy.yml).

Local preview:  python steves_site.py   ->  http://localhost:5000
"""
import datetime
import os

from flask import Flask, render_template

app = Flask(__name__)

# Public address of the site, used for canonical / social-preview URLs.
SITE_URL = os.environ.get("SITE_URL", "https://www.mcgrathtranslations.com").rstrip("/")


@app.context_processor
def site_globals():
    return {"year": datetime.date.today().year, "site_url": SITE_URL}


@app.route('/')
def homepage():
    return render_template('homepage.html', Title='Home')


@app.route('/about')
def about():
    return render_template('about.html', Title='О переводчике')


@app.route('/background')
def background():
    return render_template('background.html', Title='Background')


@app.route('/contact')
def contact():
    return render_template('contact.html', Title='Contact')


@app.route('/sample')
def sample():
    return render_template('sample.html', Title='Writing Sample')


@app.route('/Services')
def services():
    return render_template('Services.html', Title='Services')


@app.route('/Books')
def books():
    return render_template('Books.html', Title='Books')


@app.errorhandler(404)
def not_found(_):
    return render_template('404.html', Title='Page not found'), 404


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='127.0.0.1', port=port)
