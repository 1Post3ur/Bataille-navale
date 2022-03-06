import numpy
from numpy import *
import random
from random import choice, randint
import tkinter
from tkinter import *
from tkinter import messagebox


#   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Variables et listes à Définir~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# on crée les deux grilles sous formes d'arrays remplis de zéros
grille_joueur = numpy.zeros((10 , 10))
grille_ia = numpy.zeros((10 , 10))

# on associe les id des bateaux à des couleurs pour pouvoir les appeller et les modifier

liste_couleurs_bateaux = {'1': 'purple',
                          '2': 'light blue',
                          '3': 'dark green',
                          '4': 'yellow',
                          '5': 'orange',
                          '7': 'black',
                          '6': 'grey',
                          '11': 'red',
                          '12': 'red',
                          '13': 'red',
                          '14': 'red',
                          '15': 'red'}

alphabet = "ABCDEFGHIJ"


#   ~~~~~~~~~~~~~~~~~~~~Fonctions et code exécutés au lancement du jeu (pour créer la fenêtre et les bateaux~~~~~~~~~~~~~~~~~~~~~~~~


# fonction qui sert à généerer les bateaux selon leur grille, leur id (numéro pour les identifier) et leur longueur
def generate_bateau(id_bat, length, grille):
    # variable test sert à vérifier si les bateaux ne se superposent pas à l'aide de la boucle while
    test = False

    while test == False:

        orientation = randint(0, 1)     # 0 : horizontal --- 1 : vertical

        # additionne les cases du bateaux en fonction de l'orientation (horizontale ou verticale)
        if orientation == 0:
            lxc = range(1, 10 - length, 1) # liste des coords x possibles pour la premiere case du bateau
            lyc = range(1, length, 1) # liste des coords y possibles
            # on enlève la longueur du bateau aux coords possibles pour éviter que le bateau ne dépasse de la grille

        else: # même chose si on développe le bateau à la verticale
            lxc = range(1, length, 1)
            lyc = range(1, 10 - length, 1)


        #on choisit les coords aléatoires à partir des listes lxc et lyc et on les enregistre dans pbat
        x = choice(list(lxc))
        y = choice(list(lyc))
        pbat = [(x, y)]

        #création des autres cases du bateau en fonction de son orientation
        for i in range(1, length):
            if orientation == 0:
                pbat.append((x + i, y))
            else:
                pbat.append((x, y + i))

        # Vérifie si deux bateaux sont sur la même case

        somme = 0 #pour cela on fait l'addition des la valeur de toutes las cases qui vont etre occupées par le bateau

        for i in range(length):
            somme = somme + grille[pbat[i]]
        #si ces cases ne sont pas occupées le résultat devrait être 0
        #si ce n'est pas le cas, la génération du bateau recommence jusqu'à ce que les cases soient vides

        if somme == 0:
            test = True

    # On place les coordonnées sur la grille en remplacant le 0 de chaque case par leur id
    for i in range(length):
        grille[pbat[i]] = id_bat


#on génère l'ensemble des bateaux

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





#   ~~~~~~~~~~~~~~~~~~~Partie Tkinter~~~~~~~~~~~~~~~~~~~~~~~~~~~

# On génère l'ensemble de la fenêtre tkinter avec les grilles, textes, ...

fn = Tk()
fn.title = "Bataille navale"
fn.geometry('1130x900+50+50')
fn.configure(bg='white')





canvas = Canvas(fn, width=560, height=530, background="white") #le premier canva correspond à la grille de joueur

j = 1 #variable utilisée pour écrire les titres des lignes et colonnes (chiffres et lettres)

#boucle où l'on crée les lignes de la grille et les titres des lignes et colonnes
for i in range(30, 560, 50):
    canvas.create_line(i, 30, i, 530)
    canvas.create_line(30, i, 530, i)

    canvas.create_text(15, i + 25, text="%d" % (j), fill="green", font=('Helvetica 12 bold'))
    if (j <= 10):
        canvas.create_text(i + 25, 15, text=alphabet[j - 1], fill="green", font=('Helvetica 12 bold'))
    j = j + 1




canvas2 = Canvas(fn, width=560, height=530, background="white") #le deuxième canva correspond à la grille de la machine

