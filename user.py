from os import getenv
from flask import Flask
from flask import redirect, render_template, request, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash
from sqlalchemy.sql import text
from app import app
from db import db, get_user, create_user


def login(username, password):
    pass

def logout():
    pass

def register(username, password):
    pass

def remove_user(username):
    pass

def set_admin(username):
    pass
