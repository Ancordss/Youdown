#funciones adicionales
import os
import tkinter, filedialog
import re
root = tkinter.Tk() #esto se hace solo para eliminar la ventanita de Tkinter 
root.withdraw() #ahora se cierra 
file_path = filedialog.askopenfilename() #abre el explorador de archivos y guarda la seleccion en la variable!








def open():
    #os.system("nemo")
    try:
        fp = open("Functions")
    except PermissionError:
        return "some default data"
    else:
        with fp:
            return fp.read()

open() 
