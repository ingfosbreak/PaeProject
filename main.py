from tkinter import *
from services.GUI.gui import PaeGUI

# main function
def main():
    root = Tk()
    app = PaeGUI(root)
    root.mainloop()



if __name__ == '__main__':
    main()