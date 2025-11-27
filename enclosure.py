'''
File: enclosure.py
Description: A brief description of this Python module.
Author: Karl Matillano
ID: 110336447 
Username: matky024
This is my own work as defined by the University's Academic Integrity Policy.
'''

class Enclosure:
    def __init__(self, name, env_type, size, allowed_species):
        self._name = name
        self._env_type = env_type
        self._propertysize = size
        self._cleanliness = 100
        self._allowed_species = allowed_species
        self._animal = []

    def add_animal(self, animal):
        if animal._species not in self._allowed_species:
            print(f"The {animal} is not allowed due to specie limitations   .")
            self._animal.append(animal)

    def remove_animal(self, animal):
        if animal in self._animal:
            self._animal.remove(animal)

    def clean(self):
        self._cleanliness = 100
        return f"{self._name} has been cleaned"

    @property
    def status(self):
        return{
            "name:": self._name,
            "environment": self._env_type,
            "property size": self._propertysize,
            "allowed species": self._allowed_species,
            "animals": [a._name for a in self._animal],
            "cleanliness": self._cleanliness,
        }