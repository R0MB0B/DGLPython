class Personne():
    def __init__(self, prenom, nom):
        self.nom=nom
        self.prenom=prenom
    
    def SePresenter(self):
        print("Mon prenom est "+self.prenom+" et mon nom est "+self.nom)

# p1=Personne('Romain', 'Marlet')
# p1.SePresenter()

class Livre():
    def __init__(self, titre):
        self.titre=titre
    
    def print(self):
        print(self.titre)

    def gettitre(self):
        return(self.titre)


# l1=Livre("Book")
# l1.print()


class Auteur(Personne):
    def __init__(self, nom, prenom):
        self.nom=nom
        self.prenom=prenom
        self.oeuvre=[]
        super().__init__(prenom, nom)

    def listerOeuvre(self):
        return(list(self.oeuvre))

    def ecrireUnLivre(self, titre):
        l=Livre(titre)
        self.oeuvre.append(l)

# a1=Auteur('Marlet', 'Romain', [])
# a1.ecrireUnLivre('Essai')
# print(a1.listerOeuvre())
# print(len(a1.oeuvre))
# print(a1.oeuvre[1].titre)

class Bibliotheque():
    def __init__(self, nom, catalogue):
        self.nom=nom
        self.catalogue=catalogue

    def acheterLivre(self, auteur, nomLivre, quantite):
        oeuvres=auteur.listerOeuvre()
        for livre in oeuvres:
            if nomLivre==livre.titre:
                self.catalogue.append([livre, quantite])
                break
    
    def inventaire(self):
        for couple in self.catalogue:
            print("Le livre : "+str(couple[0].titre)+" est présent "+str(couple[1])+" fois dans la bibliothèque.")
    
    def louer(self, client, nomLivre):
        for couple in self.catalogue:
            if nomLivre==couple[0].titre and couple[1]>0:
                client.collection.append(couple[0])
                couple[1]=couple[1]-1
    
    def rendreLivres(self, client):
        livresClient=client.getcollection()
        for i in range(len(livresClient)):
            livre=livresClient.pop()
            for couple in self.catalogue:
                if couple[0].gettitre()==livre.gettitre():
                    couple[1]+=1

class Client(Personne):
    def __init__(self, nom, prenom):
        self.nom=nom
        self.prenom=prenom
        self.collection=[]
        super().__init__(prenom, nom)

    def inventaire(self):
        for livre in self.collection:
            print(livre.gettitre())

    def getcollection(self):
        return(self.collection)


