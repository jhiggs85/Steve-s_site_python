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


if __name__ == '__main__':
    app.run(debug=True)