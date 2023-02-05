from os import getenv
from flask import Flask
from flask import redirect, render_template, request, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash
from sqlalchemy.sql import text



app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")
db = SQLAlchemy(app)
app.secret_key = getenv("SECRET_KEY")



@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]

    session["username"] = username


    sql = text("SELECT id, password FROM users WHERE username=:username")
    result = db.session.execute(sql, {"username":username})
    user = result.fetchone()

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

    
    return render_template("user.html", username=username)

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

    hash_value = generate_password_hash(password)
    sql = text("INSERT INTO users(username, password) VALUES (:username, :password)")
    db.session.execute(sql, {"username":username, "password":hash_value})
    db.session.commit()

    session["failedlogin"] = False

    return redirect("/")





