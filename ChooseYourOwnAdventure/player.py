'''
Project Name: Choose Your Own Adventure
Team Members: Albert Zou, Benjamin Knobloch, Kyle DiMaggio
Date: February 13
Task Description: Stores information about the player.
'''

from tkinter import *
from character import Character
from PIL import Image
import math

class Player(Character):
    __speed = 0
    __cycler = 0
    __stepLeft = True
    __isMoving = False
    __inventory = None
    enabled = True

    #   Directions
    __xDir = 0
    __yDir = 0

    #   Sprites
    __sprites = []
    
    #   Get x and y
    def getXDir(self):
        return self.__xDir
    def getYDir(self):
        return self.__yDir

    #   Get speed
    def getSpeed(self):
        speed = self.__speed - len(self.__inventory.items)
        return speed

    #   Start or stop movement with direction variables (movement done in game.py)
    def __start(self, event):
        if not self.enabled:
            self.__yDir = 0
            self.__xDir = 0
            return
        if event.char == 'w': self.__yDir = -1
        if event.char == 'a': self.__xDir = -1
        if event.char == 's': self.__yDir = 1
        if event.char == 'd': self.__xDir = 1
    def __stop(self, event):
        if event.char == 'w' or event.char == 's': self.__yDir = 0
        if event.char == 'a' or event.char == 'd' : self.__xDir = 0

    #   Initialization function
    def __init__(self, canvas, sizeX, sizeY, posX, posY, orient, files, speed, inventory):
        self.enabled = True
        super().__init__(canvas, sizeX, sizeY, posX, posY, orient, files[0])
        for sprite in files:
            self.__sprites.append(PhotoImage(file = sprite).zoom(4))
        self.__speed = speed
        self.__inventory = inventory

    def populate(self, x = '', y = ''):
        super().populate(x, y)
        self._canvas.bind("<KeyPress>", self.__start)
        self._canvas.bind("<KeyRelease>", self.__stop)

    def __moving(self):
        if self.__xDir != 0 or self.__yDir != 0:
            return True
        return False

    ''' Change the sprite to match the motion of the player.    '''
    def updateSprite(self, force = False):
        if self.__moving():                                                             #   If player is moving, change sprite to a 'stepping' sprite
            self.__isMoving = True
            self.__cycler += 1                                                          #   Cycler tracks how long it has been since the last step by the avatar.
            if self.__cycler == 15:                                                     #   If cycler=15, restart the cycle and change the sprite.
                self.__cycler = 0
                self.__stepLeft = not self.__stepLeft                                   #   Change the step to the opposite step of the last cycle.
                if self.__xDir == 1:
                    if self.__stepLeft: super().changeSprite(self.__sprites[10])
                    else:               super().changeSprite(self.__sprites[11])
                elif self.__xDir == -1:
                    if self.__stepLeft: super().changeSprite(self.__sprites[4])
                    else:               super().changeSprite(self.__sprites[5])
                elif self.__yDir == 1:
                    if self.__stepLeft: super().changeSprite(self.__sprites[1])
                    else:               super().changeSprite(self.__sprites[2])
                    self._orientation = 0
                elif self.__yDir == -1:
                    if self.__stepLeft: super().changeSprite(self.__sprites[7])
                    else:               super().changeSprite(self.__sprites[8])
                self.setOrientation([self.__xDir, self.__yDir])
        elif self.__isMoving or force:
            self.__isMoving = False                                                                           #   If the player is not moving, change sprite to an 'idle' sprite.
            if self.getOrientation() == [0, 1]:
                self.changeSprite(self.__sprites[0])
            elif self.getOrientation() == [-1, 0]:
                self.changeSprite(self.__sprites[3])
            elif self.getOrientation() == [0, -1]:
                self.changeSprite(self.__sprites[6])
            elif self.getOrientation() == [1, 0]:
                self.changeSprite(self.__sprites[9])

    def changeFiles(self, files):
        for file in range(len(files)):
            self.__sprites[file] = PhotoImage(file = files[file]).zoom(4)
        super().changeImage(files[0])