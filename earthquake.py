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

#iterate through the dictionary and extract the location, magnitude, 
#  longitude and latitude of the location and put it in a new
#dictionary, name it 'eq_dict'. We are only interested in earthquakes that have a
#magnitude > 6. Print out the new dictionary.

list_eq = eq['features']
empty_list = []
eq_dict1 = {}
eq_dict = {'location': [], 'magnitude':[], 'latitude':[], 'longitude':[]}


 
for eqs in list_eq: 
   if eqs['properties']['mag'] > 6:
      eq_dict['location'].append(eqs['properties']['place'])
      eq_dict['magnitude'].append(eqs['properties']['mag'])
      eq_dict['latitude'].append(eqs['geometry']['coordinates'][1])
      eq_dict['longitude'].append(eqs['geometry']['coordinates'][2])
i = 0
while i <= 2:
   for k,j in eq_dict.items():
      print(k + ':', j[i])
   i += 1 
   print()
      
"""
for eq in list_eq:
   data_needed = [eq['properties']['place'], eq['properties']['mag'], eq['geometry']['coordinates'][1], eq['geometry']['coordinates'][0]]
   if eq['properties']['mag'] > 6:
      empty_list.append(data_needed)

for row in empty_list:
   eq_dict['location'].append(row[0])
   eq_dict['']

print(eq_dict)

"""





""""
for eq in list_eq:
   data_needed = [eq['properties']['place'], eq['properties']['mag'], eq['geometry']['coordinates'][1], eq['geometry']['coordinates'][0]]
   if eq['properties']['mag'] > 6:
      empty_list.append(data_needed)
for j in empty_list:
   print(type(j))


for dict in empty_list: 
   eq_dict['place'] = dict[0]
   eq_dict['magnitude'] = dict[1]
   eq_dict['latitude'] = dict[2]
   eq_dict['longitude'] = dict[3]
print(eq_dict)
"""

 
   


"""
for row in list_eq:
   if row['properties']['mag'] > 6:
      location = row['properties']['place']
      row.get('place', location)
      print(row)
"""





"""


list_eq = earthquakes['features']
eq_list = []
eq_dict = {}
i = 0 


for dict in list_eq:  
   if dict['properties']['mag'] > 6:
      eq_dict['place'] = dict['properties']['place']
      eq_dict['magnitude'] = dict['properties']['mag']
      eq_dict['latitude'] = dict['geometry']['coordinates'][1]
      eq_dict['longitude'] = dict['geometry']['coordinates'][0]
      eq_list.append(eq_dict)
      print(eq_list)





      eq_dict['magnitude'] = dict['properties']['mag']
      eq_dict['latitude'] = dict['geometry']['coordinates'][1]
      eq_dict['longitude'] = dict['geometry']['coordinates'][0]
      

      print(eq_list)
       #look into get method 

   """
    
