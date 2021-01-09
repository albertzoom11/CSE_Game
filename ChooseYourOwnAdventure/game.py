'''
Project Name: Choose Your Own Adventure
Team Members: Albert Zou, Benjamin Knobloch, Kyle DiMaggio
Date: February 13
Task Description: Main file to run the game
'''

from tkinter import *
from character import Character
from player import Player
from dialogue import Dialogue
from inventory import Inventory
from writing import Writing
from wall import Wall
from warp import Warp
import sprites
from item import Item
from immobileitem import ImmobileItem
from viewItem import ViewItem
from npc import Npc
from room import Room
from door import Door
from infobox import Infobox
import sprites
from random import choice

#   Create canvas
root = Tk()
canvas = Canvas(root, width = 1024, height =1024, bg='white')
canvas.grid()
canvas.focus_set()

#   Player
inventory = Inventory(canvas)
player = Player(canvas, 64, 96, 475, 510, 1, sprites.boyAvatars, 8, inventory)
writeObject = Writing('playerName', 'male')

#   Rooms
nexus = Room([], [player], sprites.rooms[0], canvas, inventory)
freshmanHallway = Room([], [player], sprites.rooms[1], canvas, inventory)
freshmanSophomoreHallway = Room([], [player], sprites.rooms[2], canvas, inventory)
sophomoreJuniorHallway = Room([], [player], sprites.rooms[3], canvas, inventory)
juniorHallway = Room([], [player], sprites.rooms[4], canvas, inventory)
juniorNexus = Room([], [player], sprites.rooms[5], canvas, inventory)
boysBathroom = Room([], [player], sprites.rooms[6], canvas, inventory)
courtyard = Room([], [player], sprites.rooms[7], canvas, inventory)
mathRoom = Room([], [player], sprites.rooms[8], canvas, inventory)
chemRoom = Room([], [player], sprites.rooms[9], canvas, inventory)
stairwellEnter = False
def onStairwellEnter():
    global stairwellEnter
    stairwellEnter = True
stairwell = Room([], [player], sprites.rooms[10], canvas, inventory, onStairwellEnter)
cseRoom = Room([], [player], sprites.rooms[11], canvas, inventory)
outside = Room([], [player], sprites.rooms[12], canvas, inventory)
darkRoom = Room([], [], sprites.rooms[13], canvas, inventory, player = player)

#   Walls
nexusWalls = [Warp(348, -48, 668, -48, nexus, juniorNexus),
                        Wall(668, -48, 668, 444),
                        Wall(668, 444, 876, 444),
                        Wall(876, 444, 876, 592),
                        Wall(876, 592, 748, 592),
                        Wall(748, 592, 748, 896),
                        Wall(748, 896, 904, 896),
                        Wall(904, 896, 904, 1008),
                        Wall(904, 1008, 348, 1008),
                        Wall(348, 1008, 348, 868),
                        Wall(348, 868, 0, 868),
                        Warp(0, 868, 0, 500, nexus, freshmanHallway),
                        Wall(0, 500, 348, 500),
                        Wall(348, 500, 348, -48)]
for wall in nexusWalls:
    nexus.addWall(wall)
freshmanWalls = [Warp(1024, 500, 1024, 868, freshmanHallway, nexus, nextWarp = nexusWalls[11]),
                            Wall(1024, 868, 988, 868),
                            Wall(988, 868, 988, 932),
                            Wall(988, 932, 576, 932),
                            Wall(576, 932, 576, 868),
                            Wall(576, 868, 0, 868),
                            Warp(0, 868, 0, 500, freshmanHallway, freshmanSophomoreHallway),
                            Wall(0, 500, 192, 500),
                            Wall(192, 500, 192, 440),
                            Wall(192, 440, 600, 440),
                            Wall(600, 440, 600, 500),
                            Wall(600, 500, 1024, 500)]
nexusWalls[11].setWarp(freshmanWalls[0])
for wall in freshmanWalls:
    freshmanHallway.addWall(wall)
freshmanSophomoreWalls = [Warp(1024, 500, 1024, 868, freshmanSophomoreHallway, freshmanHallway, nextWarp = freshmanWalls[6]),
                                            Wall(1024, 868, 464, 868),
                                            Wall(464, 868, 464, 1008),
                                            Wall(464, 1008, 240, 1008),
                                            Wall(240, 1008, 240, 972),
                                            Wall(240, 972, 136, 868),
                                            Wall(136, 868, 36, 868),
                                            Wall(36, 868, 36, 500),
                                            Wall(36, 500, 144, 500),
                                            Wall(144, 500, 144, -48),
                                            Warp(144, -48, 464, -48, freshmanSophomoreHallway, sophomoreJuniorHallway),
                                            Wall(464, -48, 464, 500),
                                            Wall(464, 500, 1024, 500)]
freshmanWalls[6].setWarp(freshmanSophomoreWalls[0])
for wall in freshmanSophomoreWalls:
    freshmanSophomoreHallway.addWall(wall)
