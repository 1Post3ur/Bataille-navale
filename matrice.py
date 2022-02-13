import numpy
from numpy import *
import random
from random import choice, randint
import tkinter
from tkinter import *
from tkinter import Canvas

taille_grille = 10

grille_joueur = numpy.zeros((taille_grille,taille_grille))
grille_ia = numpy.zeros((taille_grille,taille_grille))


def generate_bateau(id_bat, length, grille):

    test = False

    while test == False :
        orientation = randint(0,1)

        if orientation == 0 :
            lxc = range(1, taille_grille - length, 1)
            lyc = range(1, length, 1)

        else :
            lxc = range(1, length, 1)
            lyc = range(1,taille_grille-length,1)

        x = choice(list(lxc))
        y = choice(list(lyc))
        pbat = [(x, y)]


        for i in range(1, length):
            if orientation==0:
                pbat.append((x + i, y))
            else:
                pbat.append((x, y + i))

        # Vérifie si deux bateaux sont sur la même case

        somme = 0

        for i in range(length):
            somme = somme + grille[pbat[i]]

        if somme == 0 :
           test = True



    #On place les coordonnées sur la grille
    for i in range(length) :
        grille[pbat[i]] = id_bat


generate_bateau(1,2, grille_joueur)
generate_bateau(2,3, grille_joueur)
generate_bateau(3,4, grille_joueur)
generate_bateau(4,4, grille_joueur)
generate_bateau(5,5, grille_joueur)

generate_bateau(1,2, grille_ia)
generate_bateau(2,3, grille_ia)
generate_bateau(3,4, grille_ia)
generate_bateau(4,4, grille_ia)
generate_bateau(5,5, grille_ia)

######## ~~~~~~~~~~~~~~~~ PARTIE TKINTER ~~~~~~~~~~~~~~~~~~~~

# fn = Tk()
# fn.title = "Bataglia navale"
#
# canvas = Canvas(fn, width = 530, height = 530, background = "white")
#
# for i in range(30,530,50):
#     canvas.create_line(i, 30, i, 530)
#     canvas.create_line(30, i, 530, i)
#     canvas.create_text(15, i + 25, text="I", fill="green", font=('Helvetica 12 bold'))
#     canvas.create_text(i + 25, 15, text="II", fill="green", font=('Helvetica 12 bold'))
#
#
#
#
# for i in range(0 , 9):
#     for j in range(0 , 9):
#         px = j * 50 + 30 + 25
#         py = i * 50 + 30 + 25
#         if grille_joueur[i][j] > 0:
#             print(px, py)
#             canvas.create_oval(px-10 , py-10 , px+10 , py+10 , fill = "red")
#
# # TU AIMES LE CACA ???
# # OUI !!!!!
#
# canvas.pack()
#

#   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

print(grille_joueur)
print("\n\n\n\n")
print(grille_ia)

#fn.mainloop()
