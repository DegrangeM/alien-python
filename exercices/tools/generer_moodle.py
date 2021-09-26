import importlib.util
from importlib import reload
import os
from xml.dom import minidom
import base64
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

xml = minidom.Document()
quiz = xml.createElement('quiz')
xml.appendChild(quiz)



for f in os.listdir("./"):
    if os.path.isfile(f):
        
        # il faut invalider le cache du module afin que la
        # ligne alien = Alien(8,8) s'exécute à nouveau
        if 'libs.alien' in sys.modules :
            del sys.modules['libs.alien']
        r = module_from_file(f, f)
        lettres = ["", "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O"]
        with open('./sujets/'+f.split('.')[0]+'.png', "rb") as fichier_sujet:
            sujet = base64.b64encode(fichier_sujet.read()).decode()
        solution = lettres[r.alien.y] + str(r.alien.x)
        
        #quiz/question
        question = xml.createElement('question')
        quiz.appendChild(question)
        question.setAttribute('type', 'shortanswer')
        #quiz/question/name
        name = xml.createElement('name')
        question.appendChild(name)
        text = xml.createElement('text')
        name.appendChild(text)
        text.appendChild(xml.createTextNode(f.split('.')[0]));
        #quiz/question/questiontext
        questiontext = xml.createElement('questiontext')
        question.appendChild(questiontext)
        questiontext.setAttribute('format', 'html')
        text = xml.createElement('text')
        questiontext.appendChild(text)
        text.appendChild(xml.createTextNode('<img src="@@PLUGINFILE@@/' + f.split('.')[0] + '.png" alt="" role="presentation">'));
        file = xml.createElement('file')
        questiontext.appendChild(file)
        file.setAttribute('name', f.split('.')[0] + '.png')
        file.setAttribute('path', '/')
        file.setAttribute('encoding', 'base64')
        file.appendChild(xml.createTextNode(str(sujet)));
        #quiz/question/defaultgrade
        defaultgrade = xml.createElement('defaultgrade')
        question.appendChild(defaultgrade)
        defaultgrade.appendChild(xml.createTextNode('1'));
        #quiz/question/name
        answer = xml.createElement('answer')
        question.appendChild(answer)
        answer.setAttribute('fraction', '100')
        answer.setAttribute('format', 'moodle_auto_format')
        text = xml.createElement('text')
        answer.appendChild(text)
        text.appendChild(xml.createTextNode(solution));

with open("./tools/moodle.xml", "w") as f:
    f.write(xml.toprettyxml()) 
        
