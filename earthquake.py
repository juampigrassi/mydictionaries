'''
the eq_data file is a json file that contains detailed information about
earthquakes around the world for a period of a month.
NOTE: No hard-coding allowed except for keys for the dictionaries
1) print out the number of earthquakes
2) iterate through the dictionary and extract the location, magnitude, 
   longitude and latitude of the location and put it in a new
   dictionary, name it 'eq_dict'. We are only interested in earthquakes that have a
   magnitude > 6. Print out the new dictionary.
3) using the eq_dict dictionary, print out the information as shown below (first 
three shown):
Location: Northern Mid-Atlantic Ridge
Magnitude: 6.2
Longitude: -36.0923
Latitude: 35.4364
Location: 166km SSE of Muara Siberut, Indonesia
Magnitude: 6.1
Longitude: 100.0208
Latitude: -2.8604
Location: 14km ENE of Puerto Madero, Mexico
Magnitude: 6.6
Longitude: -92.2981
Latitude: 14.7628
'''
import json

infile = open('eq_data.json','r')
eq = json.load(infile)

#print out the number of earthquakes

print('The total number of earthquakes is ' + str(eq['metadata']['count']))
print()

#iterate through the dictionary and extract the location, magnitude, 
#  longitude and latitude of the location and put it in a new
#dictionary, name it 'eq_dict'. We are only interested in earthquakes that have a
#magnitude > 6. Print out the new dictionary.

list_eq = eq['features']
eq_dict = {'location': [], 'magnitude':[], 'longitude':[], 'latitude':[]}

#Generate and print new dictionary named eq_dict

for eqs in list_eq: 
   if eqs['properties']['mag'] > 6:
      eq_dict['location'].append(eqs['properties']['place'])
      eq_dict['magnitude'].append(eqs['properties']['mag'])
      eq_dict['longitude'].append(eqs['geometry']['coordinates'][0])
      eq_dict['latitude'].append(eqs['geometry']['coordinates'][1])

print(eq_dict)
print('\n')

#Display output with three first earthquakes

i = 0
while i <= 2:
   for k,j in eq_dict.items():
      print(k + ':', j[i])
   i += 1 
   print()


    
