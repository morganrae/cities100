import csv
import pandas as pd
import math

cities_data = pd.read_csv('cities_data_raw.csv',encoding='utf-8')

# Remove extra rows:
cities_data = cities_data[cities_data.City.str.contains("Mean") == False]
cities_data = cities_data[cities_data.City.str.contains("Median") == False]
cities_data = cities_data[cities_data.City.notnull() == True]

# Create row with full location:
cities_data['Location'] = 0
for index, row in cities_data.iterrows():
  cities_data.loc[index,'Location'] = (cities_data.loc[index,'City'] + ", " +
    cities_data.loc[index,'State'] + ", USA")

cities_data.to_csv('cities_data_clean.csv',encoding='utf-8')