from tkinter import *

class Board(Frame):

    def __init__(self, master, w, h):
        frame = Frame(master)
        Frame.__init__(self, frame, width = w, height = h, background = "white")
        #Frame.grid()
