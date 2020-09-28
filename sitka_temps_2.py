import csv
from datetime import datetime

open_file = open("sitka_weather_07-2018_simple.csv","r")

csv_file = csv.reader(open_file,delimiter=",")

header_row = next(csv_file)

highs = [] #creates the list variables for the highs
dates =[] #creates a list for the variables of the date

x = datetime.strptime('2018-07-01','%Y-%m-%d')



for row in csv_file:
    highs.append(int(row[5])) #appends the list to show the last row 
    thedate = datetime.strptime(row[2], '%Y-%m-%d')
    dates.append(thedate)


import matplotlib.pyplot as plt

fig = plt.figure()

plt.plot(dates,highs, c="red")

plt.title("Daily High Temps, July 2018", fontsize= 16)
plt.xlabel("")
plt.ylabel("Temperature (F)",fontsize=16)
plt.tick_params(axis="both",labelsize=16)

fig.autofmt_xdate()

plt.show()

