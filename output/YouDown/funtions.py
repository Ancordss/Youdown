#funtions
import os
import tkinter
from tkinter import messagebox
from youtube import Video



def open():# open a download library
    try:
        os.system("nemo ~/Downloads")
    except:
        messagebox.showerror("YouDown", "Ups algo a fallado,\n busca en donde esta el archivo")

def salirapp():#close the aplication
	valor=messagebox.askquestion("salir", "¿deseas salir de la aplicacion?")

	if valor=="yes":
		exit()

def licencia():
    messagebox.showinfo("YouDown","Licencia en proceso")

def acercade():
    messagebox.showinfo("YouDown","created by Anco\nhttps://github.com/Ancordss ")
