from app import app
from flask import render_template, request
from app.models import model, formopener

@app.route('/')
@app.route('/index')
def index():
    return render_template("home.html")
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
        
@app.route("/hamburger", methods=["GET", "POST"])
def hamburger():
    if request.method == "GET":
        return render_template("/hamburger.html")
    else:
        userdata1 = formopener.dict_from(request.form)
        style1 = userdata1["style1"].decode('utf-8')
        meat = userdata1["meat"].decode('utf-8')
        color = userdata1["color"].decode('utf-8')
        when1 = userdata1["when1"].decode('utf-8')
        age = userdata1["age"].decode('utf-8')
        print(userdata1)
        hamburger = str(model.chain_quiz(style1, meat, color, when1, age))
        return render_template("/hamburger.html", hamburger = hamburger)
@app.route("/music", methods=["GET", "POST"])
def music():
    if request.method == "GET":
        return render_template("/music.html")
    else:
        userdata2 = formopener.dict_from(request.form)
        print(request.form)
        print(userdata2)
        style = userdata2["style"].decode('utf-8')
        why = userdata2["why"].decode('utf-8')
        feel = userdata2["feel"].decode('utf-8')
        where = userdata2["where"].decode('utf-8')
        artist = userdata2["artist"].decode('utf-8')
        music = str(model.genre_quiz(style, why, feel, where, artist))
        return render_template("/music.html", music = music)