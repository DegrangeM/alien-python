from libs.alien import *

bas(2)
droite(7)

a = 2
while colonne() > 4 :
    a = a + 1
    haut()
    gauche(3)
bas(a)

ss()