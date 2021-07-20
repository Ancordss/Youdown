from tkinter import *

root=  Tk()
root.geometry=("500x500")
pic=PhotoImage(file="logo1.png")
label=Label(image=pic)
label.pack()
root.mainloop()