sophomoreJuniorWalls = [Warp(464, 1008, 144, 1008, sophomoreJuniorHallway, freshmanSophomoreHallway, nextWarp = freshmanSophomoreWalls[10]),
                                        Wall(144, 1008, 144, 656),
                                        Wall(144, 656, 48, 656),
                                        Wall(48, 656, 48, 292),
                                        Wall(48, 292, 1024, 292),
                                        Warp(1024, 292, 1024, 656, sophomoreJuniorHallway, juniorHallway),
                                        Wall(1024, 656, 464, 656),
                                        Wall(464, 656, 464, 1008)]
freshmanSophomoreWalls[10].setWarp(sophomoreJuniorWalls[0])
for wall in sophomoreJuniorWalls:
    sophomoreJuniorHallway.addWall(wall)
juniorWalls = [Warp(4, 656, 4, 288, juniorHallway, sophomoreJuniorHallway, nextWarp = sophomoreJuniorWalls[5]),
                        Wall(4, 288, 44, 288),
                        Wall(44, 288, 44, 228),
                        Wall(44, 228, 452, 228),
                        Wall(452, 228, 452, 288),
                        Wall(452, 288, 820, 288),
                        Wall(820, 288, 1024, 476),
                        Warp(1024, 476, 1024, 960, juniorHallway, juniorNexus),
                        Wall(1024, 960, 724, 656),
                        Wall(724, 656, 452, 656),
                        Wall(452, 656, 452, 720),
                        Wall(452, 720, 44, 720),
                        Wall(44, 720, 44, 656),
                        Wall(44, 656, 1, 656)]
sophomoreJuniorWalls[5].setWarp(juniorWalls[0])
for wall in juniorWalls:
    juniorHallway.addWall(wall)
juniorNexusWalls = [Warp(4, 620, 4, 136, juniorNexus, juniorHallway, nextWarp = juniorWalls[7]),
                                Wall(4, 136, 464, 592),
                                Wall(464, 592, 976, 592),
                                Wall(976, 592, 976, 940),
                                Wall(976, 940, 672, 940),
                                Wall(672, 940, 672, 1008),
                                Warp(672, 1008, 348, 1008, juniorNexus, nexus, nextWarp = nexusWalls[0]),
                                Wall(348, 1008, 348, 960),
                                Wall(348, 960, 4, 620)]
juniorWalls[7].setWarp(juniorNexusWalls[0])
nexusWalls[0].setWarp(juniorNexusWalls[6])
for wall in juniorNexusWalls:
    juniorNexus.addWall(wall)
boysBathroomWalls = [Wall(104, 156, 544, 156),
                                    Wall(544, 156, 544, 280),
                                    Wall(544, 280, 624, 360),
                                    Wall(624, 360, 988, 360),
                                    Wall(988, 360, 988, 524),
                                    Wall(988, 524, 900, 524),
                                    Wall(900, 524, 900, 624),
                                    Wall(900, 624, 632, 624),
                                    Wall(632, 624, 632, 480),
                                    Wall(632, 480, 544, 396),
                                    Wall(544, 396, 544, 440),
                                    Wall(544, 440, 624, 520),
                                    Wall(624, 520, 624, 624),
                                    Wall(624, 624, 524, 624),
                                    Wall(524, 624, 524, 672),
                                    Wall(524, 672, 988, 672),
                                    Wall(988, 672, 988, 944),
                                    Wall(988, 944, 432, 944),
                                    Wall(432, 944, 432, 884),
                                    Wall(432, 884, 336, 884),
                                    Wall(336, 884, 336, 944),
                                    Wall(336, 944, 180, 944),
                                    Wall(180, 944, 180, 572),
                                    Wall(180, 572, 104, 572),
                                    Wall(104, 572, 104, 156)]
for wall in boysBathroomWalls:
    boysBathroom.addWall(wall)
courtyardWalls = [Wall(36, 212, 548, 212),
                            Wall(548, 212, 696, 360),
                            Wall(696, 360, 992, 360),
                            Wall(992, 360, 992, 768),
                            Wall(992, 768, 36, 768),
                            Wall(36, 768, 36, 524),
                            Wall(36, 524, 196, 524),
                            Wall(196, 524, 196, 432),
                            Wall(196, 432, 36, 432),
                            Wall(36, 432, 36, 212),
                            Wall(432, 344, 300, 344),
                            Wall(432, 392, 432, 344),
                            Wall(300, 392, 432, 392),
                            Wall(300, 344, 300, 392),
                            Wall(432, 628, 300, 628),
                            Wall(432, 676, 432, 628),
                            Wall(300, 676, 432, 676),
                            Wall(300, 628, 300, 676)]
for wall in courtyardWalls:
    courtyard.addWall(wall)
mathWalls = [Wall(80, 72, 946, 72),
                            Wall(946, 72, 812, 264),
                            Wall(812, 264, 944, 264),
                            Wall(944, 264, 944, 536),
                            Wall(944, 536, 812, 536),
                            Wall(812, 536, 420, 724),
                            Wall(420, 710, 420, 738),
                            Wall(420, 724, 944, 724),
                            Wall(944, 724, 944, 948),
                            Wall(944, 948, 112, 948),
                            Wall(112, 948, 112, 436)]
