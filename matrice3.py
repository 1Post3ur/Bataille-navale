l1 = "E8"


def Traitement(value):
    liste = []
    if len(value) == 1:
        liste.append(l1[0])
        liste.append(l1[1])
    # elif len(value) == 2:
    #     liste.append(l1[0])
    #     liste.append(l1[1] + l1[2])
    else : 
        pass
    
    
    liste[0] = ord(liste[0])-64
    

    
    
    
    return liste

liste = Traitement(l1)    
print(liste)
