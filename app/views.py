from flask import render_template, flash, redirect
from app import app


@app.route('/')
def hello_world():
    return 'Hello World! How\'s Things?'
