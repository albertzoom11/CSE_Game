'''
Project Name: Choose Your Own Adventure
Team Members: Albert Zou, Benjamin Knobloch, Kyle DiMaggio
Date: February 13
Task Description: Stores info about items.
'''

from tkinter import *
from PIL import Image, ImageTk
from inventory import Inventory
from infobox import Infobox
import math

class Item:
    _canvas = None                 #   The root canvas
    name = ""                       #   The name of the item
    inInventory = False
    selected = False
    __thisObject = None             #   The item canvas image object
    _position = []                         #   x and y coordinates of the object
    _inventory = None              #   The associated inventory
    _player = None                 #   The associated player
    __displayItemName = []          #   The tkinter text object for the item's name
    _size = []                     #   The size of the item
    _present = False               #   Is the item currently onscreen?
    _couldBeInteractedWith = False
    effect = None
    objectsOfInteraction = []
    room = None
    populateOnLoad = True
    
    #   Sprites
    _restingSprite = None
    _outlinedSprite = None
    _inventoryRestingSprite = None
    _inventorySelectedSprite = None

    def __init__(self, canvas, name, restingSprite, x, y, sizex, sizey, effect, objectsOfInteraction, inventory, player, thisRoom, populateOnLoad=True):
        self._canvas = canvas
        self.name = name
        self.effect = effect
        self.objectsOfInteraction = objectsOfInteraction
        self._inventory = inventory
        self._player = player
        self.room = thisRoom
        self.populateOnLoad = populateOnLoad
        self._restingSprite = Image.open(restingSprite)
        self._outlinedSprite = self.outline(self._restingSprite, (255, 255, 0, 255))
        self._inventorySelectedSprite = self.outline(self._restingSprite, (0, 255, 0, 255))
        self._inventoryRestingSprite = ImageTk.PhotoImage(self._restingSprite.resize((64, 64), resample=Image.NEAREST))
        self._inventorySelectedSprite = ImageTk.PhotoImage(self._inventorySelectedSprite.resize((64, 64), resample = Image.NEAREST))
        self._restingSprite = ImageTk.PhotoImage(self._restingSprite.resize((sizex, sizey), resample=Image.NEAREST))
        self._outlinedSprite = ImageTk.PhotoImage(self._outlinedSprite.resize((sizex, sizey), resample=Image.NEAREST))
        self._position = [x, y]
        self._size = [sizex, sizey]
        thisRoom.addObject(self)
    
    ''' Create an outlined version of the item to be used when it is selected. Outline color is provided.   '''
    def outline(self, sprite, colorChoice):
        outlinedSprite = Image.new(mode='RGBA', size=(sprite.size[0] + 3, sprite.size[1] + 3), color=(255, 255, 255, 0))            #   Create a new, slightly larger image.
        outlinedSprite.paste(sprite, box=(1, 1))                                                                      #   Paste the item image onto the new image.
        ''' Iterate through the image, adding the desired color whenever there is a border between the item and transparent pixels. '''
        for x in range(outlinedSprite.size[0] - 1):
            for y in range(outlinedSprite.size[1] - 1):
                r, g, b, a = outlinedSprite.getpixel((x, y))
                r1, g1, b1, a1, = outlinedSprite.getpixel((x, y + 1))
                r2, g2, b2, a2 = outlinedSprite.getpixel((x, y - 1))
                r3, g3, b3, a3 = outlinedSprite.getpixel((x + 1, y))
                r4, g4, b4, a4 = outlinedSprite.getpixel((x - 1, y))
                if (a == 0) and ((a1 == 255 and (r1, g1, b1, a1) != colorChoice) or (a2 == 255 and (r2, g2, b2, a2) != colorChoice) or (a3 == 255 and (r3, g3, b3, a3) != colorChoice) or (a4 == 255 and (r4, g4, b4, a4) != colorChoice)):
                    outlinedSprite.putpixel((x, y), colorChoice)
        return outlinedSprite
    
    ''' Place the image on the canvas at the provided coordinates.  '''
    def populate(self, x = '', y = ''):
        if x == '': x = self._position[0]
        if y == '': y = self._position[1]
        if self.selected:
            self.__thisObject = self._canvas.create_image(x, y, image=self._inventorySelectedSprite, anchor=NW)
        elif self.inInventory:
            self.__thisObject = self._canvas.create_image(x, y, image=self._inventoryRestingSprite, anchor=NW)
        else:
            self.__thisObject = self._canvas.create_image(x, y, image=self._restingSprite, anchor=NW)
        self._position[0] = x
        self._position[1] = y
        self._present = True
        # self.__thisObject.bind('<Leave>', self.dehighlight)
        # self.__thisObject.bind('<ButtonRelease-1>', self.click)

    ''' Remove the image from the canvas'''
    def depopulate(self):
        self._present = False
        self.selected = False
        self._canvas.delete(self.__thisObject)
        for displayItem in self.__displayItemName:
                self._canvas.delete(displayItem)

    ''' If the canvas is clicked within the item's edges, the item is onscreen, and the player is nearby, collect / highlight the item. '''
    def click(self, clickx, clicky, noneSelected):
        if self._present:
            if self.inInventory and clickx > self._position[0] and clickx < self._position[0] + 64 and clicky > self._position[1] and clicky < self._position[1] + 64:
                if self.selected:                                       #   If the item is currently selected, unselect it.
                    self.displayNameBelow(False)
                    self.changeSprite(self._inventoryRestingSprite)
                    self.selected = False
                elif noneSelected:                                      #   If the item is currently unselected, select it.
                    self.displayNameBelow(True)
                    self.changeSprite(self._inventorySelectedSprite)
                    self.selected = True
                return True
            elif noneSelected and clickx > self._position[0] and clickx < self._position[0] + self._size[0] and clicky > self._position[1] and clicky < self._position[1] + self._size[1] and self.canInteract():                                #   If the item is not currently in the inventory, then it must be collected and added to the inventory.
                self.inInventory = True
                self._present = False
                self._couldBeInteractedWith = False
                self._canvas.delete(self.__thisObject)
                self._inventory.addItem(self)
                return True
        if self.selected and self.effect != None and not self.effect(self, self.objectsOfInteraction, clickx, clicky):
            infobox = Infobox(self._canvas, "You can't do that.", 1500)
            infobox.show()
            return True
        return False
    
    ''' Get inInventory '''
    def isInInventory(self):
        return self.inInventory

    ''' Destroy the canvas image object (make the item disappear).  '''
    def destroyLabel(self):
        self._canvas.delete(self.__thisObject)
        self._present = False

    ''' Destroy the canvas image object and replace it with a new image object with a different sprite. '''
    def changeSprite(self, newSprite):
        if self._present:
            self._canvas.delete(self.__thisObject)
            self.__thisObject = self._canvas.create_image(self._position[0], self._position[1], image=newSprite, anchor=NW)

    ''' If display=True, create a new text object to show the item's name when the item is selected in the inventory. If display=False, delete the text object. '''  
    def displayNameBelow(self, display):
        if display:
            self.__displayItemName.append(self._canvas.create_text(513, 921, text=self.name, fill="white", font=("Comic Sans MS", 19, "bold", 'italic')))
            self.__displayItemName.append(self._canvas.create_text(511, 919, text=self.name, fill="black", font=("Comic Sans MS", 19, "bold", 'italic')))
        else:
            for displayItem in self.__displayItemName:
                self._canvas.delete(displayItem)

    ''' Returns True if the player is close enough to the object to interact with it.   '''
    def canInteract(self):
        player_coords = self._player.getPosition()
        if int(math.sqrt(abs((self._position[0] + (self._size[0] // 2)) - player_coords[0]) ** 2 + abs((self._position[1] + (self._size[1] // 2)) - player_coords[1]) ** 2)) < 100:
            return True
        return False

    ''' Changes the item's sprite if the player moves into or out of range of the object.    '''
    def updateSprite(self):
        if self._present and not self.inInventory:
            if (not self._couldBeInteractedWith) and self.canInteract():
                self._couldBeInteractedWith = True
                self.changeSprite(self._outlinedSprite)
            elif self._couldBeInteractedWith and (not self.canInteract()):
                self._couldBeInteractedWith = False
                self.changeSprite(self._restingSprite)
