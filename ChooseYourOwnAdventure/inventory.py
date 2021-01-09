'''
Contains the inventory.
'''

from tkinter import *
from PIL import Image, ImageTk
import sprites
from infobox import Infobox

class Inventory:
    __canvas = None
    __active = False
    __open = False
    itemSelected = False
    items = {}
    __box = None
    thisObject = None

    def __init__(self, canvas):
        self.__canvas = canvas
        self.__box = ImageTk.PhotoImage(Image.open(sprites.uiBoxes[2]))
        self.__canvas.bind('e', self.toggleInventory)

    ''' Set whether the inventory is active (i.e. if it is allowed to be opened at the moment)  '''
    def active(self, isItActive):
        self.__active = isItActive
        if self.__open:
            self.closeInventory()
    
    ''' Open or close the inventory.    '''
    def toggleInventory(self, event):
        if self.__active and not self.__open:
            self.openInventory()
        elif self.__open:
            self.closeInventory()

    ''' Close the inventory.    '''
    def closeInventory(self):
        if self.__open:
            self.__open = False
            self.__canvas.delete(self.thisObject)
            for item in self.items.values():
                item.destroyLabel()
                if item.selected:
                    item.displayNameBelow(False)

    '''Open the inventory.  '''
    def openInventory(self):
        if not self.__open:
            self.__open = True
            self.thisObject = self.__canvas.create_image(62, 800, image=self.__box, anchor=NW)
            placer = 80
            for item in self.items.values():
                item.populate(placer, 816)
                if item.selected:
                    item.displayNameBelow(True)
                placer += 100

    '''Add item to the items dictionary, with the item's name as the key and the item object as the value.    '''
    def addItem(self, item):
        infobox = Infobox(self.__canvas, "You got: " + item.name, 2500)
        infobox.show()
        reopen = False
        if self.__open:
            self.closeInventory()
            reopen = True
        self.items[item.name] = item
        sorted(self.items)
        if reopen:  self.openInventory()
        item.inInventory = True
    
    def itemRemoval(self, item):
        self.itemSelected = False
        reopen = False
        if self.__open:
            self.closeInventory()
            reopen = True
        try:
            del self.items[item.name]
        except KeyError:
            pass
        if reopen:  self.openInventory()

    ''' Remove an item from the inventory.  '''
    def removeItem(self, item):
        self.__canvas.after(8, self.itemRemoval, item)
        
    