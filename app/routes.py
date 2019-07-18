from app import app
from flask import render_template, request
from app.models import model, formopener

@app.route('/')
@app.route('/index')
def index():
    return render_template("home.html")
@app.route("/hamburger")
def hamburger():
    return render_template("hamburger.html")
@app.route("/music")
def music():
    return render_template("music.html")
@app.route("/futbol", methods=["GET", "POST"])
def futbol():
    if request.method == "GET":
        return render_template("/futbol.html")
    else:
        userdata = formopener.dict_from(request.form)
        position = userdata["position"].decode('utf-8')
        goal = userdata["goal"].decode('utf-8')
        mindset = userdata["mindset"].decode('utf-8')
        team = userdata["team"].decode('utf-8')
        best = userdata["best"].decode('utf-8')
        print(userdata)
        futbol = str(model.soccer_quiz(position, goal, mindset, team, best))
        return render_template("/futbol.html", futbol = futbol)