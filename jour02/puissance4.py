import pandas as pd
import numpy as np

class Board():
    def __init__(self, i, j, debutant):
        self.i=i
        self.j=j
        self.plateau=np.full((i,j),'O')
        self.couleur=debutant
    
    def geti(self):
        return self.i

    def getj(self):
        return self.j

    def play(self, couleur, colonne):
        col=int(colonne)
        jeton=""
        if str(couleur)=='Rouge':
            jeton="R"
        if str(couleur)=='Jaune':
            jeton='J'
        self.placePieceLigne(col, jeton, self.i)

    def placePieceLigne(self,col,jeton,ligne):
        if self.plateau[ligne-1][col-1]=='O':
            self.plateau[ligne-1][col-1]=str(jeton)
        else:
            self.placePieceLigne(col, jeton, ligne-1)
        
    def commencer(self):
        self.print()  
        continuer=True
        while continuer==True:
            self.play(self.couleur, input("\n Colonne : "))
            self.print()    
            if self.couleur=='Rouge':
                self.couleur='Jaune'
            else:
                self.couleur='Rouge'
            continuer=self.etat()
        print(continuer)

    def etat(self):
        i=self.i
        j=self.j
        compteurLigne=[0 for x in range(0,i)] ## positif Pour rouge, negatif pour jaune
        compteurColonne=[0 for x in range(0,j)]
        for ligne in range(i):
            for colonne in range(j):
                if self.plateau[ligne][colonne]=='R' and compteurLigne[ligne]>=0:
                    compteurLigne[ligne]+=1
                    if compteurLigne[ligne]==4:
                        return("Le joueur Rouge a gagné")
                if self.plateau[ligne][colonne]=='J' and compteurLigne[ligne]<=0:
                    compteurLigne[ligne]-=1
                    if compteurLigne[ligne]==-4:
                        return("Le joueur Jaune a gagné")
                else:
                    compteurLigne[ligne]=0

        for colonne in range(j):
            for ligne in range(i):
                if self.plateau[ligne][colonne]=='R' and compteurColonne[colonne]>=0:
                    compteurColonne[colonne]+=1
                    if compteurColonne[colonne]==4:
                        return("Le joueur Rouge a gagné")
                if self.plateau[ligne][colonne]=='J' and compteurColonne[colonne]<=0:
                    compteurColonne[colonne]-=1
                    if compteurColonne[colonne]==-4:
                        return("Le joueur Jaune a gagné")
                else:
                    compteurColonne[colonne]=0

        for ligne in range(3,i):
            for colonne in range(0,j-3):
                    if self.plateau[ligne][colonne]==self.plateau[ligne-1][colonne+1]==self.plateau[ligne-2][colonne+2]==self.plateau[ligne-3][colonne+3]:
                        if self.plateau[ligne][colonne]=='R':
                            return("Le joueur Rouge a gagné")
                        if self.plateau[ligne][colonne]=='J':
                            return("Le joueur Jaune a gagné")

        for ligne in range(3,i):
            for colonne in range(3,j):
                    if self.plateau[ligne][colonne]==self.plateau[ligne-1][colonne-1]==self.plateau[ligne-2][colonne-2]==self.plateau[ligne-3][colonne-3]:
                        if self.plateau[ligne][colonne]=='R':
                            return("Le joueur Rouge a gagné")
                        if self.plateau[ligne][colonne]=='J':
                            return("Le joueur Jaune a gagné")
        return True
                                            
    def print(self):
        # print('\n',self.plateau)
        print('\n',pd.DataFrame(self.plateau, columns=list('1234567'))) ## il faut utiliser un interpréteur contenant pandas

jeu=Board(6,7,'Jaune')
jeu.commencer()