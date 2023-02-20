from os import getenv
from flask import Flask
from flask import redirect, render_template, request, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash
from sqlalchemy.sql import text
from app import app


app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")#.replace("://", "ql://", 1)
db = SQLAlchemy(app)


    


