import importlib.util
from importlib import reload
import os

import sys
from pathlib import Path

# On fait comme si on exécutait le script depuis le dossier exercices
os.chdir("..")
sys.path.insert(0, os.path.join(Path(__file__), ".."))

# Permet d'exécuter le contenu d'un fichier
def module_from_file(module_name, file_path):
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


for f in os.listdir("./"):
    if os.path.isfile(f):
        # il faut invalider le cache du module afin que la
        # ligne alien = Alien(8,8) s'exécute à nouveau
        if 'libs.alien' in sys.modules :
            del sys.modules['libs.alien']
        r = module_from_file(f, f)
        print(f)
        lettres = ["", "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O"]
        print(lettres[r.alien.y] + str(r.alien.x))
        