for wall in mathWalls:
    mathRoom.addWall(wall)
chemWalls = [Wall(668, 112, 740, 188),
                    Wall(740, 188, 796, 188),
                    Wall(796, 188, 968, 412),
                    Wall(968, 412, 896, 412),
                    Wall(896, 412, 896, 560),
                    Wall(896, 560, 888, 560),
                    Wall(888, 560, 888, 656),
                    Wall(888, 656, 986, 656),
                    Wall(986, 656, 986, 704),
                    Wall(986, 704, 704, 968),
                    Wall(704, 968, 704, 924),
                    Wall(704, 924, 616, 924),
                    Wall(616, 924, 616, 856),
                    Wall(616, 856, 324, 856),
                    Wall(324, 856, 324, 974),
                    Wall(324, 974, 60, 708),
                    Wall(60, 708, 60, 656),
                    Wall(60, 656, 232, 656),
                    Wall(232, 656, 232, 744),
                    Wall(232, 744, 360, 744),
                    Wall(360, 744, 360, 644),
                    Wall(360, 644, 340, 628),
                    Wall(340, 628, 252, 628),
                    Wall(252, 628, 232, 644),
                    Wall(232, 644, 172, 644),
                    Wall(172, 644, 172, 412),
                    Wall(172, 412, 60, 412),
                    Wall(60, 412, 60, 360),
                    Wall(60, 360, 152, 286),
                    Wall(152, 286, 188, 268),
                    Wall(188, 268, 268, 188),
                    Wall(268, 188, 268, 152),
                    Wall(268, 152, 324, 96),
                    Wall(324, 96, 388, 96),
                    Wall(388, 96, 388, 256),
                    Wall(388, 256, 428, 256),
                    Wall(428, 256, 428, 412),
                    Wall(428, 412, 388, 420),
                    Wall(388, 420, 340, 444),
                    Wall(340, 440, 460, 500),
                    Wall(460, 500, 464, 500),
                    Wall(464, 500, 500, 480),
                    Wall(500, 480, 532, 480),
                    Wall(532, 480, 568, 500),
                    Wall(568, 500, 572, 500),
                    Wall(572, 500, 692, 440),
                    Wall(692, 444, 644, 420),
                    Wall(644, 420, 596, 412),
                    Wall(596, 412, 596, 256),
                    Wall(596, 256, 628, 256),
                    Wall(628, 256, 628, 96),
                    Wall(628, 96, 668, 96),
                    Wall(668, 96, 668, 112),
                    Wall(564, 628, 476, 628),
                    Wall(476, 628, 456, 644),
                    Wall(456, 644, 456, 744),
                    Wall(456, 744, 584, 744),
                    Wall(584, 744, 584, 644),
                    Wall(584, 644, 564, 628),
                    Wall(792, 628, 704, 628),
                    Wall(704, 628, 684, 644),
                    Wall(684, 644, 684, 744),
                    Wall(684, 744, 812, 744),
                    Wall(812, 744, 812, 644),
                    Wall(812, 644, 792, 628)]
for wall in chemWalls:
    chemRoom.addWall(wall)
stairwellWalls = [Wall(112, 436, 420, 436),
                            Wall(420, 436, 812, 264),
                            Wall(812, 264, 944, 264),
                            Wall(944, 264, 944, 536),
                            Wall(944, 536, 812, 536),
                            Wall(812, 536, 420, 724),
                            Wall(420, 710, 420, 738),
                            Wall(420, 724, 944, 724),
                            Wall(944, 724, 944, 948),
                            Wall(944, 948, 112, 948),
                            Wall(112, 948, 112, 436)]
for wall in stairwellWalls:
    stairwell.addWall(wall)
mathWalls = [Wall(80, 152, 946, 152),
                            Wall(946, 152, 942, 912),
                            Wall(942, 912, 772, 912),
                            Wall(772, 912, 772, 964),
                            Wall(772, 964, 284, 964),
                            Wall(284, 964, 284, 868),
                            Wall(284, 868, 80, 868),
                            Wall(80, 868, 80, 152),
                            Wall(288, 288, 164, 288),
                            Wall(288, 744, 288, 288),
                            Wall(164, 744, 288, 744),
                            Wall(164, 288, 164, 744),
                            Wall(496, 288, 372, 288),
                            Wall(496, 880, 496, 288),
                            Wall(372, 880, 496, 880),
                            Wall(372, 288, 372, 880),
                            Wall(688, 288, 580, 288),
                            Wall(688, 880, 688, 288),
                            Wall(580, 880, 688, 880),
                            Wall(580, 288, 580, 880),
                            Wall(908, 276, 752, 276),
                            Wall(908, 348, 908, 276),
                            Wall(752, 348, 908, 348),
                            Wall(752, 276, 752, 348)]
for wall in mathWalls:
    mathRoom.addWall(wall)
