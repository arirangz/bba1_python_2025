import pickle

persons = [
    {"name": "John", "age": 30},
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 24},
]

with open("persons.pkl", "wb") as file:
    pickle.dump(persons, file)