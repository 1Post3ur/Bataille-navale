import numpy
from numpy import *
import random
from random import choice, randint
import tkinter
from tkinter import *
from tkinter import Canvas

taille_grille = 10

grille_joueur = numpy.zeros((taille_grille, taille_grille))
grille_ia = numpy.zeros((taille_grille, taille_grille))

liste_couleurs_bateaux = {'1': 'red', '2': 'light blue', '3': 'dark green', '4': 'yellow', '5': 'orange', 6: 'grey'}


def generate_bateau(id_bat, length, grille):
    test = False

    while test == False:
        orientation = randint(0, 1)

        if orientation == 0:
            lxc = range(1, taille_grille - length, 1)
            lyc = range(1, length, 1)

        else:
            lxc = range(1, length, 1)
            lyc = range(1, taille_grille - length, 1)

        x = choice(list(lxc))
        y = choice(list(lyc))
        pbat = [(x, y)]

        for i in range(1, length):
            if orientation == 0:
                pbat.append((x + i, y))
            else:
                pbat.append((x, y + i))

        # Vérifie si deux bateaux sont sur la même case

        somme = 0

        for i in range(length):
            somme = somme + grille[pbat[i]]

        if somme == 0:
            test = True

    # On place les coordonnées sur la grille
    for i in range(length):
        grille[pbat[i]] = id_bat


generate_bateau(1, 2, grille_joueur)
generate_bateau(2, 3, grille_joueur)
generate_bateau(3, 4, grille_joueur)
generate_bateau(4, 4, grille_joueur)
generate_bateau(5, 5, grille_joueur)

generate_bateau(1, 2, grille_ia)
generate_bateau(2, 3, grille_ia)
generate_bateau(3, 4, grille_ia)
generate_bateau(4, 4, grille_ia)
generate_bateau(5, 5, grille_ia)

######## ~~~~~~~~~~~~~~~~ PARTIE TKINTER ~~~~~~~~~~~~~~~~~~~~

fn = Tk()
fn.title = "Bataglia navale"
fn.geometry('1130x900+50+50')
fn.configure(bg='white')

canvas = Canvas(fn, width=560, height=530, background="white")

for i in range(30, 560, 50):
    canvas.create_line(i, 30, i, 530)
    canvas.create_line(30, i, 530, i)
    canvas.create_text(15, i + 25, text="I", fill="green", font=('Helvetica 12 bold'))
    canvas.create_text(i + 25, 15, text="II", fill="green", font=('Helvetica 12 bold'))

canvas2 = Canvas(fn, width=560, height=530, background="white")

for i in range(30, 560, 50):
    canvas2.create_line(i, 30, i, 530)
    canvas2.create_line(30, i, 530, i)
    canvas2.create_text(545, i + 25, text="I", fill="green", font=('Helvetica 12 bold'))
    canvas2.create_text(i + 25, 15, text="II", fill="green", font=('Helvetica 12 bold'))


def remplir_bateaux(id_bat):
    for i in range(0, 9):
        for j in range(0, 9):
            px = j * 50 + 30 + 25
            py = i * 50 + 30 + 25
            if grille_joueur[i][j] == id_bat:
                print(px, py)
                canvas.create_oval(px - 10, py - 10, px + 10, py + 10, fill=liste_couleurs_bateaux[str(id_bat)])


remplir_bateaux(1)
remplir_bateaux(2)
remplir_bateaux(3)
remplir_bateaux(4)
remplir_bateaux(5)

inpt = StringVar()

def Traitement(value):
    value = value.upper()
    liste = []
    if len(value) == 2:
        liste.append(value[0])
        liste.append(int(value[1]))
    elif len(value) == 3:
        liste.append(value[0])
        liste.append(int(value[1] + value[2]))
    else:
        pass

    liste[0] = ord(liste[0]) - 65

    return liste


def attaquer(pbat):
    grille_ia[pbat[0]][pbat[1]] = 6
    for i in range(0, 9):
        for j in range(0, 9):
            px = j * 50 + 30 + 25
            py = i * 50 + 30 + 25
            if grille_ia[i][j] == 6:
                print(px, py)
                canvas2.create_oval(px - 10, py - 10, px + 10, py + 10, fill='grey')



def valider():
    coord_attaquer = entry.get()
    print(coord_attaquer)
    coord_attaquer = Traitement(coord_attaquer)
    attaquer(coord_attaquer)


txt = Label(text="Attaquer")
entry = Entry(fn, bd=5)
entry.insert(END, 'Coords (ex : B5)')
btn = Button(fn, bd=5, text="Valider", command=valider)
txt.pack(side='top')
entry.pack(side='top')
btn.pack(side='top')

canvas.pack(side='left')
canvas2.pack(side='left')



#   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

print(grille_joueur)
print("\n\n\n\n")
print(grille_ia)






fn.mainloop()