cseWalls = [Wall(160, 248, 728, 248),
                    Wall(728, 248, 728, 256),
                    Wall(728, 256, 944, 256),
                    Wall(944, 256, 944, 592),
                    Wall(944, 592, 900, 592),
                    Wall(900, 592, 876, 616),
                    Wall(876, 584, 872, 648),
                    Wall(896, 644, 944, 644),
                    Wall(944, 644, 944, 832),
                    Wall(944, 832, 772, 832),
                    Wall(772, 832, 772, 804),
                    Wall(772, 804, 160, 804),
                    Wall(160, 804, 160, 248),
                    Wall(828, 432, 804, 408),
                    Wall(804, 408, 724, 408),
                    Wall(724, 408, 700, 432),
                    Wall(696, 432, 720, 460),
                    Wall(720, 460, 808, 460),
                    Wall(808, 460, 832, 432),
                    Wall(600, 432, 576, 408),
                    Wall(576, 408, 496, 408),
                    Wall(496, 408, 472, 432),
                    Wall(468, 432, 492, 460),
                    Wall(492, 460, 580, 460),
                    Wall(580, 460, 604, 432),
                    Wall(388, 432, 364, 408),
                    Wall(364, 408, 274, 408),
                    Wall(274, 408, 260, 432),
                    Wall(256, 432, 280, 460),
                    Wall(280, 460, 368, 460),
                    Wall(368, 460, 392, 432),
                    Wall(612, 632, 588, 608),
                    Wall(588, 608, 508, 608),
                    Wall(508, 608, 484, 632),
                    Wall(490, 632, 504, 660),
                    Wall(504, 660, 592, 660),
                    Wall(592, 660, 616, 632),
                    Wall(388, 624, 364, 600),
                    Wall(364, 600, 274, 600),
                    Wall(274, 600, 260, 624),
                    Wall(256, 624, 280, 652),
                    Wall(280, 652, 368, 652),
                    Wall(368, 652, 392, 634)]
for wall in cseWalls:
    cseRoom.addWall(wall)
def tooFar():
    Infobox(canvas, "If you go this way, Brian will get you!", 3000).show()
outsideWalls = [Wall(0, 16, 1024, 16, enterMethod = tooFar),
                        Wall(1024, 16, 1024, 980),
                        Wall(1024, 980, 0, 980),
                        Wall(0, 980, 0, 16)]
for wall in outsideWalls:
    outside.addWall(wall)
walls = [nexusWalls, freshmanWalls, freshmanSophomoreWalls, sophomoreJuniorWalls, juniorWalls, juniorNexusWalls, boysBathroomWalls, courtyardWalls, mathWalls, chemWalls, stairwellWalls, cseWalls, outsideWalls]

#   Exposition text
infoText = ["One day, while you're in the bathroom...",
                    "...the power goes out.",
                    "Oh no! What could be happening?",
                    "As you're walking back to class...",
                    "...the loudspeaker turns on:",
                    ["Everyone, there has been a power outage.",
                    "We are currently working on the problem.",
                    "For now, return to class as normal.",
                    "...",
                    "Brian, what are you doing?",
                    "Brian? Are you okay?",
                    "AHHH! EVERYONE GO TO LOCKDOWN!",
                    "BRIAN STOP IT!",
                    "...", 
                    "beep... boop..."],
                    "As you run back to CSE class...",
                    "You see Mr. Hanas standing by the door."]

#   Other objects
battery = Item(canvas, "Battery", sprites.battery, 360, 500, 32, 32, None, None, inventory, player, courtyard, False)
bushi = 0
bushGameInEffect = True
def loadBattery():
    global bushGameInEffect
    global battery
    if bushGameInEffect:
            battery.populate()
            battery.populateOnLoad = True
            bushGameInEffect = False
def bush1effect(thisBush):
    global bushi
    if bushi == 2:  bushi += 1
    else:       bushi = 0
def bush2effect(thisBush):
    global bushi
    if bushi == 4:  bushi += 1
    else:       bushi = 0
def bush3effect(thisBush):
    global bushi
    bushi = 1  
def bush4effect(thisBush):
    global bushi
    if bushi == 1:  bushi += 1
    else:       bushi = 0
def bush5effect(thisBush):
    global bushi
    global loadBattery
    if bushi == 5:
        loadBattery()
    else:       bushi = 0
def bush6effect(thisBush):
    global bushi
    if bushi == 3:  bushi += 1
    else:       bushi = 0
bush1 = ImmobileItem(canvas, "Bush1", sprites.bush, 840, 604, 120, 116, bush1effect, inventory, player, courtyard)
bush2 = ImmobileItem(canvas, "Bush2", sprites.bush, 660, 660, 120, 116, bush2effect, inventory, player, courtyard)
bush3 = ImmobileItem(canvas, "Bush3", sprites.bush, 860, 388, 120, 116, bush3effect, inventory, player, courtyard)
bush4 = ImmobileItem(canvas, "Bush4", sprites.bush, 568, 304, 120, 116, bush4effect, inventory, player, courtyard)
bush5 = ImmobileItem(canvas, "Bush5", sprites.bush, 116, 236, 120, 116, bush5effect, inventory, player, courtyard)
bush6 = ImmobileItem(canvas, "Bush6", sprites.bush, 112, 650, 120, 116, bush6effect, inventory, player, courtyard)

