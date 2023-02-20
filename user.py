from os import getenv
from flask import Flask
from flask import redirect, render_template, request, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash
from sqlalchemy.sql import text
from app import app
from db import db


def login_user(username, password):
    user = get_user(username)
    if not user:
        #invalid username
        return False      
    else:
        hash_value = user.password
        if check_password_hash(hash_value, password):
            #correct username     
            return True
        else:
            #invalid password  
            return False
    

def logout_user():
    pass

def register_user(username, password):
    pass

def remove_user(username):
    pass

def set_admin(username):
    pass


def get_user(username):
    sql = text("SELECT id, password FROM users WHERE username=:username")
    result = db.session.execute(sql, {"username":username})
    user = result.fetchone()
    return user

def create_user(username, password):
    if user_exists(username):
        return False
    else:
        hash_value = generate_password_hash(password)
        sql = text("INSERT INTO users(username, password) VALUES (:username, :password)")
        db.session.execute(sql, {"username":username, "password":hash_value})
        db.session.commit()
        return True

def user_exists(username):
    sql = text("SELECT * FROM users WHERE username=:username")
    result = db.session.execute(sql, {"username":username})
    number_of_rows = len(result.mappings().all())
    if number_of_rows > 0:
        return True
    else:
        return False
