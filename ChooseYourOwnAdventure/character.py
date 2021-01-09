'''
Project Name: Choose Your Own Adventure
Team Members: Albert Zou, Benjamin Knobloch, Kyle DiMaggio
Date: February 13
Task Description: Stores info about characters.
'''

from tkinter import *
import math

class Character:
    #   Instance variables
    _canvas = None
    _size = (0, 0)
    _position = [0, 0]
    __thisObject = None
    __positionChangeX = []
    __positionChangeY = []
    __image = None
    __orientation = [0, 0]
    _present = False
    populateOnLoad = True

    def __init__(self, canvas, sizeX, sizeY, posX, posY, orient, image, populateOnLoad = True):
        self._canvas = canvas
        self._size = (sizeX, sizeY)
        self._position = [posX, posY]
        self.__image = PhotoImage(file = image).zoom(4)
        self.__orientation = [math.cos(math.pi * orient / 2), math.sin(math.pi * orient / 2)]
        self._present = False
        self.populateOnLoad = populateOnLoad
        
    ''' Get the orientation.    '''
    def getOrientation(self):
        return self.__orientation
    
    ''' Change the orientation. '''
    def setOrientation(self, x = 0, y = 0):
        self.__orientation = [x, y]

    ''' Bring the character to the canvas.  '''
    def populate(self, x = '', y = ''):
        if x == '': x = self._position[0]
        if y == '': y = self._position[1]
        self._position = [x, y]
        self.__thisObject = self._canvas.create_image(x, y, image=self.__image)
        self._present = True

    ''' Remove the character from the canvas.   '''
    def depopulate(self):
        self._canvas.delete(self.__thisObject)
        self._present = False
        
    ''' Get canvas. '''
    def getCanvas(self):
        return self._canvas

    ''' Get size.   '''
    def getSize(self):
        return self._size
    
    ''' Get position.   '''
    def getPosition(self):
        return self._position
    
    ''' Change position.    '''
    def changePosition(self, x = 0, y = 0):
        self.__positionChangeX.append(x)
        self.__positionChangeY.append(y)
    
    ''' Set position.   '''
    def setPosition(self, x, y):
        self._position = [x, y]

    ''' Move the character. '''
    def move(self):
        self._position = [self._position[0] + sum(self.__positionChangeX), self._position[1] + sum(self.__positionChangeY)]
        self.__positionChangeX = []
        self.__positionChangeY = []
        self.__updateImage()

    ''' Update the image position.  '''
    def __updateImage(self):
        self._canvas.coords(self.__thisObject, [self._position[0], self._position[1]])

    def changeImage(self, newImage):
        self.__image = PhotoImage(file = newImage).zoom(4)

    ''' Update the sprite.  '''
    def changeSprite(self, sprite):
        self._canvas.delete(self.__thisObject)
        self.__thisObject = self._canvas.create_image(self._position[0], self._position[1], image=sprite)