def hintdrawingeffect(thisdrawing):
    player.enabled = True
    thisdrawing.depopulate()
    inventory.active(True)

hintdrawing = ViewItem(canvas, "HintDrawing", sprites.hintdrawing, 0, 0, 1024, 1024, hintdrawingeffect, inventory, player, cseRoom, False)

def hintdrawingitemeffect(thisdrawing):
    global hintdrawing
    player.enabled = False
    inventory.active(False)
    root.after(10, hintdrawing.populate())

hintdrawingitem = ImmobileItem(canvas, "HintDrawingItem", sprites.hintdrawingitem, 336, 488, 30, 36, hintdrawingitemeffect, inventory, player, cseRoom)

darbyCartHasKey = False
darbyCartHasGas = False

title = None
def winByAbandonment(event):
    global title
    outside.unloadRoom()
    if event == 0:
        player.enabled = False
        inventory.active(False)
        title = Room( [], [], sprites.titleCards[0], canvas, inventory, titleCard=True, player = player)
        title.loadRoom()
        root.after(3000, winByAbandonment, 1)
    if event == 1:
        title.unloadRoom()
        title = Room( [], [], sprites.titleCards[1], canvas, inventory, titleCard=True, player = player)
        title.loadRoom()
        root.after(3000, winByAbandonment, 2)
    if event == 2:
        title.unloadRoom()
        title = Room( [], [], sprites.titleCards[2], canvas, inventory, titleCard=True, player = player)
        title.loadRoom()

def winByIce(event):
    if event == 0:
        player.enabled = False
        inventory.active(False)
        brian.populate()
        info = Infobox(canvas, 'Brian has been summoned!', 2500)
        info.show()
        root.after(2500, winByIce, 1)
    if event == 1:
        brian.depopulate()
        brianFallen.populate()
        info = Infobox(canvas, 'Whoops! There he goes!', 2500)
        info.show()
        root.after(2500, winByIce, 2)
    if event == 2:
        info = Infobox(canvas, "He's fallen and he can't get up! He ded.", 2500)
        info.show()
        root.after(2500, winByIce, 3)
    if event == 3:
        stairwell.unloadRoom()
        Room( [], [], sprites.titleCards[3], canvas, inventory, titleCard=True, player = player).loadRoom()

brian = ImmobileItem(canvas, "Brian", sprites.brianAvatars[0], 844, 388, 64, 96, None, inventory, player, stairwell, False)
brianFallen = ImmobileItem(canvas, "BrianFallen", sprites.brianAvatars[1], 308, 596, 96, 64, None, inventory, player, stairwell, False)

def lose(event):
    if event == 0:
        player.enabled = False
        inventory.active(False)
        brian.populate()
        info = Infobox(canvas, 'Brian has been summoned!', 2500)
        info.show()
        root.after(2500, lose, 1)
    if event == 1:
        info = Infobox(canvas, 'Foolishly, you have not prepared for Brian.', 2500)
        info.show()
        root.after(2500, lose, 2)
    if event == 2:
        brian.depopulate()
        brian.populate(308, 570)
        info = Infobox(canvas, 'Beep Boop. Ya ded.', 1500)
        info.show()
        root.after(1500, lose, 3)
    if event == 3:
        stairwell.unloadRoom()
        Room( [], [], sprites.titleCards[4], canvas, inventory, titleCard=True, player = player).loadRoom()

def darbyCartEffect(thisCart):
    global darbyCartHasKey, darbyCartHasGas, winByAbandonment
    if darbyCartHasKey and darbyCartHasGas:
        winByAbandonment(0)
    elif not darbyCartHasKey:
        infobox = Infobox(canvas, "The key is missing.", 1500)
        infobox.show()
    else:
        infobox = Infobox(canvas, "The gas tank is empty.", 1500)
        infobox.show()

darbyCart = ImmobileItem(canvas, "Darby Cart", sprites.darbycart, 96, 520, 312, 148, darbyCartEffect, inventory, player, outside)

def funkyFrostingFuelEffect(fuel, darbyCart, clickx, clicky):
    global darbyCartHasGas
    if darbyCart.click(clickx, clicky, False):
        fuel._inventory.removeItem(fuel)
        darbyCartHasGas = True
        infobox = Infobox(canvas, "You put the fuel in the Darby Cart.", 2500)
        infobox.show()
        return True
    return False

def darbyCartKeysEffect(keys, darbyCart, clickx, clicky):
    global darbyCartHasKey
    if darbyCart.click(clickx, clicky, False):
        keys._inventory.removeItem(keys)
        keys.depopulate()
        darbyCartHasKey = True
        infobox = Infobox(canvas, "You put the keys in the ignition.", 2500)
        infobox.show()
        return True
    return False

