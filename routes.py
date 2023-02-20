
from os import getenv
from flask import Flask
from flask import redirect, render_template, request, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash
from sqlalchemy.sql import text
from app import app
from db import db
from user import create_user, login_user



@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")



##########################################################################################
## authentication routes

@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]
    session["username"] = username

    if login_user(username, password):
        return redirect("/user/" + session["username"])
    else:
        return render_template("index.html", message = "Väärä käyttäjänimi tai salasana")


@app.route("/logout")
def logout():
    del session["username"]
    return redirect("/")




##########################################################################################
## user account routes

@app.route("/user/<username>")
def user(username):

    if session["username"] == username:
        return render_template("profile.html", username=username)
    
@app.route("/profile")
def profile():
    return render_template("profile.html")

@app.route("/register")
def register():
    #set_message()
    return render_template("register.html")

@app.route("/create_user", methods=[ "POST"])
def createuser():
    username = request.form["username"]
    password = request.form["password"]

    if create_user(username, password):
        
        return render_template("index.html", message = "käyttäjä luotu")
    else:
       
        return render_template("register.html",message = "käyttäjänimi varattu")
    


##########################################################################################
## chatroom routes


@app.route("/add_chatroom")
def add_chatroom():
    pass

@app.route("/remove_chatroom")
def remove_chatroom():
    pass

@app.route("/play_chatroom")
def play_chatroom():
    pass

@app.route("/edit_chatroom")
def edit_chatroom():
    pass




##########################################################################################
## npc routes

@app.route("/add_npc")
def add_npc():
    pass

@app.route("/remove_npc")
def remove_npc():
    pass

@app.route("/edit_npc")
def edit_npc():
    pass









