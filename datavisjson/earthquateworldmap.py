import json

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

filename = 'data/eq_data_1_day_m1.json'

with open(filename) as f:
    all_earthquate_data =  json.load(f)

all_earthquake_dicts = all_earthquate_data['features']

mags = []
longs = []
latis = []

for earthquake_dict in all_earthquake_dicts:
    mag = earthquake_dict['properties']['mag']
    long = earthquake_dict['geometry']['coordinates'][0]
    lati = earthquake_dict['geometry']['coordinates'][1]
    mags.append(mag)
    longs.append(long)
    latis.append(lati)

data = [Scattergeo(lon = longs, lat = latis)]
my_layout = Layout(title='Globaly Earthquaked in a 24 Hour Period')

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_earthquakes.html')