funkyFrostingFuel = Item(canvas, "Funky Frosting Fuel", sprites.fuel, 340, 240, 48, 48, funkyFrostingFuelEffect, darbyCart, inventory, player, chemRoom, False)
darbyCartKeys = Item(canvas, "Darby Cart Keys", sprites.modernkey, 770, 480, 32, 32, darbyCartKeysEffect, darbyCart, inventory, player, mathRoom)
mathKey = Item(canvas, "Mullar Key", sprites.oldkey, 800, 500, 32, 32, None, None, inventory, player, boysBathroom)

def chunkOfIceEffect(thisChunkOfIce):
    infobox = Infobox(canvas, "Wow! That's a big piece of ice!", 1500)
    infobox.show()

chunkOfIce = ImmobileItem(canvas, "Chunk of Ice", sprites.icechunk, 596, 36, 162, 168, chunkOfIceEffect, inventory, player, outside)

def icePickEffect(icePick, chunkOfIce, clickx, clicky):
    global ice
    if chunkOfIce.click(clickx, clicky, False):
        icePick._inventory.removeItem(icePick)
        icePick.depopulate()
        ice.populate()
        return True
    return False
    

icePick = Item(canvas, "Ice Pick", sprites.icepick, 80, 430, 64, 64, icePickEffect, chunkOfIce, inventory, player, chemRoom)
flashlight = Item(canvas, 'Flashlight', sprites.flashlight, 512, 512, 64, 64, None, None, inventory, player, juniorHallway, populateOnLoad = False)

calculatorOnPedestal = False
iceOnStairs = False

def attemptVictoryEnding():
    if iceOnStairs:
        winByIce(0)
    else:
        lose(0)

def calculatorOnPedestalEffect(thisCalculator):
    infobox = Infobox(canvas, "The calculator is sitting on the pedestal.", 1500)
    infobox.show()
calculatorObjectOnPedestal = ImmobileItem(canvas, "CalculatorOnPedestal", sprites.calculator, 270, 575, 16, 32, calculatorOnPedestalEffect, inventory, player, stairwell, False)

def iceOnStairsEffect(thisIce):
    infobox = Infobox(canvas, "The ice is sitting at the top of the stairs.", 1500)
    infobox.show()
iceObjectOnStairs = ImmobileItem(canvas, "IceOnStairs", sprites.ice, 828, 412, 64, 64, iceOnStairsEffect, inventory, player, stairwell, False)

def pedestalEffect(thisPedestal):
    infobox = Infobox(canvas, "It's a strange-looking pedestal.", 1500)
    infobox.show()
def calculatorEffect(thisCalculator, thisPedestal, clickx, clicky):
    global calculatorOnPedestal, iceOnStairs
    if thisPedestal.click(clickx, clicky, False):
        thisCalculator._inventory.removeItem(thisCalculator)
        thisCalculator.depopulate()
        calculatorObjectOnPedestal.populate()
        attemptVictoryEnding()
        return True
    return False
def iceEffect(thisIce, topOfStairs, clickx, clicky):
    global calculatorOnPedestal, iceOnStairs
    if topOfStairs.click(clickx, clicky, False):
        thisIce._inventory.removeItem(thisIce)
        thisIce.depopulate()
        iceObjectOnStairs.populate()
        iceOnStairs = True
        return True
    return False

pedestal = ImmobileItem(canvas, "Pedestal", sprites.pedestal, 248, 580, 64, 96, pedestalEffect, inventory, player, stairwell)
icePlacer = ImmobileItem(canvas, "Ice Placer", sprites.door, 816, 328, 96, 224, None, inventory, player, stairwell)
ice = Item(canvas, "Ice", sprites.ice, 700, 200, 64, 64, iceEffect, icePlacer, inventory, player, outside, False)
calculator = Item(canvas, "Calculator", sprites.calculator, 820, 460, 32, 64, calculatorEffect, pedestal, inventory, player, mathRoom)

