from tkinter import *

def round_rectangle(root, x1, y1, x2, y2, radius=25, **kwargs): # Creating a rounded rectangle
        
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


main = Tk()
main.title("PaeProgram")
main.geometry("1000x550")


leftFrame = Frame(main, bg="#FFFFFF",width=400,height=550)
leftFrame.pack(side=LEFT)
rightFrame = Frame(main, bg="#007ea7",width=800,height=550)
rightFrame.pack(side= RIGHT)

canvas = Canvas(leftFrame, bg="#FFFFFF", width=350,height=550,highlightthickness=0)
canvas.place(x=20,y=25)
round_rectangle(canvas,0, 0, 350, 500, radius=70)
# canvas = Canvas(leftFrame, bg="grey", highlightthickness=0)
# canvas.pack(fill=BOTH, expand=1)


Label(canvas, text="Position 1 : x=0, y=0", bg="#DEE5E5", fg="black", font=('Times',24)).place(x=50, y=200)









# firstName = Entry(main)
# lastName = Entry(main)

# firstName.grid(row=0, column=1)
# lastName.grid(row=1, column=1)

main.resizable(False, False) 
main.mainloop()