j = 1

for i in range(30, 560, 50):
    canvas2.create_line(i, 30, i, 530)
    canvas2.create_line(30, i, 530, i)

    canvas2.create_text(545, i + 25, text="%d" % (j), fill="green", font=('Helvetica 12 bold'))
    if (j <= 10):
        canvas2.create_text(i + 25, 15, text=alphabet[j - 1], fill="green", font=('Helvetica 12 bold'))

    j = j + 1


#   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# fonction qui sert à afficher les bateaux sur la grille en fonction de leur id et de la grille sur laquelle on veut les afficher (joueur, ia)

# la fonction recherche dans l'array valeur par valeur si une correspond à l'id donné et remplit  la fenetre tkiinter avec

def remplir_bateaux(id_bat, grille):
    for i in range(0, 10):
        for j in range(0, 10):
            px = j * 50 + 30 + 25 #position relative dans l'abscisse l'affichage graphique
            py = i * 50 + 30 + 25 #position relative dans l'abscisse l'affichage graphique
            if grille[i][j] == id_bat:
                if str(grille) == str(grille_joueur):
                    canvas.create_oval(px - 10, py - 10, px + 10, py + 10, fill=liste_couleurs_bateaux[str(id_bat)])
                else:
                    canvas2.create_oval(px - 10, py - 10, px + 10, py + 10, fill=liste_couleurs_bateaux[str(id_bat)])


remplir_bateaux(1, grille_joueur)
remplir_bateaux(2, grille_joueur)
remplir_bateaux(3, grille_joueur)
remplir_bateaux(4, grille_joueur)
remplir_bateaux(5, grille_joueur)


#   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Fonctions exécutes lorsque les joueurs jouent~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# sert à traiter la coordonnée donnée par l'utilisateur dans la case input pour attaquer
def Traitement(value):
    value = value.upper()
    liste = []
    if len(value) == 2:
        liste.append(value[0])
        liste.append(int(value[1]) - 1)
    elif len(value) == 3:
        liste.append(value[0])
        liste.append(10 - 1)
        print(liste)
    else:
        print("Erreur dans les coordonnées")
    print("traitement liste[0]=%c ord()=%d" % (liste[0], ord(liste[0])))
    liste[0] = ord(liste[0]) - 65 #on utilise ord qui renvoie le chiffre ascii d'un caractère, ici une lettre
    print(liste)

    return liste


# remplit l'array avec les coordonnées de l'attaque et affiche le point attaqué sur la grille
def attaquer(pbat, grille):
    print("Attaque", alphabet[pbat[0]], " ", pbat[1])
    if grille[pbat[1]][pbat[0]] == 0:
        grille[pbat[1]][pbat[0]] = 6    #si il n'y a rien sur la case elle devient 6 (rien touché)
        id_touché = 6
    else:
        grille[pbat[1]][pbat[0]] = grille[pbat[1]][pbat[0]] + 10 #sinon on ajoute 10 à la valeur ( le bateau 3 devient 13)
        id_touché = grille[pbat[1]][pbat[0]]
        id_touché = int(id_touché)
        print(id_touché)

    print(grille)
    remplir_bateaux(id_touché, grille)


# fonction qui définit le comportement de la machine (amélioration possible dans le futur)

# choisit des coord au hasard (pur l'instant) à  attaquer mais évite d'attaquer une case déjà jouée
def comportement_machine():
    case_non_jouée = False
    while case_non_jouée == False :
        coord_attaquer = []
        coord_attaquer.append(randint(0, 9))
        coord_attaquer.append(randint(0, 9))
        if int(grille_joueur[coord_attaquer[1]][coord_attaquer[0]]) in [0 , 1 , 2 , 3 , 4 , 5 ]: #vérifie que la case n'est pas encore jouée
            print("Machine attaque : ", coord_attaquer)
            case_non_jouée = True
    return coord_attaquer


#fonction qui vérifie si les bateaux d'une grille on coulé

