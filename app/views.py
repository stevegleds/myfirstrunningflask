from flask import render_template, flash, redirect
from app import app


@app.route('/')
@app.route('/index')
def index():
    member = {'nickname': 'Steve'}  # fake user
    results = [  # fake race results
        {
            'member': {'nickname': 'Steve'},
            'race': 'ERR Time Trial'
        },
        {
            'member': {'nickname': 'Sarah'},
            'race': 'Horton Parkrun'
        }
        ]
    return render_template('index.html',
                           title='Home',
                           member=member,
                           results=results)

@app.route('/memberprofile')
def memberprofile():
    return render_template('memberprofile.html', title='Member')

@app.route('/memberedit')
def memberedit():
    return  render_template('memberedit.html') # TODO edit / create memberedit.html
