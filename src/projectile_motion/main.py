"""Module that starts the Tk mainloop"""
from tkinter import Tk
from window import MainWindow

def main() -> None:
    tk = Tk()
    MainWindow(tk)
    tk.mainloop()    

if __name__ == "__main__":
    main()