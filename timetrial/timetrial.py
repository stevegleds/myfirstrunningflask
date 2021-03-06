# testing

import csv
import os
from collections import Counter

TIME_TRIAL_DISTANCE = 3.0
SLOWEST_PACE = 99

# Working through https://automatetheboringstuff.com/chapter12/#calibre_link-64
# 10 July 2015 branched to follow newcoder.io tutorial on data visualization
# 11 November 2015 Added to desktop

# RUN_FILE = 'timetrial/timetrial.csv' # this is  the full file
filename = 'timetrialtest.csv'  # this is a test file
timetrial_file = os.path.join('timetrial', filename)


def parse(raw_file, delimiter):
    """
    :param raw_file: probably csv file
    :param delimiter: specify delimiter #TODO add default arg : ','
    :return: parsed data
    Parses a raw CSV file to a JSON-line object.
    """
    # open csv file
    opened_file = open(raw_file)
    # read csv file
    csv_data = csv.reader(opened_file, delimiter=delimiter)  # first delimiter is csv.reader variable name
    # csv_data object is now an iterator meaning we can get each element one at a time

    # build data structure to return parsed data
    parsed_data = []  # this list will store every row of data
    fields = csv_data.__next__()  # this will be the column headers; we can use .next() because csv_data is an iterator
    for row in csv_data:
        if row[1] == "":  # there is no text in the runner field so no data to process
            pass
        else:
            parsed_data.append(dict(zip(fields, row)))  # Creates a new dict item for each row with col header as key and stores in a list
        #  racer_count += 1  # This is number of racers not races
    print("data list is: ", parsed_data)
    print("Type of parsed_data is: ", type(parsed_data))
    # close csv file
    opened_file.close()
    return parsed_data


def races_summary(race_data):
    # count number of races, races per day, and races per runner
    runners_by_date = Counter(item['Date'] for item in race_data)  # each element contains date and number of runners for that date
    races_by_runner = Counter(item['Runner'] for item in race_data)  # each element contains runner and number of races for that runner
    print("number of races is: ", len(runners_by_date))
    #print("the races are: ")
    #for k, v in runners_by_date.items():
    #    print(k, "-->", v)
    #print("The races by each runner: ")
    #for k, v in races_by_runner.items():
    #    print(k, "-->", v)
    return


def get_runners_starting_list(new_data):
    # initializes runner_summary to 0 to store summary info
    runner_counter = Counter(item['Runner'] for item in new_data)  # stores the number of races per runner
    print("runner counter is: ", runner_counter)
    runners_list = [runner for runner in sorted(runner_counter)]  # stores list of runners full names
    # create list of runners including name, number of races, distance and time
    runners_summary ={}
    # runners_summary['fields'] = 'races', 'total_distance', 'total_time'
    for runner in runners_list:
        runners_summary[runner] = [0, 0, 'date', 'pb time', SLOWEST_PACE]  # total distance, total time, pb date, pb time, pb pace
    print("Runners summary at start is: ", runners_summary)
    print("Runner list is :", runners_list)
    print("************")
    return runners_list, runners_summary


def get_distances(new_data):
    total_distance = 0
    for race in new_data:
        if race['Runner'] != "" :
            total_distance += float(TIME_TRIAL_DISTANCE)
    return total_distance


def get_runners_summary(new_data, runners_summary): #TODO get max pace
    print("*** get_runners_summary starts ***")
    for result in new_data:
        print("Result is : ", result)
        print("runner field 3 type is is: ", type(runners_summary[result['Runner']][0]))
        print("runners_summary element type is: ", type(runners_summary[result['Runner']]))
        distance, digitime, date, time, pace = TIME_TRIAL_DISTANCE, result['Digitime'], result['Date'], result['Time'], result['Pace']
        runners_summary[result['Runner']][0] += distance
        if float(runners_summary[result['Runner']][4]) >= float(pace):
            runners_summary[result['Runner']][1] = digitime
            runners_summary[result['Runner']][2] = date
            runners_summary[result['Runner']][3] = time
            runners_summary[result['Runner']][4] = pace
        print("************ one race processed ************")
        # runners_summary[result['Runner']][4] = min(runners_summary[result['Runner']][4], result['Pace'])
    print("*** Runners Summary is now : ", runners_summary)
    print("*** get_runners_summary ends ***")    
    return runners_summary


def show_pbs(runners_distances):
    print("************ PBs !!! ************")
    pbs = runners_distances
    print(pbs)
    print(type(pbs))

    # runners_summary[result['Runner']][0] += distance


def main():
    # Call our parse function with required file an delimiter
    race_data = parse(timetrial_file, ',')
    races_summary(race_data)
    print("The keys in the data are:", race_data[0].keys())
    runners_list, runners_summary = get_runners_starting_list(race_data)
    print("Runners are: ", runners_list)
    runners_distances = get_runners_summary(race_data, runners_summary)
    print("Runners distances are:", runners_distances)
    show_pbs(runners_distances)
    total_distance = get_distances(race_data)
    print('Total distance run : ', total_distance)
    return total_distance

if __name__ == "__main__":
    main()
