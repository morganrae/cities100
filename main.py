import csv
import pandas as pd
import json

# Load descriptive data on cities:
cities_data = pd.read_csv('cities_data_clean.csv',encoding='utf-8',
    lineterminator='\n')

cities_locs = []

for index,row in cities_data.iterrows():
    lat = cities_data.loc[index,'Latitude']
    lng = cities_data.loc[index,'Longitude']
    loc = cities_data.loc[index,'Location']
    print(loc)
    
    cities_locs.append({'loc': loc, 'lat': lat, 'lng': lng})

with open('map/map_data.json', 'w') as outfile:
    json.dump(cities_locs, outfile)
