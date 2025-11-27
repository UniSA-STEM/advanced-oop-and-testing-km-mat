'''
File: main.py
Description: A brief description of this Python module.
Author: Karl Matillano
ID: 110336447 
Username: matky024
This is my own work as defined by the University's Academic Integrity Policy.
'''

from animal import Animal, Mammal, Reptile, Bird, Aquatic
from enclosure import Enclosure
from staff import Staff

def main():

    #create animals
    lion = Mammal("Mufasa","Lion", 5, "raw meat")
    parrot = Bird("Zazu","Parrot",1, "seeds")
    anaconda = Reptile("Voldmort","Snake",100,"Harry Potter")
    fish = Aquatic("Nemo", "Fish",1, "dory")

    print(lion.make_sound())
    print(lion.move())

    print(parrot.make_sound())
    print(parrot.move())

    print(anaconda.make_sound())
    print(anaconda.move())

    print(fish.make_sound())
    print(fish.move())

    #create enclosures
    savannah = Enclosure("Savannah 1", "Savannah", 200, ["Lion"]
    swamp = Enclosure("Swamp 1", "Swamp", 200, ["Snakes"])
    treetop = Enclosure("Treetop 1", "Treetop", 50, ["bird"])
    aquarium = Enclosure("Aquarium 1", "Aquarium", 20, ["Fish"])

print(lion.make_sound())