import csv
import pandas as pd
import pickle

cities_data = pd.read_csv('cities_data_raw.csv',encoding='utf-8')
geocodes = pickle.load(open('geocodes.p','rb'))

# Remove extra rows:
cities_data = cities_data[cities_data.City.str.contains("Mean") == False]
cities_data = cities_data[cities_data.City.str.contains("Median") == False]
cities_data = cities_data[cities_data.City.notnull() == True]

# Create row with full city location:
cities_data['Location'] = 0
cities_data['Latitude'] = 0
cities_data['Longitude'] = 0

for index, row in cities_data.iterrows():
    location = (cities_data.loc[index,'City'] + ", " + 
        cities_data.loc[index,'State'] + ", USA")
    cities_data.loc[index,'Location'] = location

    if location not in geocodes.keys(): 
        print('Missing geocode for ', location, '.')
    else:
        geocode = geocodes[location]
        latitude = geocode[0]['geometry']['location']['lat']
        longitude = geocode[0]['geometry']['location']['lng']

        cities_data.loc[index,'Latitude'] = latitude
        cities_data.loc[index,'Longitude'] = longitude
  
cities_data.to_csv('cities_data_clean.csv',encoding='utf-8')