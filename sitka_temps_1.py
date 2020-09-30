import csv

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

for row in csv_file:
    highs.append(int(row[5]))           # we're looking at TMAX

print(highs)

import matplotlib.pyplot as plt

plt.plot(highs, c="red")        # line color is red             we only gave it one list instead of 2 for each axis

plt.title("Daily High Temps, July 2018", fontsize = 16)
plt.xlabel("")
plt.ylabel("Temperature (F)", fontsize = 16)
plt.tick_params(axis="both",which="major",labelsize=16)    # defining ticks on x and y-axes

plt.show()              # so we can see it on the screen

