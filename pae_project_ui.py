import tkinter as tk
from tkinter import ttk, RIGHT, BOTTOM, Y, X, NO, CENTER
from PIL import Image, ImageTk
from urllib.request import urlopen
from io import BytesIO


mock_images_url= ['https://pixnio.com/free-images/2017/10/21/2017-10-21-08-04-02.jpg',
 'https://c0.wallpaperflare.com/preview/397/432/51/sky-wallpaper-background-nature.jpg',
 'https://pixnio.com/free-images/2017/10/21/2017-10-21-08-04-02-1078x825.jpg',
 'https://p0.pikist.com/photos/89/865/building-house-old-colonial-doors-architecture-painted-urban-city.jpg',
 'https://pixnio.com/free-images/2017/09/13/2017-09-13-07-49-15.jpg']

class PaeProject(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("PaeProject")
        # self.grid_rowconfigure(0, weight=1)  # 5
        # self.grid_columnconfigure(0, weight=1)  # 7

        # variables
        self.search_keyword = tk.StringVar()
        self.selected_type = tk.StringVar()
        self.selected_dominant_color = tk.StringVar()

        self.selected_type_choices = ["None", "room", "building"]
        self.selected_dominant_color_choices = ["None", "black","blue", "brown", "gray", "green", "orange", "pink", "purple", "red", "teal", "white", "yellow"]

        self.init_components()

    def init_components(self):
        self.search_keyword_field = tk.Entry(self, width=20, textvariable=self.search_keyword)
        self.selected_type_combobox = ttk.Combobox(self, width=20, textvariable=self.selected_type, state="readonly")
        self.selected_dominant_color_combobox = ttk.Combobox(self, width=20, textvariable=self.selected_dominant_color, state="readonly")

        # set combobox value
        self.selected_type_combobox["values"] = self.selected_type_choices
        self.selected_dominant_color_combobox["values"] = self.selected_dominant_color_choices

        # set default value
        self.selected_type_combobox.current(0)
        self.selected_dominant_color_combobox.current(0)

        # don't forget to add sticky
        self.search_keyword_label = tk.Label(self, text="Search keyword:").grid(row=1, column=0, padx=5, pady=5)
        self.selected_type_label = tk.Label(self, text="Types:").grid(row=2, column=0, padx=5, pady=5)
        self.selected_dominant_color_label = tk.Label(self, text="Dominant color:").grid(row=3, column=0, padx=5, pady=5)
        self.search_keyword_field.grid(row=1, column=1, padx=5, pady=5)
        self.selected_type_combobox.grid(row=2, column=1, padx=5, pady=5)
        self.selected_dominant_color_combobox.grid(row=3, column=1, padx=5, pady=5)

        self.submit_button = tk.Button(self, text='Submit',
                                      command=lambda x=None: self.submit_handler())
        self.submit_button.grid(row=4, column=0, padx=5, pady=5, columnspan=2)

        # Frame
        # self.images_frame = tk.Frame(self, bg="black", width=1000, height=500)
        # self.images_frame.grid(row=1, column=2, padx=5, pady=5, columnspan=5, rowspan=100)

        # Display text
        # self.frame_status_label = tk.Label(self.images_frame, text="Nothing to do", fg="white", bg="black").pack(anchor=CENTER)

    def submit_handler(self):
        current_search_keyword = self.search_keyword.get()
        current_selected_type = self.selected_type.get()
        current_selected_dominant_color = self.selected_dominant_color.get()

        if current_selected_type == "None":
            current_selected_type = ""
        if current_selected_dominant_color == "None":
            current_selected_dominant_color = "imgDominantColorUndefined"

        # print(current_search_keyword)
        # print(current_selected_type)
        # print(current_selected_dominant_color)

        # use google image search service
        # get list of images

        # display images
        self.display_images(mock_images_url)

    def display_images(self, images: list[str]):
        temp_row = 5
        for image_url in images:
            try:
                u = urlopen(image_url) 
                raw_data = u.read()
                u.close()

                # open the image and resize
                im = Image.open(BytesIO(raw_data)).resize((300, 100))

                photo = ImageTk.PhotoImage(im)
                label = tk.Label(image=photo)
                label.image = photo
                label.grid(row=temp_row, column=0, padx=5, pady=5, columnspan=100)

                temp_row += 1
            except:
                pass

    def run(self):
        self.mainloop()


if __name__ == "__main__":
    UI = PaeProject()
    UI.run()