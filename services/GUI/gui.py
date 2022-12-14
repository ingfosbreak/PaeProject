from tkinter import *

main = Tk()
# main.title("PaeProgram")
main.geometry("1000x600")


# frame = Frame(main)
# frame.pack()


leftFrame = Frame(main, bg="red")
leftFrame.pack(side=LEFT)
rightFrame = Frame(main, bg="white")
rightFrame.pack(side= RIGHT)

Label(leftFrame).pack(pady=600,padx=200)
Label(rightFrame).pack(pady=600,padx=800)

# firstName = Entry(main)
# lastName = Entry(main)

# firstName.grid(row=0, column=1)
# lastName.grid(row=1, column=1)

main.mainloop()