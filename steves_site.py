import os
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def homeppage():
    return render_template('homepage.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/background')
def background():
    return render_template('background.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/sample')
def sample():
    return  render_template('sample.html')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, port=port)