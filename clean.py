import csv
import pandas as pd
import math

cities_data = pd.read_csv('cities_data_raw.csv',encoding='utf-8')

cities_data = cities_data[cities_data.City.str.contains("Mean") == False]
cities_data = cities_data[cities_data.City.str.contains("Median") == False]
cities_data = cities_data[cities_data.City.notnull() == True]

cities_data.to_csv('cities_data_clean.csv')