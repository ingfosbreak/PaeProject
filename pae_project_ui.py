import tkinter as tk
from tkinter import ttk, RIGHT, BOTTOM, Y, X, NO, CENTER


class PaeProject(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("PaeProject")

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

    def submit_handler(self):
        current_search_keyword = self.search_keyword.get()
        current_selected_type = self.selected_type.get()
        current_selected_dominant_color = self.selected_dominant_color.get()

        if current_selected_type == "None":
            current_selected_type = ""
        if current_selected_dominant_color == "None":
            current_selected_dominant_color = "imgDominantColorUndefined"

        print(current_search_keyword)
        print(current_selected_type)
        print(current_selected_dominant_color)
        # use google image search service

    def run(self):
        self.mainloop()


if __name__ == "__main__":
    UI = PaeProject()
    UI.run()