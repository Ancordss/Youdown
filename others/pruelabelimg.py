from tkinter import *
from PIL import ImageTk, Image

#root=  Tk()
#root.geometry=("500x500")
#pic=PhotoImage(file="logo1.png")
#label=Label(image=pic)
#label.pack()
#root.mainloop()


#prueba insert desde URL
#root=Tk()
#root.geometry=("500x500")
#frame=Frame(root)
#frame.config(background="black")
#frame.pack()


#img=ImageTk.PhotoImage(Image.WEB(str("https://upload.wikimedia.org/wikipedia/commons/3/39/AiryBi_Imag_Surface.png")))
#myimg=Label(image=img)
#myimg.pack()
#root.mainloop()



#def getimage(photo):
 #   """Copies the contents of a PhotoImage to a PIL image memory."""
  #  im = Image.new"RGBA", (photo.width(), photo.height()))
   # block = im.im

    #photo.tk.call("https://upload.wikimedia.org/wikipedia/commons/3/39/AiryBi_Imag_Surface.png", photo, block.id)

    #eturn im
imgs=int(input("ingresa el link: "))

li=str(imgs)
img=ImageTk.PhotoImage(Image.open(li))

myimg=ImageTk.PhotoImage(Image.open("/media/anco/Disk/Progra/Youtobe Dowloader/1.png"))
mylabimg=Label(frame1, background="black", image=myimg)
mylabimg.pack()

