from libs.alien import *

x = 8
y = 8

y = y + 6
bas(6)
x = x - 7
gauche(7)

while x < 12 :
    while y < 11 :
        x = x + 1
        droite()
        y = y + 3
        bas(3)
    y = y - 10
    haut(10)

ss()