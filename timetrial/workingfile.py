﻿# import things
from flask_table import Table, Col
import timetrial
import os
# Declare your table


class ItemTable(Table):
    Runner = Col('Runner')
    Digitime = Col('Digitime')
    Time = Col('Time')
    Date = Col('Date')
    Pace = Col('Pace')


# Get some objects
class Item(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description
# Or, equivalently, some dicts
items2 = [dict(name='Name1', description='Description1'),
         dict(name='Name2', description='Description2'),
         dict(name='Name3', description='Description3')]

filename = 'timetrialtest.csv'  # this is a test file
timetrial_file = os.path.join('', filename)
race_data = timetrial.parse(timetrial_file, ',')
items = race_data
# Populate the table
table = ItemTable(items)

# Print the html
print(table.__html__())
# or just {{ table }} from within a Jinja template