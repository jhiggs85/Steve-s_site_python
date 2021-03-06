import os
from flask import Flask, render_template
from flask_talisman import Talisman
app = Flask(__name__)
csp = {
    'default-src': [
        '\'self\'',
        'https://*',
        '*.w3.org',
        '\'unsafe-inline\'',
            ],
        'img-src': '*',
        'style-src': [
            '\'self\'',
            'https://*',
            '\'unsafe-inline\'',
    ],
    'script-src': [
        '\'self\'',
        'https://*',
        '\'unsafe-inline\'',
    ],
}
Talisman(app, content_security_policy=csp, content_security_policy_nonce_in=['script-src', 'style-src'])


@app.route('/')
def homepage():
    return render_template('homepage.html', Title='MCGRATH TRANSLATIONS')


@app.route('/about')
def about():
    return render_template('about.html', Title='О ПЕРЕВОДЧИКЕ')


@app.route('/background')
def background():
    return render_template('background.html', Title='Background')


@app.route('/contact')
def contact():
    return render_template('contact.html', Title='Contact')


@app.route('/sample')
def sample():
    return render_template('sample.html', Title='Sample')


@app.route('/Services')
def services():
    return render_template('Services.html', Title='Services', Page='Services')


@app.route('/Books')
def books():
    return render_template('Books.html', Title='Books', Page='Books')


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=False, host='0.0.0.0', port=port)
