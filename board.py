from tkinter import *

class Board(Frame):

    def __init__(self, w, h):
        Frame.__init__(self, width = w, height = h, background = "white")
        #Frame.grid()
