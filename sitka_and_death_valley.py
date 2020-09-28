import csv
from datetime import datetime

dv_file = open("death_valley_2018_simple.csv","r")

valley_file = csv.reader(dv_file,delimiter=",")

header_row = next(valley_file)

names = []
highs = []
lows = []
dates = []

for row in (valley_file):

    try:
        high = int(row[4])
        low = int(row[5])
        thedate = datetime.strptime(row[2],'%Y-%m-%d')
    except ValueError:
        print(f"Missing data for {thedate}")
    else:
        highs.append(high)
        lows.append(low)
        dates.append(thedate)


sitka_file = open("sitka_weather_2018_simple.csv","r")

s_file = csv.reader(sitka_file,delimiter=",")

header1_row = next(s_file)

highs2 = []
lows2 = []
dates2 = []

for row in s_file:
    highs2.append(int(row[5]))
    lows2.append(int(row[6]))
    thedate2 = datetime.strptime(row[2],'%Y-%m-%d')
    dates2.append(thedate2)

import matplotlib.pyplot as plt

fig, ax = plt.subplots(2)

ax[0].plot(dates,highs, c="red", alpha = 0.5)
ax[0].plot(dates, lows, c="blue",  alpha = 0.5)

ax[1].plot(dates2,highs2, c="red", alpha = 0.5)
ax[1].plot(dates2, lows2, c="blue",  alpha = 0.5)

ax[0].title("Death Valley, CA US", fontsize= 16)
ax[0].xlabel("")
ax[0].ylabel("Temperature (F)",fontsize=16)
ax[0].tick_params(axis="both",labelsize=12)

ax[1].title("Sitka, AK US", fontsize= 16)
ax[1].xlabel("")
ax[1].ylabel("Temperature (F)",fontsize=16)
ax[1].tick_params(axis="both",labelsize=12)

fig.autofmt_xdate()


ax[0].fill_between(dates, highs, lows, facecolor = 'blue', alpha=0.1)
ax[1].fill_between(dates2, highs2, lows2, facecolor = 'blue', alpha=0.1)


plt.show()




