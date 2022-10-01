import os
import re

# IMPORTANT : NECESSITE PYTHON >= 3.8

# La génération ne fonctionnera pas avec tous les programmes pythons possibles

# IL VA Y AVOIR UN SOUCIS EN CAS DE MULTIPLE FERMETURE DE BLOCK
# Ex :
# if XXX :
# 	if XXX :
# XXX
# au les deux ifs ont été fermés

for f in os.listdir("../"):
    if os.path.isfile("../" + f):
        with open('../' + f, 'r') as c :
            with open('../scratch/'+f.split('.')[0]+'.tex', 'w',  encoding="utf-8") as i:

                latex = [
                    '\\documentclass{standalone}',
                    '\\usepackage[T1]{fontenc}',
                    '\\usepackage[utf8]{inputenc}',
                    '\\usepackage{lmodern}',
                    '\\usepackage{babel}',
                    '\\usepackage{scratch3}',
                    '\\begin{document}',
                    '\\begin{scratch}'
                ]

                code = c.readlines()
                
                code = code[1:-1] # on retire la première (import) et dernière (ss) ligne
                
                indent = 0
                lastIndent = indent
                blocks = []
                
                for line in code :
                    line = line.rstrip()
                    length = len(line)
                    line = line.lstrip()
                    if line == '' :
                        continue
                    if line[0] == '#' :
                            
                        continue
                    indent = length - len(line)
                    # On suppose que le code est indenté de manière valide
                    if lastIndent > indent : # L'indentation s'est réduite (décallage vers la gauche)
                        if blocks[-1] == 'def' :
                            latex.append('\\blockspace')
                        else :
                            latex.append('}')
                            if blocks[-1] == 'if' :
                                latex.append('{}') # On ajoute un else vide, on l'enlèvera si besoin
                        blocks.pop(-1) # On retire le dernier block de la liste puisqu'on vient d'en sortir
                    lastIndent = indent
                    
                    if line == '' :
                        continue
                                    
                    # Déplacements
                    if m := re.match(r'(gauche|droite|haut|bas)\(\s?([0-9]*)\s?\)', line) :
                        prefix = 'à' if m.group(1) in ['gauche', 'droite'] else 'en'
                        if m.group(2) == '' :
                            latex.append('\\blockmove{Se déplacer \\selectmenu{'+prefix+' '+m.group(1)+'}}')
                        else :
                            latex.append('\\blockmove{Se déplacer \\selectmenu{'+prefix+' '+m.group(1)+'} de \\ovalnum{'+m.group(2)+'} '+('cases' if int(m.group(2)) >= 2 else 'case') + '}')
                        continue
                    
                    # Affectation
                    if m := re.match(r'([a-zA-Z_]+)\s?=\s?(.+)', line) :
                        valeur = m.group(2)
                        valeur = valeur.strip()
                        if re.match(r'^[0-9]+$', valeur) :
                            valeur = '\\ovalnum{'+valeur+'}'
                        else :
                            valeur = re.sub(r'([a-zA-Z_]+)([^(a-zA-Z_]|$)', r'\\ovalvariable{\1}\2', valeur)
                            valeur = valeur.replace('colonne()', '\\ovalsensing{colonne actuelle}')
                            valeur = re.sub(r'([0-9]+)', r'\\ovalnum{\1}', valeur)
                            valeur = '\\ovaloperator{'+valeur+'}'
                        
                        latex.append('\\blockvariable{mettre \\ovalvariable{'+m.group(1)+'} à '+valeur+'}')
                        continue
                    
                    # If
                    if m := re.match(r'if(?: |\()([^:]+):$', line) :
                        blocks.append('if')
                        condition = m.group(1)
                        condition = condition.strip()
                        condition = re.sub(r'([a-zA-Z_]+)([^(a-zA-Z_]|$)', r'\\ovalvariable{\1}\2', condition)
                        condition = condition.replace('colonne()', '\\ovalsensing{colonne actuelle}')
                        condition = re.sub(r'([0-9]+)', r'\\ovalnum{\1}', condition)
                        
                        latex.append('\\blockifelse{Si \\booloperator{' + condition + '} alors}{')
                        continue
                    
                    # Else
                    if m := re.match(r'else\s*:$', line) :
                        latex.pop(-1) # On enlève le else vide ajouté temporairement
                        blocks.append('else')
                        latex.append('{')
                        continue
                    
                    # For
                    if m := re.match(r'for\s+([a-zA-Z_]+)\s+in range\(([^)]+)\)\s+:$', line) :
                        blocks.append('for')
                        rangeValue = m.group(2)
                        rangeValue = rangeValue.strip()
                        rangeValue = re.sub(r'([a-zA-Z_]+)([^(a-zA-Z_]|$)', r'\\ovalvariable{\1}\2', rangeValue)
                        rangeValue = rangeValue.replace('colonne()', '\\ovalsensing{colonne actuelle}')
                        rangeValue = re.sub(r'([0-9]+)', r'\\ovalnum{\1}', rangeValue)
                        # Il y aura un mini-problème graphique non gênant si le rangeValue contient des opérations
                        if m.group(1) == 'loop' :
                            latex.append('\\blockrepeat{Répéter '+rangeValue+' fois}{')
                        else :
                            rangeValues = rangeValue.split(',')
                            if len(rangeValues) == 1 : # Une seule valeur n'est donné donc c'est de 0 à X
                                rangeValues = ['\\ovalnum{0}'] + rangeValues
                            latex.append('\\blockrepeat{Répéter pour \ovalvariable{'+m.group(1)+'} allant de '+rangeValues[0]+' (inclus) à '+rangeValues[1]+' (exclus)}{')
                        continue
                    
                    # While
                    if m := re.match(r'while(?: |\()([^:]+):$', line) :
                        blocks.append('while')
                        condition = m.group(1)
                        condition = condition.strip()
                        condition = re.sub(r'([a-zA-Z_]+)([^(a-zA-Z_]|$)', r'\\ovalvariable{\1}\2', condition)
                        condition = condition.replace('colonne()', '\\ovalsensing{colonne actuelle}')
                        condition = re.sub(r'([0-9]+)', r'\\ovalnum{\1}', condition)
                        latex.append('\\blockrepeat{Tant que \\booloperator{' + condition + '} faire}{')
                        continue
                    
                    # Def
                    if m := re.match(r'def\s+([^:]+)\s+:$', line) :
                        blocks.append('def')
                        # Il faudrait gérer les variables, pour l'instant l'affichage est brut ...
                        latex.append('\\initmoreblocks{définir \\namemoreblocks{'+m.group(1)+'}}')
                        continue
                        
                    # Impossible de convertir la ligne ...
                    latex.append('\\blockpen{'+line+'}')
                
                if len(blocks) : # Il faut fermer les blocks ouvert qui n'auraient jamais été fermé par absance de nouvelle ligne
                    parenthese_a_fermer = len(blocks) - blocks.count('def')
                    if parenthese_a_fermer > 0 :
                        latex.append('}'*parenthese_a_fermer)
                
                latex.extend([
                    '\\end{scratch}',
                    '\\end{document}'
                ])
              
                i.write('\n'.join(latex))
                print("Génération de " + f + " terminée")