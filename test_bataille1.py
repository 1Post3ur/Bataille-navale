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
c1= Canvas(fn, width=700, height=700, bg="black", bd=0, highlightthickness=0)
c1.create_image(x/2,y/2, image=bg)
c1.pack()
#
# c2= Canvas(fn, width=700, height=700, bg="black", bd=0, highlightthickness=0)
# c2.create_image(x/2,y/2, image=bg)
# c2.pack()
#

def quitter():
    if messagebox.askokcancel("Quitter", "Voulez-vous vraiment quitter ?"):
        fn.destroy()

fn.protocol("WM_DELETE_WINDOW", quitter)







#
# ~~~~~~~~~~~~~~~~Input des positions des bateaux~~~~~~~~~~~~~~~~~~

#
# def pos_to_coord() :
#     bt1 = []
#     bt1.append(bat1[0])
#     bt1.append(bat1[1])
#     print(bt1)
#
#
#
# def input_coord() :
#     print("DONNER LES COORDONNEES SOUS LA FORME 1 lettre 1 chiffre , ex : A9")
#     bat1= input("Position du bateau 1 (2 blocs?) : ")
#     pos_to_coord()
#


fn.mainloop()



