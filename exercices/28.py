from libs.alien import *

a = 5
b = 2

droite(5)
if a < b :
    haut()
    gauche()
    for loop in range(4) :
        haut()
    bas(3)
droite()
if a > b :
    bas()
    droite()
    for loop in range(4) :
        bas()
    gauche(3)
ss()