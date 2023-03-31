import json

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

print(mags[:10])
print(longs[:10])
print(latis[:10])


print(len(all_earthquake_dicts))

readable_file = 'data/readable_earthquake_data.json'

with open(readable_file, 'w') as f:
    json.dump(all_earthquate_data, f, indent=4)