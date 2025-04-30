import pickle

with open("persons.pkl", "rb") as file:
    persons = pickle.load(file)
    
if persons:
    for person in persons:
        print(person["name"])
        