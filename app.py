from flask import Flask, render_template, redirect, url_for
from flask_fontawesome import FontAwesome

app = Flask(__name__, static_url_path='', static_folder='static', template_folder='templates')
app.config["DEBUG"] = True
fa = FontAwesome(app)


@app.route('/')
def home():
    return render_template("home.html")

@app.route('/game')
def game():
    return render_template("game.html")

@app.route('/prepare')
def prepare():
    return render_template("prepare.html")

@app.route('/pitchers')
def pitchers():
    return render_template("pitchers.html")

if __name__ == '__main__':
    app.run(host="localhost", port=8000, debug=True)
