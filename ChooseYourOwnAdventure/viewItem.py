'''
Project Name: Choose Your Own Adventure
Team Members: Albert Zhou, Benjamin Knobloch, Kyle DiMaggio
Date: February 13
Task Description: Stores info about items which are pop up boxes.
'''

from inventory import Inventory
from item import Item


class ViewItem(Item):

    __effect = None

    def __init__(self, canvas, name, restingSprite, x, y, sizex, sizey, effect, inventory, player, thisRoom, populateOnLoad = False):
        super().__init__(canvas, name, restingSprite, x, y, sizex, sizey, None, None, inventory, player, thisRoom, populateOnLoad)
        self.__effect = effect

    def click(self, clickx, clicky, noneSelected):
        if self._present and clickx > self._position[0] and clickx < self._position[0] + self._size[0] and clicky > self._position[1] and clicky < self._position[1] + self._size[1]:
            if not self._inventory.itemSelected and self.__effect != None:
                self.__effect(self)
            return True
        return False
        
    def updateSprite(self):
        pass