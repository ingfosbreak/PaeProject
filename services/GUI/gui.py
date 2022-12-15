from tkinter import *
from tkinter import ttk, RIGHT, BOTTOM, Y, X, NO, CENTER
from PIL import Image, ImageTk
from urllib.request import urlopen
from io import BytesIO
from services.google_search.images_search import fetch_images
import time


mock_images_url= ['https://pixnio.com/free-images/2017/10/21/2017-10-21-08-04-02.jpg',
 'https://c0.wallpaperflare.com/preview/397/432/51/sky-wallpaper-background-nature.jpg',
 'https://pixnio.com/free-images/2017/10/21/2017-10-21-08-04-02-1078x825.jpg',
 'https://p0.pikist.com/photos/89/865/building-house-old-colonial-doors-architecture-painted-urban-city.jpg',
 'https://pixnio.com/free-images/2017/09/13/2017-09-13-07-49-15.jpg'
 ]

class PaeGUI: 
    def __init__(self,root):
        self.root = root
        self.root.title("PaeProgram")
        self.root.geometry("1000x550")
        self.root.resizable(False, False) 
        self.images = []

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
        self.search_keyword_field.grid(row=1, column=1, padx=30, pady=20)
        self.selected_type_combobox.grid(row=2, column=1, padx=30, pady=5)
        self.selected_dominant_color_combobox.grid(row=3, column=1, padx=30, pady=5)

        # fix window GUI
        self.fix1 = Label(self.canvas, text="",  bg='#DEE5E5').grid(row=1, column=4, padx=20, pady=20)
        self.fix2 = Label(self.canvas, text="",  bg='#DEE5E5').grid(row=5, column=4, padx=20, pady=30)
        
        

        self.submit_button = Button(self.canvas, text='Submit',  bg='#DEE5E5',
                                      command=lambda x=None: self.submit_handler())
        self.submit_button.grid(row=4, column=0, padx=5, pady=30, columnspan=2)

        # logo
        logo_image = Image.open("resources/Logo.jpg")
        logo_image_TK = ImageTk.PhotoImage(logo_image)

        logo_Label = Label(self.leftFrame, image=logo_image_TK,highlightthickness=0,bg="white")
        logo_Label.image = logo_image_TK
        
        logo_Label.place(x=35, y=30)






        '''
            Right Frame
        '''

        self.var1 = StringVar()
        self.var2 = StringVar()
        self.var3 = StringVar()
        self.var4 = StringVar()

        self.var1.set("ImageSearch:~ $python")
        self.var2.set("Python 3.9.10 (default, released 13)")
        self.var3.set("Type “help”, “copyright”, “credits” or “license” for more information")
        self.var4.set(">>> Wating for Image Search")

        self.terminal1 = Label(self.rightFrame, textvariable=self.var1, fg='#29BF12', bg="black")
        self.terminal2 = Label(self.rightFrame, textvariable=self.var2, fg='#29BF12', bg="black")
        self.terminal3 = Label(self.rightFrame, textvariable=self.var3, fg='#29BF12', bg="black")
        self.terminal4 = Label(self.rightFrame, textvariable=self.var4, fg='#29BF12', bg="black")

        self.terminal1.place(x=50,y=50)
        self.terminal2.place(x=50,y=70)
        self.terminal3.place(x=50,y=90)
        self.terminal4.place(x=50,y=110)


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
        for widget in self.images:
            widget.destroy() 
        
        current_search_keyword = self.search_keyword.get()
        current_selected_type = self.selected_type.get()
        current_selected_dominant_color = self.selected_dominant_color.get()

        self.var1.set("")
        self.var2.set("")
        self.var3.set("")
        self.var4.set("")



        if current_selected_type == "None":
            current_selected_type = ""
        if current_selected_dominant_color == "None":
            current_selected_dominant_color = "imgDominantColorUndefined"

        # use google image search service
        # get list of images
        print(f'ui: fetch_images("{current_search_keyword} {current_selected_type}", "{current_selected_dominant_color}")')
        images_url = fetch_images(f"{current_search_keyword} {current_selected_type}", current_selected_dominant_color)
        print(images_url)       
        if type(images_url) is list:
            # display images
            # self.display_images(mock_images_url)

            self.display_images(images_url)
        else:
            # error handle
            self.var1.set("ImageSearch:~ $python")
            self.var2.set("Python 3.9.10 (default, released 13)")
            self.var3.set("Type “help”, “copyright”, “credits” or “license” for more information")
            self.var4.set(f">>> Error {images_url}")

            self.terminal1.config(fg="red")
            self.terminal2.config(fg="red")
            self.terminal3.config(fg="red")
            self.terminal4.config(fg="red")

    def display_images(self, images: list[str]):
        temp_row = 1
        posy = 50
        posx = 50
        for image_url in images:
            
            try:
                u = urlopen(image_url) 
                raw_data = u.read()
                u.close()

                # open the image and resize
                im = Image.open(BytesIO(raw_data)).resize((250, 150))

                photo = ImageTk.PhotoImage(im)
                label = Label(self.rightFrame,image=photo)
                self.images.append(label)
                label.image = photo
                label.place(x= posx, y= posy)
                posy += 150
                # grid(row=temp_row, column=0, padx=5, pady=5, columnspan=100)
                if (temp_row == 3):
                    posx = 310
                    posy = 50
                temp_row += 1
            except:
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