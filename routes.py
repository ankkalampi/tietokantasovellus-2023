
from os import getenv
from flask import Flask
from flask import redirect, render_template, request, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash
from sqlalchemy.sql import text
from app import app
from db import db, get_user, create_user


@app.route("/")
def index():
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


@app.route("/back")
def back():
    session["failedlogin"] = False
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
    return render_template("register.html")

@app.route("/createuser", methods=[ "POST"])
def createuser():
    username = request.form["username"]
    password = request.form["password"]

    create_user(username, password)
    

    session["failedlogin"] = False

    return redirect("/")