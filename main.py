from tkinter import *
from board import *

if __name__ == "__main__":
    root = Tk()
    print(root.winfo_screenwidth())
    board = Board(root, root.winfo_screenwidth(), root.winfo_screenheight())
    board.mainloop()
