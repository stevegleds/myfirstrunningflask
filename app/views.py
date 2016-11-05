from flask import render_template, flash, redirect
from app import app
from timetrial import timetrial
from timetrial import timetrialpandas
import os


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
    return render_template('memberedit.html')  # TODO edit / create memberedit.html


@app.route('/timetrialindex', methods=['GET', 'POST'])
def timetrialindex():
    filename = 'timetrialtest.csv'  # this is a test file
    timetrial_file = os.path.join('timetrial', filename)
    race_data = timetrial.parse(timetrial_file, ',')
    runners_list, runners_summary = timetrial.get_runners_starting_list(race_data)
    print('runners summaries in views.py are: ', runners_summary)
    return render_template('timetrialindex.html', title='Time Trial', race_data=race_data,
                            runners=runners_list, runners_summary=runners_summary)
    # return render_template('timetrialindex.html', title='Time Trial', distance='25')

@app.route('/tables')
def tables():
    from flask_table import Table, Col
    # Declare your table

    class ItemTable(Table):
        Runner = Col('Runner')
        Digitime = Col('Digitime')
        Time = Col('Time')
        Date = Col('Date')
        Pace = Col('Pace')
        classes = ['class1', 'class2']

        def tr_format(self, item):
            if float(item['Pace']) < 10:
                return '<tr class = "fast">{}</tr>'
            else:
                return '<tr>{}</tr>'

    # Get some objects
    #  class Item(object):
        #  def __init__(self, name, description):
        #    self.name = name
        #    self.description = description

    filename = 'timetrialtest.csv'  # this is a test file
    timetrial_file = os.path.join("timetrial", filename)
    race_data = timetrial.parse(timetrial_file, ',')
    items = race_data
    # Populate the table
    table = ItemTable(items)

    return render_template('tables.html', title='Time Trial', table=table)
    # Print the html
    print(table.__html__())
    # or just {{ table }} from within a Jinja template

@app.route('/timetrialindexpandas', methods=['GET', 'POST'])
def timetrialindexpandas():
    filename = 'timetrialtest.csv'  # this is a test file
    timetrial_file = os.path.join('timetrial', filename)
    race_data = timetrial.parse(timetrial_file, ',')
    runners_list, runners_summary = timetrial.get_runners_starting_list(race_data)
    print('runners summaries in views.py are: ', runners_summary)
    return render_template('timetrialindex.html', title='Time Trial', race_data=race_data,
                            runners=runners_list, runners_summary=runners_summary)
