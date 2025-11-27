'''
File: animal.py
Description: A brief description of this Python module.
Author: Karl Matillano
ID: 110336447 
Username: matky024
This is my own work as defined by the University's Academic Integrity Policy.
'''
from enclosure import Enclosure


class Animal:
    def __init__(self, name, species, age, diet):
        self._name = name
        self._age = age
        self._species = species
        self._diet = diet

    #animal actions
    def make_sound(self):
        return f"{self._species} makes a sound."

    def eat(self):
        return f"{self._species} eats {self._diet}."

    def sleep(self):
        return f"{self._species} sleeps."

    def move(self):
        return f"{self._name} moves."

    def info(self):
        return f"{self._name} is a {self._species}, aged {self._age} and eats {self._diet}."

class Bird(Animal):
    def make_sound(self):
        return f"{self._name} chirps."

    def move(self):
        return f"{self._name} flies around"

class Mammal(Animal):
    def make_sound(self):
        return f"{self._name} roars"

    def move(self):
        return f"{self._name} paces around."

class Reptile(Animal):
    def make_sound(self):
        return f"{self._name} hisses"
    def move(self):
        return f"{self._name} slithers."

class Aquatic(Animal):
    def make_sound(self):
        return f"{self._name} bubbles"
    def move(self):
        return f"{self._name} swims."