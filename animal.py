'''
File: animal.py
Description: A brief description of this Python module.
Author: Karl Matillano
ID: 110336447 
Username: matky024
This is my own work as defined by the University's Academic Integrity Policy.
'''

class Animal:
    def __init__(self, name, species, age, diet):
        self._name = name
        self._age = age
        self._species = species
        self._diet = diet

class Bird(Animal):
    def make_sound(self):
        return f"{self._name} chirps."

class Mammal(Animal):
    def make_sound(self):
        return f"{self._name roars}"

class reptile(Animal):
    def make_sound(self):
        return f"{self._name hisses}"