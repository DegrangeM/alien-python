from libs.alien import *

def deplacement(n) :
    if n > 6 :
        haut(2)
    else :
        droite(n)

gauche(7)
bas(7)

n = 0

while n < 12 :
    n = n + 2
    deplacement(n)

ss()