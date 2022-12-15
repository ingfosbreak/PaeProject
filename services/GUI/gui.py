from tkinter import *
from tkinter import ttk, RIGHT, BOTTOM, Y, X, NO, CENTER
from PIL import Image, ImageTk
from urllib.request import urlopen
from io import BytesIO

class PaeGUI: 
    def __init__(self,root):
        self.root = root
        self.root.title("PaeProgram")
        self.root.geometry("1000x550")
        self.root.resizable(False, False) 

        # variables
        self.search_keyword = StringVar()
        self.selected_type = StringVar()
        self.selected_dominant_color = StringVar()
        

        self.selected_type_choices = ["None", "room", "building"]
        self.selected_dominant_color_choices = ["None", "black","blue", "brown", "gray", "green", "orange", "pink", "purple", "red", "teal", "white", "yellow"]

        '''
            for draggable and beauty
        '''
        self.root.overrideredirect(True) 
        self.lastClickX = 0
        self.lastClickY = 0
        self.make_Draggable(self.root)
    

        self.init_Components()



    def init_Components(self):
        ''' 
            Main Frame
        '''
        self.leftFrame = Frame(self.root, bg="#FFFFFF",width=400,height=550)
        self.leftFrame.pack(side=LEFT)
        self.rightFrame = Frame(self.root, bg="black",width=800,height=550, highlightthickness=1)
        self.rightFrame.pack(side= RIGHT)

        '''
            Left Frame
        '''
        self.canvas = Canvas(self.leftFrame, bg="#FFFFFF", width=400,height=550,highlightthickness=0)
        self.canvas.place(x=25,y=250)
        self.round_rectangle(self.canvas,0, 0, 350, 275, radius=70)

        self.search_keyword_field = Entry(self.canvas, width=20, textvariable=self.search_keyword)
        self.selected_type_combobox = ttk.Combobox(self.canvas, width=20, textvariable=self.selected_type, state="readonly")
        self.selected_dominant_color_combobox = ttk.Combobox(self.canvas, width=20, textvariable=self.selected_dominant_color, state="readonly")

        # set combobox value
        self.selected_type_combobox["values"] = self.selected_type_choices
        self.selected_dominant_color_combobox["values"] = self.selected_dominant_color_choices

         # set default value
        self.selected_type_combobox.current(0)
        self.selected_dominant_color_combobox.current(0)


        # don't forget to add sticky
        self.search_keyword_label = Label(self.canvas, text="Search keyword:", bg='#DEE5E5').grid(row=1, column=0, padx=10, pady=20)
        self.selected_type_label = Label(self.canvas, text="Types:",  bg='#DEE5E5').grid(row=2, column=0, padx=10, pady=20)
        self.selected_dominant_color_label = Label(self.canvas, text="Dominant color:",  bg='#DEE5E5').grid(row=3, column=0, padx=10, pady=20)
        self.search_keyword_field.grid(row=1, column=1, padx=20, pady=20,)
        self.selected_type_combobox.grid(row=2, column=1, padx=5, pady=5)
        self.selected_dominant_color_combobox.grid(row=3, column=1, padx=5, pady=5)

        self.submit_button = Button(self.canvas, text='Submit',  bg='#DEE5E5',
                                      command=lambda x=None: self.submit_handler())
        self.submit_button.grid(row=4, column=0, padx=5, pady=30, columnspan=2)



        '''
            Right Frame
        '''

        '''
            Close Button
        '''

        close_image = Image.open("resources/close-button-label.png")
        close_image_TK = ImageTk.PhotoImage(close_image)

        close_Label = Label(self.root, image=close_image_TK, bg='white')
        close_Label.image = close_image_TK
        close_Label.bind('<Button-1>', self.exit_button_Click)

        
        close_Label.place(x=965, y=15)



    def round_rectangle(self, root, x1, y1, x2, y2, radius=25, **kwargs): # Creating a rounded rectangle
        
        points = [x1+radius, y1,
                x1+radius, y1,
                x2-radius, y1,
                x2-radius, y1,
                x2, y1,
                x2, y1+radius,
                x2, y1+radius,
                x2, y2-radius,
                x2, y2-radius,
                x2, y2,
                x2-radius, y2,
                x2-radius, y2,
                x1+radius, y2,
                x1+radius, y2,
                x1, y2,
                x1, y2-radius,
                x1, y2-radius,
                x1, y1+radius,
                x1, y1+radius,
                x1, y1]

        return root.create_polygon(points, **kwargs, smooth=True, fill="#DEE5E5")

    def submit_handler(self):
        pass

    def make_Draggable(self, root):
        root.bind('<Button-1>', self.saveLastClickPos)
        root.bind('<B1-Motion>', self.dragging)
    
    def saveLastClickPos(self, event):
        global lastClickX, lastClickY
        lastClickX = event.x
        lastClickY = event.y

    def dragging(self,event):
        x, y = event.x - lastClickX + self.root.winfo_x(), event.y - lastClickY + self.root.winfo_y()
        self.root.geometry("+%s+%s" % (x , y))


    def exit_button_Click(self,event):
        self.root.destroy()