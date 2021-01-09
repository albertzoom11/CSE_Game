'''
Project Name: Choose Your Own Adventure
Team Members: Albert Zou, Benjamin Knobloch, Kyle DiMaggio
Date: February 13
Task Description: Stores info about rooms.
'''

from tkinter import *
from wall import Wall
from item import Item
from character import Character
import sprites

class Room:
    #   Instance variables
    __walls = []
    __objects = []
    __image = None
    __canvas = None
    __inventory = None
    __thisRoom = None
    __enterMethod = None

    def __init__(self, walls, objects, image, canvas, inventory, enterMethod = None, titleCard = False, player = None):
        self.__walls = walls
        self.__objects = objects
        self.__image = PhotoImage(file = image).zoom(4)
        if player != None:
            player.enabled = False
        if titleCard:
            inventory.active(False)
            self.__image = PhotoImage(file = image).zoom(2)
        self.__canvas = canvas
        self.__inventory = inventory
        self.__enterMethod = enterMethod
    
    ''' Activate walls and bring objects onto canvas.   '''
    def loadRoom(self):
        self.__thisRoom = self.__canvas.create_image(0, 0, image = self.__image, anchor = NW)
        for wall in self.__walls:
            wall.isEnabled(True)
        for object in self.__objects:
            try:
                if object.populateOnLoad:
                    object.populate()
            except AttributeError:
                object.populate()
        self.__canvas.bind('<ButtonRelease-1>', self.click)
        if self.__enterMethod != None:
            self.__enterMethod()
        
    ''' Deactivate walls and remove objects from canvas.    '''
    def unloadRoom(self):
        self.__inventory.closeInventory()
        self.__canvas.delete(self.__thisRoom)
        for wall in self.__walls:
            wall.isEnabled(False)
        for object in self.__objects:
            object.depopulate()
            try:
                if object.isInInventory():
                    self.__objects.remove(object)
            except:
                pass
    
    def click(self, event):
        noneSelected = True
        self.__inventory.itemSelected = None
        for object in self.__inventory.items.values():
            if object.selected:
                noneSelected = False
                self.__inventory.itemSelected = object
                break
        for object in self.__objects:
            if object not in self.__inventory.items.values():
                try:
                    if object.click(event.x, event.y, noneSelected):
                        break
                except AttributeError:
                    pass
        for object in self.__inventory.items.values():
            try:
                if object.click(event.x, event.y, noneSelected):
                    break
            except AttributeError:
                pass

    ''' Get walls.  '''
    def getWalls(self):
        return self.__walls
    
    ''' Add wall.   '''
    def addWall(self, wall):
        self.__walls.append(wall)

    ''' Add object. '''
    def addObject(self, object):
        self.__objects.append(object)
    
    def removeObject(self, object):
        try:
            self.__objects.remove(object)
        except ValueError:
            pass
