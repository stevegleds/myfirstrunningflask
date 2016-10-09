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
print(df[df.Date > "2015-10-05"])
print(df[df.Date < "2015-10-05"])
print(df[df.Date == "2015-10-05"])
