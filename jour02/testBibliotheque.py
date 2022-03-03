from Personne import *

livre1=Livre('roman')
livre2=Livre('poeme')
livre3=Livre('book')
auteur1=Auteur('Marlet', 'Romain')
auteur1.ecrireUnLivre('essai')
magasin=Bibliotheque('Fnac', [[livre1,1],[livre2,2],[livre3,1]])
magasin.acheterLivre(auteur1, 'essai', 1)
client1=Client('Martin', 'Thomas')
magasin.louer(client1, 'essai')
magasin.inventaire()
client1.inventaire()