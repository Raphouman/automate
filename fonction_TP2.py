
#dico des mots avec leurs classes (article= classe 0, adjectif=1, nom=2, verbe=3, nom propre=4, point=5)
dictionnaire ={"le" : 0, "la" : 0, "chat" : 2, "souris" : 2, "martin" : 4,
"mange" : 3, "la" : 0, "petite" : 1, "joli" : 1, "grosse" : 1,
"bleu" : 1, "verte" : 1, "dort" : 3,"julie" : 4, "jean" : 4, "." : 5}

#tableau qui lie les états entre eux, il permet de savoir en fonction de ce qu'on trouve dans la phrase et  à quel état cela nous renvoie
tableau_de_transition= [[1,8,8,8,4,8],
                        [8,1,2,8,8,8],
                        [8,2,8,3,8,8],
                        [5,8,8,8,7,9],
                        [8,8,8,3,8,8],
                        [8,5,6,8,8,8],
                        [8,6,8,8,8,9],
                        [8,8,8,8,8,9],
                        [0,0,0,0,0,0],
                        [0,0,0,0,0,0],]

#définition de l'alphabet des sorties, ici les états : 8= phrase incorrecte et 9= phrase correcte
tableau_sortie=[8,9]

#définition de l'alphabet des entrées, déjà explicitées au dessus
tableau_entree= [0,1,2,3,4,5]

#défintion de l'alphabet des états, attention les états ne sont pas des objets forcément définissable. Ex : l'état 1 n'est pas la même chose que l'entrée 1 qui correspond à un adjectif
tableau_etat= [0,1,2,3,4,5,6,7,8,9]

#définition de l'alphabet des sorties, qui aide à dire si la phrase est bonne ou fausse syntaxiquement parlant
sortie= ["syntaxiquement incorrecte", "syntaxiquement correcte"]

#FONCTION

def transition(etat,classe): #fonction qui renvoie en sortie l'état voulu, entrée : valeur d'entrée (article ou nom ...) et l'état  dans lequel on est
    return tableau_de_transition[etat][classe]


def decoder(phrase): #fonction qui sépare la phrase en une liste de mots. entrée : la phrase, sortie : liste des classes des mots préalablement séparés
    liste_mot= phrase.split()
    return [dictionnaire[i] for i in liste_mot]




def reponse(s):           #fonction qui retourne en sortie si la phrase est correcte ou non avec une courte phrase. entrée = état de sortie
    if s== tableau_sortie[0]:
        return sortie[0]         #retourne "syntaxiquement incorrecte"
    else:
        return sortie[1]        #retourne "syntaxiquement correcte"



def automate(phrase):       #fonction représentant l'automate qui retourne en sortie l'état finale (8 ou 9) de si la phrase est correcte ou non. entrée : la phrase en question
    etat=0
    while etat<8:       #on initialise l'état à 0 pour commencer le test depuis le début, et tant que l'état est différent de 8 ou de 9 (donc tant que la phrase n'est pas "jugeable"), on continue de vérifier la phrase
        for i in range (len(decoder(phrase))):
            etat= transition(etat,decoder(phrase)[i])
    else:
        print("La phrase est ", reponse(etat))


#phrase="le joli chat mange ." #le point doit être séparé d'un espace avec le dernier mot
#La fonction map() est une fonction intégrée en Python qui permet d’appliquer une fonction à chaque élément d’un itérable (par exemple, une liste) et de retourner un nouvel itérable contenant les résultats.
#La fonction split permet, à partir d'une chaîne de caractères, de la couper en petits morceaux, chaque morceau étant séparé des autres par une espace. La fonction renvoie un tableau de mots, auxquels on peut alors accéder de manière classique.