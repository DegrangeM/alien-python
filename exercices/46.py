from libs.alien import *

a = 1
b = 0

bas(7)
gauche(7)

while a == 1 :
    b = b + 4
    if b < 50 :
        b = b * 2
        haut()
    if b > 65 :
        a = 0
    droite()
haut(3)

ss()