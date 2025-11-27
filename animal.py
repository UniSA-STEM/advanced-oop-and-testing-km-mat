'''
File: animal.py
Description: A brief description of this Python module.
Author: Karl Matillano
ID: 110336447 
Username: matky024
This is my own work as defined by the University's Academic Integrity Policy.
'''

from abc import ABC, abstractmethod
class Animal(ABC):
    def __init__(self, name, species, age, diet):
        self._name = name
        self._age = age
        self._species = species
        self._diet = diet
        self._health_record = []

    #animal actions
    @abstractmethod
    def make_sound(self):
        pass
    @abstractmethod
    def move(self):
        pass
    def eat(self):
        return f"{self._species} eats {self._diet}."

    def sleep(self):
        return f"{self._species} sleeps."

    def info(self):
        return f"{self._name} is a {self._species}, aged {self._age} and eats {self._diet}."

    def add_health_record(self, issue, severity, behavioral_concerns):
        record = HealthRecord(issue, severity, behavioral_concerns)
        self._health_record.append(record)
        return f"health record updated"

    def health_report(self):
        if not self._health_record:
            return f"No health records available."
        report = f"Health report for {self._name}:\n"
        for a in self._health_record:
            report += f"- {a}\n"
        return report

    def __str__(self):
        return f"{self._name, self._species, self._age, self._diet, self._health_record, self._behavioral_concerns }."

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

class HealthRecord:
    def __init__(self, issue, severity, behavioral_concerns):
        self._issue = issue
        self._severity = severity
        self._behavioral_concerns = behavioral_concerns

    def __str__(self):
        return f"Has {self._issue} that is {self._severity}. Behaviour is {self._behavioral_concerns}."
