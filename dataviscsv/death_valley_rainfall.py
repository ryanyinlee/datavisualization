import csv

import matplotlib.pyplot as plt

from datetime import datetime

filename = 'data/death_valley_2018_simple.csv'

with open(filename) as f:
    reader = csv.reader(f)
    headerrow = next(reader)
    
    rainfall = []
    dates = []

    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            rain = float(row[3])
        except:
            print(f"Missing data for {current_date}")
        else:
            dates.append(current_date)
            rainfall.append(rain)


plt.style.use('seaborn')

fig, ax = plt.subplots()
ax.plot(dates, rainfall, c='green')

ax.set_title('Death Valley Rainfall, 2018', fontsize = 24)
ax.set_xlabel('', fontsize = 16)
fig.autofmt_xdate()
ax.set_ylabel('Rainfall Per Day (Inches)', fontsize = 16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()
