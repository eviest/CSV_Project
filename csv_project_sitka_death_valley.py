import csv
from datetime import datetime

# Open Sitka file
open_file_s = open("sitka_weather_2018_simple.csv", "r")

csv_file_s = csv.reader(open_file_s, delimiter = ",")

header_row_s = next(csv_file_s)

# Open Death Valley file
open_file_dv = open("death_valley_2018_simple.csv", "r")

csv_file_dv = csv.reader(open_file_dv, delimiter = ",")

header_row_dv = next(csv_file_dv)

# Create lists
highs_s = []
lows_s = []
dates_s = []
highs_dv = []
lows_dv = []
dates_dv = []

# Iterate through Sitka file to fill lists
for row in csv_file_s:
    TMAXindex_s = header_row_s.index('TMAX')
    TMINindex_s = header_row_s.index('TMIN')
    DATEindex_s = header_row_s.index('DATE')
    TITLEindex_s = header_row_s.index('NAME')
            
    highs_s.append(int(row[TMAXindex_s]))
    lows_s.append(int(row[TMINindex_s]))
    the_date = datetime.strptime(row[DATEindex_s], '%Y-%m-%d')
    dates_s.append(the_date)
    title_s = row[TITLEindex_s]

# Iterate through Death Valley file to fill lists
for row in csv_file_dv:
    TMAXindex_dv = header_row_dv.index('TMAX')
    TMINindex_dv = header_row_dv.index('TMIN')
    DATEindex_dv = header_row_dv.index('DATE')
    TITLEindex_dv = header_row_dv.index('NAME')
    
        
    if row[TMAXindex_dv] != '' and row[TMINindex_dv] != '':
        highs_dv.append(int(row[TMAXindex_dv]))
        lows_dv.append(int(row[TMINindex_dv]))
        the_date = datetime.strptime(row[DATEindex_dv], '%Y-%m-%d')
        dates_dv.append(the_date)
    title_dv = row[TITLEindex_dv]


# Plot on a chart
import matplotlib.pyplot as plt

# Create two charts
fig, ax = plt.subplots(2)

# Plot dates, highs, and lows
ax[0].plot(dates_s, highs_s, c="red", alpha=0.5)
ax[0].plot(dates_s, lows_s, c="blue", alpha=0.5)         
ax[1].plot(dates_dv, highs_dv, c="red", alpha=0.5)
ax[1].plot(dates_dv, lows_dv, c="blue", alpha=0.5) 

# Chart title size
ax[0].set_title(title_s, fontsize = 16)
ax[1].set_title(title_dv, fontsize = 16)

# Fill in between lines
ax[0].fill_between(dates_s, highs_s, lows_s, facecolor='blue', alpha=0.1)
ax[1].fill_between(dates_dv, highs_dv, lows_dv, facecolor='blue', alpha=0.1)

# Format date
fig.autofmt_xdate()

# Show the line charts
plt.show()