# print("DONNER LES COORDONNEES SOUS LA FORME 1 lettre 1 chiffre , ex : A9")
#
#
#
# def input_coord() :
#     bat1 = input("Position du bateau %s : " % nb_bateau)
#     pos_to_coord()
#
# def pos_to_coord() :
#     bt1 = []
#     bt1.append(bat1[0])
#     bt1.append(bat1[1])
#
#
# for nb_bateau in range(4):
#     input_coord()
#
# for i in range(4):
#     print(bt1)
#

#-------------------------------------------------------------------

bt1 = []
bt2 = []
bt3 = []
bt4 = []
bt5 = []

def pos_to_coord() :
    bat1 = input("Position du bateau 1 (2 blocs?) : ")
    bt1.append(bat1[0])
    bt1.append(bat1[1])
    print(bt1)



print("DONNER LES COORDONNEES SOUS LA FORME 1 lettre 1 chiffre , ex : A9")

pos_to_coord()
