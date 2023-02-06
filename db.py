from os import getenv
from flask import Flask
from flask import redirect, render_template, request, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash
from sqlalchemy.sql import text
from app import app

app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")##.replace("://", "ql://", 1)
db = SQLAlchemy(app)

def get_user(username):
    sql = text("SELECT id, password FROM users WHERE username=:username")
    result = db.session.execute(sql, {"username":username})
    user = result.fetchone()
    return user

def create_user(username, password):
    hash_value = generate_password_hash(password)
    sql = text("INSERT INTO users(username, password) VALUES (:username, :password)")
    db.session.execute(sql, {"username":username, "password":hash_value})
    db.session.commit()

def create_npc(name, username):
    user = get_user(username)
    user_id = user.id
    sql = text("INSERT INTO npcs(name, user_id) VALUES (:name, :user_id)")
    db.session.execute(sql, {"name":name, "user_id":user_id})
    db.session.commit()

def get_npcs(username):
    user = get_user(username)
    user_id = user.id
    sql = text("SELECT * FROM npcs WHERE user_id=:user_id")
    result = db.session.execute(sql, {"user_id":user_id})
    npcs = result.fetchall()
    return npcs
