from libs.alien import *

n = 0
u = 5

while u < 200 :
    droite()
    n = n + 1
    u = 3 * u
haut(n)
if u > 400 :
    gauche()
else :
    droite()

ss()