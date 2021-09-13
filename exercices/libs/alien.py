from PIL import Image, ImageDraw, ImageFont
import sys

class Alien :
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.i = 1;
        self.l = False
        self.step = False
        self.font = ImageFont.truetype("../ressources/font/LiberationMono-Bold.ttf", 10)
        self.grille = Image.open("../ressources/img/grille.png")
        self.alien = Image.open("../ressources/img/alien.png")
        self.alien2 = Image.open("../ressources/img/alien2.png")
        self.output = Image.new('RGB', (750, 750))
        self.draw = ImageDraw.Draw(self.output)
        self.output.paste(self.grille, (0,0))
        self.afficher()
        
    def afficher(self) :
        self.output.paste(self.alien2 if self.l else self.alien, (50*(self.x-1),50*(self.y-1)), self.alien)
        self.draw.text((50*(self.x-1)+48,50*(self.y-1)+47), str(self.i), fill=(111, 196, 169), anchor="rb", font=self.font)
        
    def teleporter(self, x, y, l=False) :
        self.draw.line([(50*(self.x-1)+25,50*(self.y-1)+25),(50*(x-1)+25,50*(y-1)+25)], fill=(255, 255, 255), width=2)
        self.afficher() # pour être sûr que la ligne soit derrière l'alien
        self.l = l
        self.i += 1
        self.x = x
        self.y = y
        self.afficher()
        self.step and self.show()
    
    def haut(self, n=1) :
        self.teleporter(self.x,self.y-n)
    def gauche(self, n=1) :
        self.teleporter(self.x-n,self.y)
    def droite(self, n=1) :
        self.teleporter(self.x+n,self.y)
    def bas(self, n=1) :
        self.teleporter(self.x,self.y+n)
        
    def colonne(self) :
        return self.x
    
    def ligne(self) :
        return self.y
        
    def localiser(self) :
        self.l = True
        self.afficher()
        self.step and self.show()
        
    def show(self) :
        self.output.show()
        
    def save(self, name=None) :
        if name == None :
            name = sys.argv[0].split('.')[0].split('/')[-1]
        self.output.save("corrections/" + str(name) + ".png")
        
    def ss(self, name=None) :
        self.save(name)
        self.show()
        
        
alien = Alien(8,8)



for f in [f for f in dir(Alien) if not f.startswith('_')] :
    globals()[f] = getattr(alien, f)