courtyardDooraIn = Door(canvas, 'courtyardDooraIn', 316, 28, 40, 200, inventory, player, nexus, courtyard, (928, 520))
boysBathroomDoorIn = Door(canvas, 'boysBathroomDoorIn', 316, 252, 40, 120, inventory, player, nexus, boysBathroom, (932, 842), dark = True, flashlight = flashlight, battery = battery)
guidanceDoora = Door(canvas, 'guidanceDoora', 656, 212, 40, 104, inventory, player, nexus)
girlsBathroomDoor = Door(canvas, 'girlsBathroomDoor', 188, 428, 84, 132, inventory, player, nexus)
door110 = Door(canvas, 'door110', 868, 936, 92, 40, inventory, player, freshmanHallway)
door120 = Door(canvas, 'door120', 600, 936, 92, 40, inventory, player, freshmanHallway)
door125 = Door(canvas, 'door120', 484, 364, 80, 136, inventory, player, freshmanHallway)
mathDoorIn = Door(canvas, 'mathDoorIn', 224, 364, 80, 136, inventory, player, freshmanHallway, mathRoom, (856, 800), key= mathKey)
chemDoorIn = Door(canvas, 'chemDoorIn', 124, 884, 112, 112, inventory, player, freshmanSophomoreHallway, chemRoom, (830, 312))
door145 = Door(canvas, 'door145', 4, 616, 40, 152, inventory, player, freshmanSophomoreHallway)
courtyardDoorbIn = Door(canvas, 'courtyardDoorbIn', 452, 0, 36, 192, inventory, player, freshmanSophomoreHallway, courtyard, (68, 652))
fish = Item(canvas, "Red Herring", sprites.fish, 500, 500, 64, 64, None, None, inventory, player, sophomoreJuniorHallway)
stairwellDoorIn = Door(canvas, 'stairwellDoorIn', 112, 780, 40, 152, inventory, player, sophomoreJuniorHallway, stairwell, (900, 436))
door160 = Door(canvas, 'door160', 16, 436, 40, 152, inventory, player, sophomoreJuniorHallway)
door165 = Door(canvas, 'door165', 172, 216, 84, 136, inventory, player, sophomoreJuniorHallway)
door175 = Door(canvas, 'door175', 332, 152, 84, 136, inventory, player, juniorHallway)
door177 = Door(canvas, 'door177', 628, 216, 84, 132, inventory, player, juniorHallway)
deDoorIn = Door(canvas, 'deDoorIn', 72, 724, 92, 40, inventory, player, juniorHallway)
door185 = Door(canvas, 'door185', 328, 724, 92, 40, inventory, player, juniorHallway)
cseDoorIn = Door(canvas, 'cseDoorIn', 76, 152, 84, 136, inventory, player, juniorHallway, cseRoom, (864, 772))
outsideDoorb = Door(canvas, 'outsideDoorb', 964, 680, 40, 220, inventory, player, juniorNexus, outside = True)
guidanceDoorb = Door(canvas, 'guidanceDoorb', 744, 944, 124, 40, inventory, player, juniorNexus)
boysBathroomDoorOut = Door(canvas, 'boysBathroomDoorOut', 968, 776, 48, 132, inventory, player, boysBathroom, nexus, (396, 312))
courtyardDooraOut = Door(canvas, 'courtyardDooraOut', 976, 484, 44, 72, inventory, player, courtyard, nexus, (396, 128))
courtyardDoorbOut = Door(canvas, 'courtyardDoorbOut', 44, 524, 48, 64, inventory, player, courtyard, freshmanSophomoreHallway, (416, 96))
mathDoorOut = Door(canvas, 'mathDoorOut', 804, 896, 108, 40, inventory, player, mathRoom, freshmanHallway, (264, 568))
chemDoorOut = Door(canvas, 'chemDoorOut', 800, 168, 56, 148, inventory, player, chemRoom, freshmanSophomoreHallway, (236, 896))
stairwellDoorOut = Door(canvas, 'stairwellDoorOut', 932, 368, 40, 136, inventory, player, stairwell, sophomoreJuniorHallway, (184, 856))
stairwellExit = Door(canvas, 'stairwellExit', 80, 504, 40, 220, inventory, player, stairwell, outside, (512, 928))
doorTech = Door(canvas, 'doorTech', 216, 952, 136, 40, inventory, player, stairwell)
doorStairwellHall = Door(canvas, 'doorStairwellHall', 932, 780, 40, 136, inventory, player, stairwell)
cseDoorOut = Door(canvas, 'cseDoorOut', 800, 836, 128, 36, inventory, player, cseRoom, juniorHallway, (118, 220))
stairwellEntrance = Door(canvas, 'stairwellEntrance', 424, 984, 168, 40, inventory, player, outside, stairwell, (180, 614))
def hanasDialogue():
    if stairwellEnter:
        inventory.addItem(flashlight)
        return Writing('playername', 'male').chanas3()
    else:
        return Writing('playername', 'male').chanas2()
mrHanas = Npc(canvas, 64, 96, 150, 300, 1, sprites.chanasAvatars, 'Mr. Hanas', sprites.hanasface, hanasDialogue, inventory, player, juniorHallway) 


metBabbinFirstTime = False
tookFuel = False
def frostingEffect(thisFrosting, thisMsBabbin, clickx, clicky):
    global tookFuel
    if thisMsBabbin.click(clickx, clicky, False):
        thisFrosting._inventory.removeItem(thisFrosting)
        thisFrosting.depopulate
        funkyFrostingFuel.populate()
        tookFuel = True
        info = Dialogue(canvas, Writing("playername", "male").babbin4(), 'Mrs. Babbin', sprites.babbinface, chemRoom, msBabbin, player, inventory)
        info.show()
        return True
    return False

def babbinProduceSpeech():
    global tookFuel
    if tookFuel:
        return Writing('playername', 'male').babbin4()
    elif metBabbinFirstTime:
        return Writing('playername', 'male').babbin2()
    else:
        return Writing('playername', 'male').babbin1()
    

