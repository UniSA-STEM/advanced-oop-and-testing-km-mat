'''
File: filename.py
Description: A brief description of this Python module.
Author: Karl Matillano
ID: 110336447 
Username: matky024
This is my own work as defined by the University's Academic Integrity Policy.
'''
from enclosure import Enclosure


class Staff:
    def __init__(self, name):
        self._name = name

    def __str__(self):
        return self._name

class Zookeper(Staff):
    def feed_animal(self, animal, enclosure):
        enclosure.dirtify(10)
        return f"{self._name} feeds {animal._name}. {animal.eat()}"

    def clean_enclosure(self, enclosure):
        return f"{self._name} cleans {enclosure._name}. {enclosure.clean()}"

    def health_check(self, animal):
        return f"{self._name} performs healthcheck on {animal._name}."
