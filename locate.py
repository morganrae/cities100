import pickle
import pandas as pd
import googlemaps

geocodes = pickle.load(open('geocodes.p','rb'))
cities_data = pd.read_csv('cities_data_clean.csv',encoding='utf-8',
    lineterminator='\n')

failure_count = 0 

for index in range(0,77):
    location = cities_data.loc[index,'Location']
    print('Processing',index,':',location)

    if location not in geocodes.keys(): 
        
        with open('api.txt','r') as api_file:
            api_key = api_file.read()

        gmaps = googlemaps.Client(key=api_key)

        try: 
            geocode = gmaps.geocode(location)
            geocodes[location] = geocode
            print('Success!')
    
        except Exception as e: 
            print('Failed attempt',e,index)
            failure_count += 1

    elif geocodes[location] == []:

        print('Empty address...replacing.')

        with open('api.txt','r') as api_file:
            api_key = api_file.read()

        gmaps = googlemaps.Client(key=api_key)

        try: 
            geocode = gmaps.geocode(location)
            geocodes[location] = geocode
            print('Success!')
    
        except Exception as e: 
            print('Failed attempt', e, index)
            failure_count += 1

    else: print('Address already in dictionary.')

print(len(geocodes),'addresses in dictionary.')
print(failure_count,'failures.')

pickle.dump(geocodes,open('geocodes.p','wb'))