from libs.alien import *

a = 1
gauche(7)

while a < 80 :
    if a < 50 :
        a = a * 2
        haut()
    else :
        a = a + 5
        bas(2)
    droite()
    print(a)

ss()