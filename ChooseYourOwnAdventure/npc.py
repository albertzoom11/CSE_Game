'''
Project Name: Choose Your Own Adventure
Team Members: Albert Zou, Benjamin Knobloch, Kyle DiMaggio
Date: February 13
Task Description: Stores info about NPCs.
'''

import math
from tkinter import *
from dialogue import Dialogue
from character import Character
from item import Item
from PIL import Image, ImageTk

class Npc(Character, Item):
    __name = ''
    __icon = None
    speakMode = 0                       #   speakMode=0 means the character is not speaking. speakMode=1 means the character's sprite needs to be updated. speakMode=2 means the character is currently speaking.
    __doneSpeaking = False
    __produceSpeech = None
    __inventory = None
    __room = None
    _player = None
    __sprites0 = None
    __sprites1 = None
    __sprites2 = None
    __sprites3 = None
    
    def __init__(self, canvas, sizeX, sizeY, posX, posY, orient, files, name, icon, produceSpeech, inventory, player, room):
        super().__init__(canvas, sizeX, sizeY, posX, posY, orient, files[0])
        self.__sprites0 = (PhotoImage(file = files[0]).zoom(4))
        self.__sprites1 = (PhotoImage(file = files[1]).zoom(4))
        self.__sprites2 = (PhotoImage(file = files[2]).zoom(4))
        self.__sprites3 = (PhotoImage(file = files[3]).zoom(4))
        self.__name = name
        self.__icon = icon
        self.__produceSpeech = produceSpeech
        self.__inventory = inventory
        self._player = player
        self.__room = room
        self._restingSprite = Image.open(files[0])
        self._outlinedSprite = self.outline(self._restingSprite, (255, 255, 0, 255))
        self._restingSprite = ImageTk.PhotoImage(self._restingSprite.resize((sizeX, sizeY), resample = Image.NEAREST))
        self._outlinedSprite = ImageTk.PhotoImage(self._outlinedSprite.resize((sizeX, sizeY), resample = Image.NEAREST))
        room.addObject(self)

    ''' Load in the character.  '''
    def populate(self, x = '', y = ''):
        super().populate(x, y)

    ''' If the player clicks on the NPC and does not have an item selected, make the NPC speak. '''
    def click(self, clickx, clicky, noneSelected):
        if self.speakMode == 0 and self._present and clickx > self._position[0] - self._size[0] / 2 and clickx < self._position[0] + self._size[0] / 2 and clicky > self._position[1] - self._size[1] / 2 and clicky < self._position[1] + self._size[1] / 2:
            if not self.__inventory.itemSelected:
                self.speak()
            return True
        return False

    ''' If the NPC is beginning to speak, turn the NPC to the player. Otherwise, highlight the NPC if it is in range of the player.'''
    def updateSprite(self):
        if self.speakMode == 1:
            self.speakMode = 2
            self._couldBeInteractedWith = False
            self.changeSprite(self.turnToPlayer())
        if self._present and self.speakMode == 0:
            if (not self._couldBeInteractedWith) and self.canInteract():
                self._couldBeInteractedWith = True
                self.changeSprite(self._outlinedSprite)
            elif self._couldBeInteractedWith and (not self.canInteract()):
                self._couldBeInteractedWith = False
                self.changeSprite(self.__sprites0)
    
    ''' Create dialogue given the produceSpeech() function passed into __init__().'''
    def speak(self):
        self.speakMode = 1
        ''' Write code for speaking.    '''
        speech = Dialogue(self._canvas, self.__produceSpeech(), self.__name, self.__icon, self.__room, self, self._player, self.__inventory)
        speech.show()

    ''' Choose a "facing" sprite depending on the player's position relative to the NPC.    '''
    def turnToPlayer(self):
        player_coords = self._player.getPosition()
        horiDistance = self._position[0] - player_coords[0]
        vertiDistance = self._position[1] - player_coords[1]
        if abs(horiDistance) >= abs(vertiDistance):
            if horiDistance > 0:
                return self.__sprites1
            return self.__sprites3
        if vertiDistance > 0:
            return self.__sprites2
        return self.__sprites0