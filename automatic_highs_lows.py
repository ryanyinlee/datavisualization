import csv

import matplotlib.pyplot as plt

from datetime import datetime


filename = 'data/death_valley_2018_simple.csv'
filename= 'data/sitka_weather_2018_simple.csv'

with open(filename) as f:
    reader = csv.reader(f)
    headerrow = next(reader)
    highs = []
    dates = []
    lows = []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            high = int(row[headerrow.index('TMAX')])
            low = int(row[headerrow.index('TMIN')])
        except:
            print(f"Missing data for {current_date}")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

plt.style.use('seaborn')

fig, ax = plt.subplots()
ax.plot(dates, highs, c='red')
ax.plot(dates, lows, c='blue')
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)


nameindex = headerrow.index('NAME')

date = headerrow.index('DATE')
year = row[date].split('-')[0]

ax.set_title(f'Highs & Lows, {row[nameindex]}, {year}', fontsize = 24)
ax.set_xlabel('', fontsize = 16)
fig.autofmt_xdate()
ax.set_ylabel('Temp (F)', fontsize = 16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()
