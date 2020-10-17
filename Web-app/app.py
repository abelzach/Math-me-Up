from flask import Flask, render_template
from cs50 import SQL


app = Flask(__name__)


db = SQL("sqlite:///questions.db")


@app.route("/add")
def addqn():
    return render_template("addqn.html")

@app.route("/")
def index():
    return render_template("index.html")



if __name__ == '__main__':
    app.run()
