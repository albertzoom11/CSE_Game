'''
Project Name: Choose Your Own Adventure
Team Members: Albert Zou, Benjamin Knobloch, Kyle DiMaggio
Date: February 13
Task Description: Stores info about items which cannot be picked up.
'''

from inventory import Inventory
from item import Item


class ImmobileItem(Item):

    __effect = None

    def __init__(self, canvas, name, restingSprite, x, y, sizex, sizey, effect, inventory, player, thisRoom, populateOnLoad = True):
        self.__effect = effect
        super().__init__(canvas, name, restingSprite, x, y, sizex, sizey, None, None, inventory, player, thisRoom, populateOnLoad)

    def click(self, clickx, clicky, noneSelected):
        if self._present and self.canInteract() and clickx > self._position[0] and clickx < self._position[0] + self._size[0] and clicky > self._position[1] and clicky < self._position[1] + self._size[1]:
            if not self._inventory.itemSelected and self.__effect != None:
                self.__effect(self)
            return True
        return False
        
    def updateSprite(self):
        if self._present:
            if (not self._couldBeInteractedWith) and self.canInteract():
                self._couldBeInteractedWith = True
                self.changeSprite(self._outlinedSprite)
            elif self._couldBeInteractedWith and (not self.canInteract()):
                self._couldBeInteractedWith = False
                self.changeSprite(self._restingSprite)