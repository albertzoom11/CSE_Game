'''
Project Name: Choose Your Own Adventure
Team Members: Albert Zou, Benjamin Knobloch, Kyle DiMaggio
Date: February 13
Task Description: Stores info about info boxes.
'''

from tkinter import *
from PIL import Image, ImageTk
import sprites

class Infobox:
    thisObject = None
    __canvas = None
    text = ""
    textObject = None
    __box = None
    timeduration = 0

    def __init__(self, canvas, text, timeduration):
        self.__canvas = canvas
        self.text = text
        self.timeduration = timeduration
        global box
        box = Image.open(sprites.uiBoxes[1])
        box = box.resize((800, 72))
        self.__box = ImageTk.PhotoImage(box)
        
    ''' Destroys the info box.  '''
    def destroy(self):
        self.__canvas.delete(self.thisObject)
        self.__canvas.delete(self.textObject)

    ''' Displays the info box.  '''
    def show(self):
            self.__canvas.after(self.timeduration, self.destroy)
            self.thisObject = self.__canvas.create_image(200, 62, image=self.__box, anchor=NW)
            self.textObject = self.__canvas.create_text(600, 98, text=self.text, width=675, fill="white", font=("Comic Sans MS", 24, 'italic'), anchor=CENTER)
