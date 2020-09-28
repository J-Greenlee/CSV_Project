import csv
from datetime import datetime

open_file = open("sitka_weather_2018_simple.csv","r")

csv_file = csv.reader(open_file,delimiter=",")

header_row = next(csv_file)

highs = []
lows = []
dates = []

for row in csv_file:
    highs.append(int(row[5]))
    lows.append(int(row[6]))
    thedate = datetime.strptime(row[2],'%Y-%m-%d')
    dates.append(thedate)


import matplotlib.pyplot as plt

fig = plt.figure()

plt.plot(dates,highs, c="red", alpha = 0.5)
plt.plot(dates, lows, c="blue",  alpha = 0.5)

plt.title("Daily High and Low Temps, 2018", fontsize= 16)
plt.xlabel("")
plt.ylabel("Temperature (F)",fontsize=16)
plt.tick_params(axis="both",labelsize=12)

fig.autofmt_xdate()

plt.fill_between(dates, highs, lows, facecolor = 'blue', alpha=0.1)

plt.show()