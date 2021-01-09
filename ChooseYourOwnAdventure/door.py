'''
Project Name: Choose Your Own Adventure
Team Members: Albert Zou, Benjamin Knobloch, Kyle DiMaggio
Date: February 13
Task Description: Contains information about doors
'''

from item import Item
from player import Player
from room import Room
from PIL import Image
from infobox import Infobox
import sprites

class Door(Item):
    #   Instance variables
    __thisRoom = None
    __nextRoom = None
    __nextPosition = []
    __key = None
    __dark, __outside = False, False  # Refers to the room about to be entered, not the door itself
    __points = []
    __flashlight = None
    __battery = None

    def __init__(self, canvas, name, x, y, sizex, sizey, inventory, player, thisRoom, nextRoom = None, nextPosition = None, key = None, dark = False, outside = False, flashlight = None, battery = None):
        super().__init__(canvas, name, sprites.door, x, y, sizex, sizey, None, None, inventory, player, thisRoom)
        self.__thisRoom = thisRoom
        self.__nextRoom = nextRoom
        self.__nextPosition = nextPosition
        self.__key = key
        self.__dark = dark
        self.__outside = outside
        self.__flashlight = flashlight
        self.__battery = battery
    
    ''' When clicked, move the player into the next room.   '''
    def click(self, clickx, clicky, noneSelected):
        if not self._present or clickx < self._position[0] or clickx > self._position[0] + self._size[0] or clicky < self._position[1] or clicky > self._position[1] + self._size[1] or not self.canInteract():   return
        if self.__outside:
            Infobox(self._canvas, "If you go this way, Brian will get you!", 3000).show()
            return
        if self.__key != None and not self.__key.isInInventory() or self.__nextRoom == None:
            Infobox(self._canvas, "This door is locked!", 3000).show()
            return
        if self.__dark and not (self.__flashlight.isInInventory() and self.__battery.isInInventory()): #add "has flashlight"
            print(self.__flashlight.isInInventory())
            print(self.__battery.isInInventory())
            Infobox(self._canvas, "This room is too dark to enter!", 3000).show()
            return
        self._player.setPosition(self.__nextPosition[0], self.__nextPosition[1])
        self.__thisRoom.unloadRoom()
        #   Reloading the room fixes bugs with items being present when they shouldn't be
        self.__thisRoom.loadRoom()
        self.__thisRoom.unloadRoom()
        self.__nextRoom.loadRoom()
    
    ''' Outline the door.   '''
    def outline(self, sprite, colorChoice):
        outlinedSprite = Image.new(mode='RGBA', size=(sprite.size[0] + 3, sprite.size[1] + 3), color=(255, 255, 255, 0))            #   Create a new, slightly larger image.
        outlinedSprite.paste(self._restingSprite, box=(1, 1))                                                                #   Paste the item image onto the new image.
        for x in range(outlinedSprite.size[0]):
            outlinedSprite.putpixel((x, 0), colorChoice)
            outlinedSprite.putpixel((x, outlinedSprite.size[1] - 1), colorChoice)
        for y in range(outlinedSprite.size[1]):
            outlinedSprite.putpixel((0, y), colorChoice)
            outlinedSprite.putpixel((outlinedSprite.size[0] - 1, y), colorChoice)
        return outlinedSprite