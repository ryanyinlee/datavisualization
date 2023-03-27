from plotly.graph_objs import Bar, Layout
from plotly import offline

from dice import Die

die0 = Die()
die1 = Die()

results = []

for rollnum in range(1000):
    result = die0.roll() * die1.roll()
    results.append(result)

frequencies = []

maxresult = die0.numsides * die1.numsides

for value in range(1, maxresult + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

xvals = list(range(1, maxresult + 1))
data = [Bar(x=xvals, y=frequencies)]

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}

my_layout = Layout(title='Results of rolling two D6 1000 times multiplied', xaxis = x_axis_config, yaxis = y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='multiply2xd6.html')