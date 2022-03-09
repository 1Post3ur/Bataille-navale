_Rémi FUNES_
## Projet Python
## Bataille Navale

&nbsp;

###### Le jeu fonctionne à partir de deux arrays (contenant chacun 10 listes de 10 valeurs représentant les lignes et colonnes) qui sont à l'origine remplis de zeros.

###### Les arrays utilisés viennent du module [NumPy][numpy].

###### Ces arrays sont ensuites modifiées de manière y remplacer les 0 par d'autres chiffres (des id) représentant les bateaux et leurs états. Il sont notées dans le code à l'aide de la variable ou du paramètre id_bat 

_Lien du [jeu][jeu]_

&nbsp;

#### Id des bateaux :

- __1, 2, 3, 4, 5 :__ Case occupée par un bateau (par exemple le bateau 1 occupe les cases contenant un 1) __(couleurs multiples : vert, violet, ...)__

- __11, 12, 13, 14, 15 :__ Case occupée par un bateau mais touché par l'autre joueur __(rouge)__

- __6 :__ Case attaquée mais vide __(gris)__

- __7 :__ Case occupée par un bateau coulé __(noir)__

###### _Un dictionnaire sert aussi à lier les id à des couleurs, servant dans l'affichage graphique tkinter à les différencier_

&nbsp;

### Fonctionnalités supplémentaires :

• Demande de confirmation avant de fermer la fenêtre
```sh
def quitter():
    if messagebox.askokcancel("Quitter", "Voulez-vous vraiment quitter ?"):
        fn.destroy()
        exit()

fn.protocol("WM_DELETE_WINDOW", quitter)
```
• Message affiché lors d'une Victoire ou d'une défaite _(ce message propose de quitter la fenêtre)_
def quitter():
```sh
if grille is grille_ia:
            print("Gagné")
            rép = messagebox.askokcancel(title="Victoire", message="Tu as gagné \n Veux-tu quitter ?")
            print(rép)
            fin(rép)
        else :
            print("Perdu")
            rép = messagebox.askokcancel(title="Défaite", message="Tu as perdu \n Veux-tu quitter ?")
            print(rép)
            fin(rép)

def fin(rép):
   if rép == True:
        print("Quitter")
        fn.destroy()
        exit()
```

• Le joueur et la machine ne peuvent pas rejouer une case déjà jouée
```
def comportement_machine():
    case_non_jouée = False
    while case_non_jouée == False :
        coord_attaquer = []
        coord_attaquer.append(randint(0, 9))
        coord_attaquer.append(randint(0, 9))
        if int(grille_joueur[coord_attaquer[1]][coord_attaquer[0]]) in [0 , 1 , 2 , 3 , 4 , 5 ]:
        #vérifie que la case n'est pas encore jouée
            print("Machine attaque : ", coord_attaquer)
            case_non_jouée = True
    return coord_attaquer
```
• La pression de la touche <kbd>Enter</kbd> permet aussi de valider la coordonnée que l'on attaque
```sh
btn.bind_all('<KeyPress-Return>', valider)
# Découverte de args* et kwargs** dans la fonction valider qui prenait donc un paramètre en trop
```

• L'input d'une coordonnée à attaquer se vide automatiquement après validation

```sh
entry.delete(0, END)
```


### Codes de triche

> A utiliser pour tester certaines fonctionnalités du jeu
(les rentrer dans l'input de coordonnées à attaquer)

• `42` : Permet de faire gagner le joueur automatiquement

• `24` : Permet de faire gagner la machine automatiquement

• `99` : Permet d'afficher les bateaux ennemis

   [numpy]: <https://numpy.org/>
   [jeu]: <https://github.com/joemccann/dillinger.git>
