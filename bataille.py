import random
from random import *
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk



fn = Tk()
fn.title("Batalle navale")
fn.config(width=700, height=700, background="black")

x=700
y=700

#background
bg=ImageTk.PhotoImage(Image.open("Capture4.jpg"))
c1= Canvas(fn, width=650, height=650, bg="black", bd=0, highlightthickness=0)
c1.create_image(x/2,y/2, image=bg)
c1.pack()




# ~~~~~~~~~~~~~~~~Input des positions des bateaux~~~~~~~~~~~~~~~~~~

print("DONNER LES COORDONNEES SOUS LA FORME 1 lettre 1 chiffre , ex : A9")
bt1= input("Position du bateau 1 (2 blocs?) : ")



def pos_to_coord() :
    bt1 = []
    bt1.append(bt1[0])
    bt1.append(bt1[1])
    print(bt1)    

pos_to_coord()



fn.mainloop()
