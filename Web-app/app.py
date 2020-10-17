from flask import Flask, render_template
from cs50 import SQL
from helper import url


app = Flask(__name__)

app.config["TEMPLATES_AUTO_RELOAD"] = True

db = SQL("sqlite:///questions.db")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/add")
def addqn():
    return render_template("addqn.html")


if __name__ == '__main__':
    app.run()
