"""Module that starts the Tk mainloop"""
from tkinter import *

from window import MainWindow


if __name__ == "__main__":
    tk = Tk()

    MainWindow(tk)

    tk.mainloop()