def coulé(grille):
    for x in range(1,6): #verifie pour chaque bateau (1 à 5)
        test = False
        if x in grille : #si on trouve cet id dans la liste alors le bateau n'est pas coulé
            test = True
        if test == False : # si le bateau est coulé
            print("Bateau " + str(x) + " coulé")
            for i in range(0, 10): #on reremplit la grille en remplacant les cases touchées par des 7 (coulé)
                for j in range(0, 10):
                    if grille[i][j] == (x + 10):
                        grille[i][j] = 7
    remplir_bateaux(7, grille) #on actualise l'affichage graphique
    gagné(grille) #appelle directement la fonction qui vérifie si une joueur a gagné


#vérifie si le joueur qui attaque la grille donnée en paramètre a gagné
def gagné(grille):
    test = False
    for i in range(0, 10):
        for j in range(0, 10):
            if grille[i][j] not in [0, 6, 7] :
                test = True
    if test == False :
        if grille is grille_ia:
            print("Gagné")
            rép = messagebox.askokcancel(title="Victoire", message="Tu as gagné \n Veux-tu quitter")
            print(rép)
            fin(rép)
        else :
            print("Perdu")
            rép = messagebox.askokcancel(title="Défaite", message="Tu as perdu \n Veux-tu quitter")
            print(rép)
            fin(rép)

#fonction utilisée pour les tests (voir fonction valider()) elle remplace toutes les valeurs de l'array par 0
def effacer(grille):
    for i in range(0, 10):
        for j in range(0, 10):
            grille[i][j] = 0

#ferme la fenêtre et arrête le programme si l'utilisateur le demande à la fin de la partie
def fin(rép):
   if rép == True:
        print("Quitter")
        fn.destroy()
        exit()

#demande à l'utilisateur si il est sûr de voiloir quitter
def quitter():
    if messagebox.askokcancel("Quitter", "Voulez-vous vraiment quitter ?"):
        fn.destroy()
        exit()

fn.protocol("WM_DELETE_WINDOW", quitter)

# ---------------------------------------------------------

# fonction qui est déclenchée par le bouton d'attaque et qui gère les tours en appellant diverse fonctions
def valider(*bouton_pressé):

    coord_attaquer = entry.get() #récupère la valeur de l'input d'attaque
    print(coord_attaquer)

    #~~~~~Partie test (il y a des codes qui font des actions spécifiques pour tester le code et résoudre des erreurs
    if coord_attaquer == "42":  # le code 42 fait gagner l'utilisateur
        effacer(grille_ia)
        gagné(grille_ia)
    elif coord_attaquer == "24":    # le code 24 fait gagner la machine
        effacer(grille_joueur)
        gagné(grille_joueur)
    elif coord_attaquer == "99":    # le code 24 affiche les bateaux de la machine sur la grille
        remplir_bateaux(1, grille_ia)
        remplir_bateaux(2, grille_ia)
        remplir_bateaux(3, grille_ia)
        remplir_bateaux(4, grille_ia)
        remplir_bateaux(5, grille_ia)
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    else : #tour normal

        coord_attaquer = Traitement(coord_attaquer) #interprète l'inpu de l'utilisateur
        if int(grille_ia[coord_attaquer[1]][coord_attaquer[0]]) in [0, 1, 2, 3, 4, 5]: #vérifie que son attaque n'a pas déjà été jouée
            attaquer(coord_attaquer, grille_ia)
            coulé(grille_ia)
            coord_attaquer = comportement_machine() #demande des coords à attaquer pour la machine
            attaquer(coord_attaquer, grille_joueur)
            coulé(grille_joueur)
        else :
            print("Coordonnée déjà jouée")
            messagebox.showinfo(title="Erreur", message="Vous avez déjà joué cette coordonnée")
    entry.delete(0, END)



#   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



# Crée las widgets,...

txt = Label(text="Attaquer")
entry = Entry(fn, bd=5)
entry.insert(END, 'Coords (ex : B5)')
btn = Button(fn, bd=5, text="Valider", command=valider)
txt.pack(side='top')
entry.pack(side='top')
btn.pack(side='top')



canvas.pack(side='left')
canvas2.pack(side='left')

btn.bind_all('<KeyPress-Return>', valider)#Permer de lier le pression de la touche entrée à la fonction valider (donc au bouton valider)


#   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

print(grille_joueur)
print("\n\n\n\n")
print(grille_ia)

fn.mainloop()