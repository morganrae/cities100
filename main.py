import csv
import pandas as pd

# Load descriptive data on cities:
cities_data = pd.read_csv('cities_data_clean.csv',encoding='utf-8',
    lineterminator='\n')