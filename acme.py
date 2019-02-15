#!/usr/bin/env python
"""
Python Module to simulate Acme Corporation's stealability
"""
import numpy as np


class Product:
    """
    Acme Co. class to calculate things
    """

    def __init__(self, name, price=10, weight=20, flammability=0.5, identifier=np.random.uniform(1000000, 10000000)):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = identifier

    def stealability(self):
        if self.price / self.weight < 0.5:
            return "Not so stealable..."
        elif self.price / self.weight < 1.0:
            return "Kinda stealable."
        else:
            return "Very stealable!"

    def explode(self):
        coeff = self.flammability * self.weight
        if coeff < 10:
            return "...fizzle."
        elif coeff < 50:
            return "...boom!"
        else:
            return "...BABOOM!!"


class BoxingGlove(Product):

    def __init__(self, name):
        super(BoxingGlove, self).__init__(name)
        self.weight = 10

    def explode(self):
        return "...it's a glove."

    def punch(self):
        if self.weight < 5:
            return "That tickles."
        elif self.weight < 15:
            return "Hey that hurt!"
        else:
            return "OUCH!"
