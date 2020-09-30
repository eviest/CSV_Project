import csv
from datetime import datetime

open_file = open("sitka_weather_07-2018_simple.csv", "r")

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
dates = []

x = datetime.strptime('2018-07-01', '%Y-%m-%d')        # converts from str to datetime format
print(x)



for row in csv_file:
    highs.append(int(row[5]))           # we're looking at TMAX
    the_date = datetime.strptime(row[2], '%Y-%m-%d')
    dates.append(the_date)


import matplotlib.pyplot as plt

fig = plt.figure()

plt.plot(dates, highs, c="red")        # line color is red             we only gave it one list instead of 2 for each axis

plt.title("Daily High Temps, July 2018", fontsize = 16)
plt.xlabel("")
plt.ylabel("Temperature (F)", fontsize = 16)
plt.tick_params(axis="both",labelsize=16)    # defining ticks on x and y-axes

fig.autofmt_xdate()

plt.show()              # so we can see it on the screen