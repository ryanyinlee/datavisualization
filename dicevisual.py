from plotly.graph_objs import Bar, Layout
from plotly import offline

from dice import Die

die = Die()

results = []

for rollnum in range(1000):
    result = die.roll()
    results.append(result)

frequencies = []

for value in range(1, die.numsides + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

xvals = list(range(1, die.numsides+1))
data = [Bar(x=xvals, y=frequencies)]

x_axis_config = {'title': 'Result'}
y_axis_config = {'title': 'Frequency of Result'}

my_layout = Layout(title='Results of rolling a D6 1000 times', xaxis = x_axis_config, yaxis = y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6.html')