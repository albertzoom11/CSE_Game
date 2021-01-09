'''
Project Name: Choose Your Own Adventure
Team Members: Albert Zou, Benjamin Knobloch, Kyle DiMaggio
Date: February 13
Task Description: Stores info about potions.
'''

from tkinter import *
from inventory import Inventory
from item import Item

class Potion(Item):
    #   Instance variables
    __ingredient = ""
    __effect = ""

    def __init__(self, canvas, name, restingSprite, size, inventory, ingredient, effect):
        super().__init__(canvas, name, restingSprite, size, inventory)
        self.__ingredient = ingredient
        self.__effect = effect
    
    ''' Get ingredient. '''
    def getIngredient(self):
        return self.__ingredient
    
    ''' Get effect. '''
    def getEffect(self):
        return self.__effect
