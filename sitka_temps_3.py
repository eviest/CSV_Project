# Look at video from 9/16/2020 to include extra notes
import csv
from datetime import datetime

open_file = open("sitka_weather_2018_simple.csv", "r")

csv_file = csv.reader(open_file, delimiter = ",")

header_row = next(csv_file)

'''
print(header_row)

# shows index and value of each item

for index, column_header in enumerate(header_row):
    print(index, column_header)

# make sure to right click --> run python file in terminal
'''

highs = []
lows = []
dates = []

x = datetime.strptime('2018-07-01', '%Y-%m-%d')        # converts from str to datetime format
print(x)



for row in csv_file:
    highs.append(int(row[5]))           # we're looking at TMAX
    lows.append(int(row[6]))
    the_date = datetime.strptime(row[2], '%Y-%m-%d')
    dates.append(the_date)

#print(lows)

# Plot highs and dates on a chart
import matplotlib.pyplot as plt

fig = plt.figure()

plt.plot(dates, highs, c="red", alpha=0.5)        # line color is red             we only gave it one list instead of 2 for each axis
plt.plot(dates, lows, c="blue", alpha=0.5)          # make lines more transparent w/alpha

# Chart title
plt.title("Daily High and Low Temps, 2018", fontsize = 16)
plt.xlabel("")

plt.fill_between(dates,highs, lows, facecolor='blue', alpha=0.1)       # fill in between graphs

# The call to fig.auto

plt.ylabel("Temperature (F)", fontsize = 16)
plt.tick_params(axis="both",labelsize=16)    # defining ticks on x and y-axes

fig.autofmt_xdate()

plt.show()              # so we can see it on the screen


# There are 2 x points (highs and lows) and one y point (temp)

# I created a new graph for lows and dates in addition to the highs and dates graph (2 graphs)
