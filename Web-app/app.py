from flask import Flask, render_template, request, redirect
from cs50 import SQL
from helper import url


app = Flask(__name__)

app.config["TEMPLATES_AUTO_RELOAD"] = True

db = SQL("sqlite:///questions.db")


@app.route("/", methods = ["GET" , "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")


@app.route("/add", methods = ["GET" , "POST"])
def addqn():
    if request.method == "GET":
        return render_template("addqn.html")
    else:
        qstn = request.form.get("question")
        tl = request.form.get("time")
        tpc = request.form.get("topic")
        dif = request.form.get("difficulty")
        db.execute("INSERT INTO questions(qn, topic, difficulty, timelimit) VALUES(:qstn, :tpc, :dif, :tl)", qstn=qstn, tpc=tpc, dif=dif, tl=tl)
        return redirect("/")

if __name__ == '__main__':
    app.run()
