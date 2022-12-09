# starting point of the program
import tkinter as tk
import tkinter.ttk as ttk

# internals
from widgets.ds import DeltaStar

class Applications():
    def __init__(self, master):
        
        base = DeltaStar(master)
        base.pack(expand=True, fill="both")

        master.mainloop()


if __name__ == "__main__":
    window = tk.Tk()
    window.geometry("600x500")
    window.title("Tkinter Delta-Star Conversion")
    app = Applications(window)
