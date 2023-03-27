import csv



filename = 'data/sitka_07-2018-simple.csv'

with open(filename) as f:
    reader = csv.reader(f)
    headerrow = next(reader)
    
    highs = []
    for row in reader:
        high = int(row[5])
        highs.append(high)

print(highs)
"""    for index, columnheader, in enumerate(headerrow):
        print(index, columnheader)"""