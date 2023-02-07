
from os import getenv
from flask import Flask
from flask import redirect, render_template, request, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash
from sqlalchemy.sql import text
from app import app
from db import db, get_user, create_user
from login import set_message


@app.route("/", methods=["GET"])
def index():
    if request.method == "GET":
        set_message()
    return render_template("index.html")

@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]

    session["username"] = username


    
    user = get_user(username)

    if not user:
        #invalid username
        session["failedlogin"] = True
        return redirect("/")
        
    else:
        hash_value = user.password
        if check_password_hash(hash_value, password):
            #correct username
            session["failedlogin"] = False
            return redirect("/user/" + session["username"])
        else:
            #invalid password
            session["failedlogin"] = True
            return redirect("/")



@app.route("/user/<username>")
def user(username):

    if session["username"] == username:
        return render_template("profile.html", username=username)

@app.route("/add_npc")
def add_npc():

    return


@app.route("/back")
def back():
    session["failedlogin"] = False
    set_message()
    return redirect("/")


@app.route("/logout")
def logout():
    del session["username"]
    return redirect("/")

@app.route("/profile")
def profile():
    return render_template("profile.html")

@app.route("/register")
def register():
    set_message()
    return render_template("register.html")

@app.route("/create_user", methods=[ "POST"])
def createuser():
    username = request.form["username"]
    password = request.form["password"]

    if create_user(username, password):
        session["usercreated"] = True
        return redirect("/")
    else:
        session["failedlogin"] = False
        return redirect("/register")