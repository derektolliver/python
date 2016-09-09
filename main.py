from tkinter import *
from board import *

if __name__ == "__main__":
    root = Tk()
    width = root.winfo_screenwidth() // 2
    height = int(root.winfo_screenheight() / 1.5)
    size = str(width) + 'x' + str(height)
    root.geometry(size)
    print(root.winfo_screenwidth())
    board = Board(root.winfo_screenwidth(), root.winfo_screenheight())
    board.mainloop()
