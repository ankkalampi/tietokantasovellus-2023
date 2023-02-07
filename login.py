from os import getenv
from flask import Flask
from flask import redirect, render_template, request, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash
from sqlalchemy.sql import text
from app import app
from db import db, get_user, create_user


def set_message():
    
    if session["failedlogin"]:
        if session["failedlogin"] == True:
            session["infomessage"] = "Väärä käyttäjänimi tai salasana"
            session["failedlogin"] = False
        elif session["failedlogin"] == False:
            session["infomessage"] = ""
    else:
        session["infomessage"] = ""
    
    if session["usercreated"]:
        if session["usercreated"] == True:
            session["infomessage"] = "Käyttäjä luotu!"
            session["usercreated"] = False
        else:
            session["infomessage"] = ""


    