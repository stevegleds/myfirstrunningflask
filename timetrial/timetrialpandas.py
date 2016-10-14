import csv
import os
import pandas as pd
import pandas_datareader
from pandas import DataFrame
import datetime
from pandas_datareader import data, wb


TIME_TRIAL_DISTANCE = 3.0
SLOWEST_PACE = 99

# Working through https://automatetheboringstuff.com/chapter12/#calibre_link-64
# 10 July 2015 branched to follow newcoder.io tutorial on data visualization
# 11 November 2015 Added to desktop

# RUN_FILE = 'timetrial/timetrial.csv' # this is  the full file
filename = 'timetrialtest.csv'  # this is a test file
timetrial_file = os.path.join('timetrial', filename)

df = pd.read_csv(filename, parse_dates=[0], dayfirst=True)
print(df.head())
choice =''
while choice.lower() != 'quit':
    is_ascending = 'False'
    choice = input('Date, Runner, Time or Quit')
    if choice == 'Runner': is_ascending = 'True'
    if choice.lower() in ('date', 'runner', 'time', 'quit'):
        print(df.sort_values(choice, ascending=is_ascending))
    else:
        print('Please enter Date, Runner, Time or Quit')
#  df_date = df.sort_values('Date', ascending=False)
#  print(df_date)
#  print(df[df.Date > "2015-10-05"])
#  print(df[df.Date < "2015-10-05"])
#  print(df[df.Date == "2015-10-05"])
