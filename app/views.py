from flask import render_template, flash, redirect
from app import app
from timetrial import timetrial


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
    return render_template('memberedit.html') # TODO edit / create memberedit.html


@app.route('/timetrialindex')
def timetrialindex():
    file = 'timetrial\\timetrialtest.csv'
    race_data = timetrial.parse(file, ',')
    runners_list, runners_summary = timetrial.get_runners_starting_list(race_data)
    print('runners summaries in views.py are: ', runners_summary)
    return render_template('timetrialindex.html', title='Time Trial', race_data=race_data,
                           runners=runners_list, runners_summary=runners_summary)
