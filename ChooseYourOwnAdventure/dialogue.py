'''
Stores info about dialogue.
'''

from tkinter import *
from PIL import Image, ImageTk
import sprites

class Dialogue:
    thisObject = None
    __canvas = None
    room = None
    command = None
    text = []
    curText = 0
    textObject = None
    name = ""
    nameObject = None
    closeInfoObject = None
    speaker = None
    __box = None
    __player = None
    __inventory = None

    def __init__(self, canvas, text, name, icon, room, speaker, player, inventory):
        self.__canvas = canvas
        self.text = text
        self.name = name
        self.room = room
        self.speaker = speaker
        global box
        box = Image.open(sprites.uiBoxes[0])
        global image    #Prevents image being moved to garbage collection and becoming invisible
        image = Image.open(icon)
        image = image.resize((175, 175))
        box.paste(image, (25, 25))              #   Paste icon onto text box.
        self.__box = ImageTk.PhotoImage(box)
        self.__player = player
        self.__inventory = inventory
        
    ''' Calls the next line of dialogue in the sequence.    '''
    def click(self, eventx, eventy, noneSelected):
        self.curText += 1
        if self.curText < len(self.text):                   #   If there is another line of dialogue in the sequence, display it.
            self.__canvas.delete(self.textObject)
            #if self.text[self.curText][0:7] == "COMMAND":
            #    self.command()
            if self.text[self.curText][0:8] == "THINKING":  #   If the lines begins with THINKING, change the format of the text.
                self.textObject = self.__canvas.create_text(365, 725, text=self.text[self.curText][8:], width=475, fill="gray", font=("Comic Sans MS", 18, "bold", "italic"), anchor=NW)                
            else:
                self.textObject = self.__canvas.create_text(365, 725, text=self.text[self.curText], width=475, fill="white", font=("Comic Sans MS", 23, "bold"), anchor=NW)

        else:                                               #   If the end of the dialogue is reached, destroy the text box.
            self.__canvas.delete(self.thisObject)
            self.__canvas.delete(self.textObject)
            self.__canvas.delete(self.nameObject)
            self.__canvas.delete(self.closeInfoObject)
            if self.speaker != None:                   #   If the dialogue box was created by an NPC, return the NPC to its idle position.
                self.speaker.speakMode = 0
            self.room.removeObject(self)
            self.__player.enabled = True
            self.__inventory.active(True)

    ''' Begins sequence of text boxes.  '''
    def show(self):
        self.room.addObject(self) #    Binds the mouse click to nextText(), which replaces the text with the next in the list
        self.thisObject = self.__canvas.create_image(137, 700, image=self.__box, anchor=NW)
        self.textObject = self.__canvas.create_text(365, 725, text=self.text[0], width=475, fill="white", font=("Comic Sans MS", 23, 'bold'), anchor=NW)
        self.nameObject = self.__canvas.create_text(250, 920, text=self.name, fill="white", font=("Comic Sans MS", 19, "bold", 'italic'))
        self.closeInfoObject = self.__canvas.create_text(875, 913, text="Click to proceed.", fill="lightgray", font=("Comic Sans MS", 16, 'italic'), anchor=NE)
        self.__player.enabled = False
        self.__inventory.active(False)
    
    ''' If the dialogue boxes have been fully read, return True. Otherwise, return False.   '''
    def finished(self):
        if self.curText == len(self.text):
            return True
        return False
