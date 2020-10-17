from flask import Flask, render_template, request, redirect
from cs50 import SQL
import random
import requests
from helper import url, Device_ID, API_KEY


app = Flask(__name__)

app.config["TEMPLATES_AUTO_RELOAD"] = True

db = SQL("sqlite:///questions.db")


@app.route("/", methods = ["GET" , "POST"])
def index():
    n = str(random.randint(0,100))
    response = requests.get(url+n)
    if request.method == "GET":
        return render_template("index.html", Device_ID=Device_ID, API_KEY=API_KEY, fact=response.text)
    else:
        dif = request.form.get("difficulty")
        tpc = request.form.get("topic")
        Qndata = db.execute("SELECT * FROM questions WHERE topic = :tpc AND difficulty = :dif", tpc=tpc, dif=dif)
        return render_template("index.html", Qndata=Qndata, Device_ID=Device_ID, API_KEY=API_KEY, fact=response.text)


@app.route("/add", methods = ["GET" , "POST"])
def addqn():
    n = str(random.randint(0,100))
    response = requests.get(url+n)
    if request.method == "GET":
        return render_template("addqn.html", fact=response.text)
    else:
        qstn = request.form.get("question")
        tl = request.form.get("time")
        tpc = request.form.get("topic")
        dif = request.form.get("difficulty")
        db.execute("INSERT INTO questions(qn, topic, difficulty, timelimit) VALUES(:qstn, :tpc, :dif, :tl)", qstn=qstn, tpc=tpc, dif=dif, tl=tl)
        return redirect("/")

if __name__ == '__main__':
    app.run()
