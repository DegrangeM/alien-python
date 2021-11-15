from libs.alien import *

a = 0

haut(6)
droite(6)
while colonne() > 6 :
    bas(3)
    gauche(2)
haut(2)
droite(3)
while colonne() < 14 :
    droite(3)
    haut(2)

ss()