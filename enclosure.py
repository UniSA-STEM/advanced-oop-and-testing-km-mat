'''
File: enclosure.py
Description: A brief description of this Python module.
Author: Karl Matillano
ID: 110336447 
Username: matky024
This is my own work as defined by the University's Academic Integrity Policy.
'''

class enclosure:
    def __init__(self, name, env_type, size, cleanliness, allowed_species):
        self._name = name
        self._env_type = env_type
        self._propertysize = size
        self.cleanliness = 100
        self._allowed_species = allowed_species
        self._animal = []