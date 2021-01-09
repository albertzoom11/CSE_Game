'''
Project Name: Choose Your Own Adventure
Team Members: Albert Zou, Benjamin Knobloch, Kyle DiMaggio
Date: February 13
Task Description: Contains info about "warp zones", which move the player from room to room
'''

from wall import Wall

class Warp(Wall):
    #   Instance variables
    __thisRoom = None
    __nextRoom = None
    __nextWarp = None

    def __init__(self, x1, y1, x2, y2, thisRoom, nextRoom, wallSize = 8, canvas = None, nextWarp = None):
        super().__init__(x1, y1, x2, y2, wallSize = wallSize, canvas = canvas)
        self.__thisRoom = thisRoom
        self.__nextRoom = nextRoom
        self.__nextWarp = nextWarp
    
    ''' Set nextWarp.   '''
    def setWarp(self, nextWarp):
        self.__nextWarp = nextWarp
    
    ''' Move player to next room.   '''
    def removePlayer(self, player):
        if abs(self.findDistance(player)) < self._wallSize:
            if abs(self.getSlope()) >= 1:
                changeInY = player.getPosition()[1] - self.getPoints()[1][1]
                player.setPosition(self.__nextWarp.getPoints()[0][0] + changeInY / self.getSlope(), self.__nextWarp.getPoints()[0][1] + changeInY)
            else:
                changeInX = player.getPosition()[0] - self.getPoints()[1][0]
                player.setPosition(self.__nextWarp.getPoints()[0][0] + changeInX, self.__nextWarp.getPoints()[0][1] + self.getSlope() * changeInX)
            wall = Wall(self.__nextWarp.getPoints()[0][0], self.__nextWarp.getPoints()[0][1], self.__nextWarp.getPoints()[1][0], self.__nextWarp.getPoints()[1][1])
            wall.isEnabled(True)
            wall.removePlayer(player)
            player.move()
            wall.isEnabled(False)
            self.__thisRoom.unloadRoom()
            #   Reloading the room fixes bugs with items being present when they shouldn't be
            self.__thisRoom.loadRoom()
            self.__thisRoom.unloadRoom()
            self.__nextRoom.loadRoom()