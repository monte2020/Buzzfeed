from app import app
from flask import render_template, request
from app.models import model, formopener

@app.route('/')
@app.route('/index')
def index():
    return render_template("home.html")
@app.route("/futbol")
def futbol():
    return render_template("futbol.html")
@app.route("/hamburger")
def hamburger():
    return render_template("hamburger.html")
@app.route("/music")
def music():
    return render_template("music.html")