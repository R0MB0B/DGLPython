from Jeu import *

# jeu=Board(6,7)
# jouer=True
# while jouer==True:
#     jeu.print()
#     jeu.play(input("quelle couleur ?"), input("quelle colonne ?"))
#     jeu.print()
#     jouer=bool(input("\n continuer ?"))
    

jeu=Board(6,7)
jouer='oui'
couleur=input("Qui commence ?")
while jouer=='oui':
    jeu.print()
    jeu.play(couleur, input("\n Colonne : "))
    jeu.print()
    jouer=input("continuer ? ")
    if couleur=='Rouge':
        couleur='Jaune'
    else:
        couleur='Rouge'