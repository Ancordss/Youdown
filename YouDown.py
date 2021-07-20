from tkinter import *
from tkinter import messagebox
from youtube import Video
from youtube.__main__ import Video
from PIL import ImageTk,Image
from Functions.funtions import open, salirapp, licencia, acercade



root=Tk()
root.geometry("500x500")
root.title("YouDown By Anco")
menu_bar=Menu(root)
root.config(menu=menu_bar, width=100, height=100, background="grey")



#-------------agregando a barra------------------
file_menu=Menu(menu_bar, tearoff=0)
file_menu.add_command(label="abrir ubicacion", command=open)
file_menu.add_command(label="salir", command=salirapp)

info_menu=Menu(menu_bar, tearoff=0)
info_menu.add_command(label="licencia", command=licencia)
info_menu.add_command(label="acerca de",command=acercade)

menu_bar.add_cascade(label="File", menu=file_menu)
menu_bar.add_cascade(label="Info", menu=info_menu)

#----------------frames--------------------------

frame1=Frame(root)
frame1.config(background="grey")
frame1.pack()

#-----------------LOGOLABEL-----------------

myimg=ImageTk.PhotoImage(Image.open("/media/anco/Disk/Progra/Youtobe Dowloader/1.png"))
mylabimg=Label(frame1, background="black", image=myimg)
mylabimg.pack()

#------------------fram2----------------

frame2=Frame(root)
frame2.config(background="grey")
frame2.pack()

#------------------labels--------------
linklabel=Label(frame2, text="Ingrese el link:", background="grey", font="arial 12 bold")
linklabel.grid(row=0, column=0, sticky="e", padx=3, pady=1)


#--------------frame3--------------------





frame3=Frame(root)
frame3.config(background="grey")
frame3.pack()

#------------------------descarga--------------

linkvid=StringVar()
tittle=StringVar()
author=StringVar()

def generate():
    try:
        videoURL=linkvid.get()
        v=Video(videoURL)
        tittle.set(v.title)
        author.set(v.author)
        
    except:
        messagebox.showwarning("YouDown", "Porfavor ingresa un Link")

def downloadlow():

    try:
        link=linkvid.get()
        v= Video(link).streams
        v.fflow.download()
   

        messagebox.showinfo("YouDown", "Descarga Reallizada con exito")
        messagebox.showinfo("YouDown", "if the download is webm try again\nthis error will be solved soon")


    except:

        messagebox.showerror("YouDown", "Ha Ocurrido un Error")


def downloadmid():

    try:
        link=linkvid.get()
        v= Video(link).streams
        v.ffmid.download('~/Downloads')


        messagebox.showinfo("YouDown", "Descarga Reallizada con exito")
        messagebox.showinfo("YouDown", "if the download is webm try again\nthis error will be solved soon")

    except:

        messagebox.showerror("YouDown", "Ha Ocurrido un Error")

def downloadhight():

    try:
        link=linkvid.get()
        v= Video(link).streams
        v.ffhigh.download()


        messagebox.showinfo("YouDown", "Descarga Reallizada con exito")
        messagebox.showinfo("YouDown", "if the download is webm try again\nthis error will be solved soon")

    except:

        messagebox.showerror("YouDown", "Ha Ocurrido un Error")







#---------------entrada de link-----------frame3
picturelink=Entry(frame3, width=45, textvariable=linkvid,)
picturelink.grid(row=0, column=1, padx=10, pady=10)

generatebutton=Button(frame3, text="Load", font="arial 12 bold", bg="grey", command=generate)
generatebutton.grid(row=0, sticky="w", column=2, padx=5, pady=5)

inf_video=Entry(frame3, width=40, textvariable=tittle, background="grey")
inf_video.grid(row=1, column=1, padx=10, pady=10)




#-------------------boton--------------
frame4=Frame(root)
frame4.config(background="grey")
frame4.pack()

label_info=Label(frame4,text="click on the desired quality to download", background="grey",font="arial 12 bold")
label_info.grid(row=0, sticky="s", padx=3, pady=3)

Frame4_1=Frame(root)
Frame4_1.config(background="grey")
Frame4_1.pack()
      
DownloadLow=Button(Frame4_1,text="Low", font="arial 12 bold", bg ="grey", command=downloadlow)
DownloadLow.grid(row=0, column=0, sticky="n", padx=10, pady=10, )

Downloadmid=Button(Frame4_1,text="Mid", font="arial 12 bold", bg ="grey", command=downloadmid)
Downloadmid.grid(row=0, column=1, sticky="n", padx=10, pady=10, )

Downloadhight=Button(Frame4_1,text="Hight", font="arial 12 bold", bg ="grey", command=downloadhight)
Downloadhight.grid(row=0, column=2, sticky="n", padx=10, pady=10, )



root.mainloop()


