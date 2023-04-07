import json

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

filename = 'data/eq_data_7_day_4-7-23.json'

with open(filename) as f:
    all_earthquate_data =  json.load(f)

all_earthquake_dicts = all_earthquate_data['features']
metadata = all_earthquate_data['metadata']

mags = []
longs = []
latis = []
hovertexts = []

for earthquake_dict in all_earthquake_dicts:
    mags.append(earthquake_dict['properties']['mag'])
    longs.append(earthquake_dict['geometry']['coordinates'][0])
    latis.append(earthquake_dict['geometry']['coordinates'][1])
    hovertexts.append(earthquake_dict['properties']['title'])

data = [{
    'type': 'scattergeo',
    'lon': longs,
    'lat': latis,
    'text': hovertexts,
    'marker': {
        'size': [5*mag for mag in mags],
        'color': mags,
        'colorscale': 'temps',
        'reversescale': False,
        'colorbar': {'title': 'Magnitude'},
    },

}]
my_layout = Layout(title=metadata['title'])

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_earthquakes.html')