msBabbin = Npc(canvas, 64, 96, 360, 192, 1, sprites.babbinAvatars, 'Ms. Babbin', sprites.babbinface, babbinProduceSpeech, inventory, player, chemRoom)
frosting = Item(canvas, "Huge Tub of Frosting", sprites.frosting, 85, 600, 64, 64, frostingEffect, msBabbin, inventory, player, boysBathroom)

stepheni = -1
def stephenProduceSpeech():
    global stepheni
    stepheni += 1
    if stepheni == 5: stepheni = 0
    if stepheni == 0: return Writing('playername', 'male').stephen()
    if stepheni == 1: return Writing('playername', 'male').stephen1()
    if stepheni == 2: return Writing('playername', 'male').stephen2()
    if stepheni == 3: return Writing('playername', 'male').stephen3()
    if stepheni == 4: return Writing('playername', 'male').stephen4()

stephen = Npc(canvas, 64, 96, 350, 350, 1, sprites.stephenAvatars, 'Stephen', sprites.stephenface, stephenProduceSpeech, inventory, player, cseRoom)


def mullarkeyProduceSpeech():
    return Writing('playername', 'male').mullarkey()

mullarkey = Npc(canvas, 64, 96, 800, 400, 1, sprites.mullarkeyAvatars, 'Mr. Mullarkey', sprites.mullarkeyface, mullarkeyProduceSpeech, inventory, player, mathRoom)
objects = [player, pedestal, hintdrawingitem, hintdrawing, bush1, bush2, bush3, bush4, bush5, bush6, courtyardDooraIn, 
    icePick, boysBathroomDoorIn, guidanceDoora, girlsBathroomDoor, door110, door120, door125, mathDoorIn, chemDoorIn,
    door145, courtyardDoorbIn, fish, battery, stairwellDoorIn, door160, door165, cseDoorIn, door175, door177, deDoorIn,
    door185, outsideDoorb, guidanceDoorb, boysBathroomDoorOut, courtyardDooraOut, courtyardDoorbOut, mathDoorOut, 
    chemDoorOut, stairwellDoorOut, stairwellExit, doorTech, doorStairwellHall, cseDoorOut, stairwellEntrance, mullarkey, 
    mrHanas, msBabbin, darbyCart, chunkOfIce, darbyCartKeys, funkyFrostingFuel, mathKey, frosting, ice, calculator, stephen]

''' Play function called once playButton is pressed.    '''
def startGame():
    boysBathroom.loadRoom()
    start(0)
    #loop()
    #player.enabled = True
    #inventory.active(True)
    

def play():
    playButton.destroy()
    chooseBoy.place(x = 312, y = 512, anchor = CENTER)
    chooseGirl.place(x = 712, y = 512, anchor = CENTER)
    # cseRoom.loadRoom()
    # brian.populate()
    # loop()
    # player.enabled = True
    # inventory.active(True)

def boy():
    chooseBoy.destroy()
    chooseGirl.destroy()
    startGame()
def girl():
    chooseBoy.destroy()
    chooseGirl.destroy()
    player.changeFiles(sprites.girlAvatars)
    startGame()


#   Create a play button
playButton = Button(root, text = "Play!", command = play, font=96)
playButton.place(x = 512, y = 512, anchor = CENTER)

chooseBoy = Button(root, text = "Boy", command = boy, font=96)

chooseGirl = Button(root, text = "Girl", command = girl, font=96)

''' Start the game and run through the opening "cutscene."  '''
def start(event):
    if event == 1:
        inventory.active(False)
        boysBathroom.unloadRoom()
        darkRoom.loadRoom()
    elif event == 3:
        darkRoom.unloadRoom()
        nexus.loadRoom()
    elif event == 6:
        nexus.unloadRoom()
        juniorHallway.loadRoom()
    if event == 5:
        info = Dialogue(canvas, infoText[event], 'Loudspeaker', sprites.loudspeaker, nexus, None, player, inventory)
        info.show()
        isDialogueGone(event, info)
    elif event < len(infoText):
        info = Infobox(canvas, infoText[event], 3000)
        info.show()
        root.after(3000, start, event + 1)
    else: 
        inventory.active(True)
        loop()
        info = Dialogue(canvas, writeObject.chanas1(), 'Mr. Hanas', sprites.hanasface, juniorHallway, mrHanas, player, inventory)
        info.show()

''' Check if the dialogue is gone.  '''
def isDialogueGone(event, dialogue):
    if dialogue.finished():
        inventory.active(False)
        start(event + 1)
    else:
        root.after(8, isDialogueGone, event, dialogue)

''' Run the main loop for the game. '''
i = 0
def loop():
    global i
    i += 1
    #print(i)
    player.changePosition(x = player.getXDir() * player.getSpeed(), y = player.getYDir() * player.getSpeed())
    player.move()
    for object in objects:
        object.updateSprite()
    for wallList in walls:
        for wall in wallList:
            wall.removePlayer(player)
    player.move()
    root.after(8, loop)

mainloop()