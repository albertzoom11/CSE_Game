'''
Project Name: Choose Your Own Adventure
Team Members: Albert Zou, Benjamin Knobloch, Kyle DiMaggio
Date: February 13
Task Description: Stores info about walls.
'''

from tkinter import *
import math

class Wall:
    #   Instance variables
    __point1 = (0, 0)
    __point2 = (0, 0)
    __deltaX = 0
    __delatY = 0
    __slope = 0
    __normalAngle = 0
    _enabled = False
    _wallSize = 0
    __canvas = None
    __enterMethod = None

    def __init__(self, x1, y1, x2, y2, wallSize = 32, canvas = None, enterMethod = None):
        self.__point1 = (x1, y1)
        self.__point2 = (x2, y2)
        self.__deltaX = x2 -  x1
        self.__deltaY = y2 - y1
        if self.__deltaX != 0:
            self.__slope = float(self.__deltaY) / float(self.__deltaX)
        else:
            self.__slope = float(self.__deltaY) * math.inf
        self.__normalAngle = (math.atan2(float(self.__deltaY), float(self.__deltaX)) + math.pi / 2) % (2 * math.pi) # Order of points changes normal vector
        self._enabled = False
        self._wallSize = wallSize
        self.__canvas = canvas
        self.__enterMethod = enterMethod

    ''' Find the players distance from the wall.    '''
    def findDistance(self, player):
        if not self._enabled: return math.inf
        if abs(self.__slope) >= 1:  # Normal vector points mostly in the x direction
            if player.getPosition()[1] < min(self.__point1[1], self.__point2[1]) or max(self.__point1[1], self.__point2[1]) < player.getPosition()[1]: return math.inf
            return player.getPosition()[0] - self.__point1[0] - (player.getPosition()[1] - self.__point1[1]) / self.__slope
        else:   # Normal vector points mostly in the y direction
            if player.getPosition()[0] < min(self.__point1[0], self.__point2[0]) or max(self.__point1[0], self.__point2[0]) < player.getPosition()[0]: return math.inf
            return player.getPosition()[1] - self.__point1[1] - (player.getPosition()[0] - self.__point1[0]) * self.__slope
            
    ''' Push the player out of the hitbox.  '''
    def removePlayer(self, player):
        if abs(self.findDistance(player)) < self._wallSize:
            if self.__enterMethod != None:
                self.__enterMethod()
            if abs(self.__slope) >= 1:  # Normal vector points mostly in the x direction
                player.changePosition(x = math.cos(self.__normalAngle) * self._wallSize - abs(math.cos(self.__normalAngle)) * self.findDistance(player), y = math.sin(self.__normalAngle) * (self._wallSize - abs(self.findDistance(player))))
            else:   # Normal vector points mostly in the y direction
                player.changePosition(x = math.cos(self.__normalAngle) * (self._wallSize - abs(self.findDistance(player))), y = math.sin(self.__normalAngle) * self._wallSize - abs(math.sin(self.__normalAngle)) * self.findDistance(player))

    ''' Set if the wall is enabled or not.  '''
    def isEnabled(self, enabled):
        self._enabled = enabled
        if enabled and self.__canvas != None:
            self.__canvas.create_line(self.__point1[0], self.__point1[1], self.__point2[0], self.__point2[1], fill = 'green', width = self._wallSize)
            
    
    ''' Get the points of the wall. '''
    def getPoints(self):
        return [self.__point1, self.__point2]

    ''' Get slope.  '''
    def getSlope(self):
        return self.__slope

    def setCanvas(self, canvas):
        self.__canvas = canvas