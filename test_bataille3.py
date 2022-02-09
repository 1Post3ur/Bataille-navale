import random
from random import randint
import time
from time import sleep
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk



fn = Tk()
fn.title("Batalle navale")
fn.config(width=1400, height=700, background="black")

x=700
y=700

#background
bg=ImageTk.PhotoImage(Image.open("Capture4.jpg"))
c1= Canvas(fn, width=1400, height=700, bg="black", bd=0, highlightthickness=0)
c1.create_image(x/2,y/2, image=bg)
c1.pack()

def quitter():
    if messagebox.askokcancel("Quitter", "Voulez-vous vraiment quitter ?"):
        fn.destroy()

fn.protocol("WM_DELETE_WINDOW", quitter)



#####INPUT###### VAR : B1, B2 ... = TXT ; BAT1, BAT2, ... = Position bateaux


B1 = Label(fn, text="POS BAT1", bd=5)
B1.pack(side = LEFT, padx=15)
BAT1 = Entry(fn, bd =5)
BAT1.pack(side = LEFT)

B2 = Label(fn, text="POS BAT2", bd=5)
B2.pack(side = LEFT, padx=15)
BAT2 = Entry(fn, bd =5)
BAT2.pack(side = LEFT)

B3 = Label(fn, text="POS BAT3", bd=5)
B3.pack(side = LEFT, padx=15)
BAT3 = Entry(fn, bd =5)
BAT3.pack(side = LEFT)



######## Traitement de coordonnées ##############

bt1 = []
bt2 = []
bt3 = []
bt4 = []
bt5 = []

def Traitement():
    bt1.append(BAT1[0])
    bt1.append(BAT1[1])
    bt2.append(BAT2[0])
    bt2.append(BAT2[1])
    bt3.append(BAT3[0])
    bt3.append(BAT3[1])




#######

Bouton_fin = Button(fn,text='Valider',command=Traitement)
Bouton_fin.pack(padx=5,pady=5)


fn.mainloop()



