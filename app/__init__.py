from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from config import basedir

# create an instance of flask
app = Flask(__name__)
# include config info from config.py
app.config.from_object('config')
# create an instance of SQLAlchemy
db = SQLAlchemy(app)

from app import views, models


