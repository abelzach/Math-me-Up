from flask import Flask, render_template
import sqlite3
import os

currentdirectory = os.path.direname(os.path.abspath(__file__))

app = Flask(__name__)
         

@app.route("/add", methods = ["POST"])
def question():
    ques = request.form["ques"]
    ans = request.form["ans"]
    level = request.form["level"]
    maths = request.form["maths"]
    connection = sqlite3.connect(currentdirectory = "\questions.db")
    cursor = connection.cursor()
    query1 = "INSERT INTO questions VALUES({q},{a},{l},{m})".format(q = ques, a = ans, l = level, m = maths)
    cursor.execute(query1)
    connection.commit()
def addqn():
    return render_template("addqn.html")

@app.route("/", methods = ["GET"])
def index():
    try:
        if request.method == "GET":
            level = request.form["level"]
            maths = request.form["maths"]
            connection = sqlite3.connect(currentdirectory = "\questions.db")
        cursor = connection.cursor()
        query1 = "SELECT ques from questions WHERE level = {l}".format(l = level)
        cursor.execute(query1)
        result = result.fetchall()[0][0]
        return render_template("index.html",ques = result)
    except:
        return render_template("index.html", ques = "")



if __name__ == '__main__':
    app.run()
