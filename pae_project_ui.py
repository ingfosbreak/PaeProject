import tkinter as tk
from tkinter import ttk, RIGHT, BOTTOM, Y, X, NO, CENTER


class PaeProject(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("PaeProject")

        # variable

        self.init_components()

    def init_components(self):
        pass

    def run(self):
        self.mainloop()


if __name__ == "__main__":
    UI = PaeProject()
    UI.run()