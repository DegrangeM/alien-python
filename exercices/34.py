from libs.alien import *

gauche(6)
haut(5)
if colonne() < 3 :
    droite(4)
if colonne() < 5 :
    droite(2)
if colonne() > 9 :
    bas(4)
droite(4)
if colonne() > 9 :
    bas(4)
for loop in range(3) :
    gauche()
    haut()

ss()
