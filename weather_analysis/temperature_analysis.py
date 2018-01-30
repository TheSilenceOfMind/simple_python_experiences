"""
SOME INFO
    It's much useful to unifiable to scan a whole bunch of data and make a
    graph for each of them. It is preferable to do in loop using index
    shifting. In this case it's need to solve unification problem with
    painting the grid for minor and major.
"""

import csv
from matplotlib import pyplot as plt
from datetime import datetime
import matplotlib.ticker as ticker
from matplotlib.dates import DateFormatter


def get_files_content(filename):
    """
    This function gets filename and retrieve data from it to the list which
    is a returned value.
    The values in the returned list are parsed to correct type.

    :param filename: string
    :return: data list - list of rows with data
    """
    with open(filename) as f:
        reader = csv.reader(f, delimiter=';')

        # returned list
        data = []

        for row in reader:
            building_row = []
            if row:
                for i in row:
                    # parsing to correct type and appending to the list
                    # try parse to int
                    try:
                        value = int(i)
                    except:
                        # try parse to float
                        try:
                            value = float(i)
                        # append string instead int/float
                        except:
                            value = str(i)
                            building_row.append(value)
                        else:
                            building_row.append(value)
                    else:
                        building_row.append(value)
            data.append(building_row)
        return data


def ordered_print(list_var):
    """
    This function just used for simplified interface while working with code

    :param list_var:
    :return: none
    """
    for i, v in enumerate(list_var):
        print(i, v)


def get_dates_from_data(data):
    """
    The function retrieves list of dates from whole dataset

    :param data: list of rows
    :return: list of dates
    """
    dates = []
    for row in data:
        # build string to parse it to date format
        str_cur_date = ''
        for i in range(0, 5):
            str_cur_date += str(row[i]) + '-'
        str_cur_date = str_cur_date[:-1]
        cur_date = datetime.strptime(str_cur_date, '%Y-%m-%d-%H-%M')
        dates.append(cur_date)
    return dates


data = get_files_content('weather_history_SP.csv')

header_row = data[12]
types = data[7]
# ordered_print(types)
data = data[13:]

# set list of current data
temperatures = [i[5] for i in data]
dates = get_dates_from_data(data)

# plot data
fig = plt.figure(dpi=100, figsize=(10, 6))
ax = fig.gca()
plt.plot(dates, temperatures, c='blue')

# format plot
plt.title(header_row[5] + ' in Saint-Petersburg in 2018')
plt.xlabel('')

# set limit between little(minor) and main(major) ticks
ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.25))
ax.yaxis.set_major_locator(ticker.MultipleLocator(1))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.2))

# set date format
ax.xaxis.set_major_formatter(DateFormatter('%d.%m'))

# set auto-rotation of x-axes labels, and something more I guess
fig.autofmt_xdate()

plt.ylabel(types[5])
plt.tick_params(axis='both', labelsize=8)
plt.grid()

# it is needed if we want see minor grid
plt.grid(which='minor', alpha=0.1)

plt.show()
