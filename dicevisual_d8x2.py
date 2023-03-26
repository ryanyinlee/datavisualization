from plotly.graph_objs import Bar, Layout
from plotly import offline

from dice import Die

die0 = Die(8)
die1 = Die(8)

results = []

for rollnum in range(10000):
    result = die0.roll() + die1.roll()
    results.append(result)

frequencies = []

maxresult = die0.numsides + die1.numsides

for value in range(2, maxresult + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

xvals = list(range(2, maxresult + 1))
data = [Bar(x=xvals, y=frequencies)]

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}

my_layout = Layout(title='Results of rolling two D6 1000 times', xaxis = x_axis_config, yaxis = y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='2xd6.html')