from flask import Flask
from flask_sqlalchemy import SQLAlchemy
CSRF_ENABLED = True  # from grinberg
SECRET_KEY = "you-will-never-guess"  # from grinberg
#  https://www.youtube.com/watch?v=Tu4vRU4lt6k

import os  # from grinberg
basedir = os.path.abspath(os.path.dirname(__file__))  ## from grinberg
appal = Flask(__name__)  # create an instance of flask
appal.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'appal.db')
db = SQLAlchemy(appal)  # create an instance of SQLAlchemy
db.create_all()


class Example(db.Model):
    __tablename__ = 'example'
    id = db.Column('id', db.Integer, primary_key=True )
    data = db.Column('data', db.Unicode)






