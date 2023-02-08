person = {}
person["fname"] = "Joe"
person["lname"] = "Fonebone"
person["age"] = 51
person["spouse"] = "Edna"
person["children"] = ["Ralph", "Betty", "Joey"]
person["pets"] = {"dog": "Fido", "cat": "Sox"}




#Name of the second child 
print(person["children"][1])


#Name of the cat 

print(person['pets']['dog'])
print(person["pets"].keys())
#List each child 

for i in person['children']:
    print(i)

#print out the pets in this format, 
#type of pet:dog, name of pet: fido

for i,j in person['pets'].items():
    print(f"Type of pet: {i} name of pet: {j}")