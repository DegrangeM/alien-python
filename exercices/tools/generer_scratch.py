import os
import re

# IMPORTANT : NECESSITE PYTHON >= 3.8

for f in os.listdir("../"):
    if os.path.isfile("../" + f):
        with open('../' + f, 'r') as c :
            with open('../scratch/'+f.split('.')[0]+'.tex', 'w',  encoding="utf-8") as i:

                latex = [
                    '\\documentclass[french]{article}',
                    '\\usepackage[T1]{fontenc}',
                    '\\usepackage[utf8]{inputenc}',
                    '\\usepackage{lmodern}',
                    '\\usepackage[a4paper]{geometry}',
                    '\\usepackage{babel}',
                    '\\usepackage{scratch3}',
                    '\\begin{document}',
                    '\\begin{scratch}'
                ]

                code = c.readlines()
                
                code = code[1:-1] # on retire la première (import) et dernière (ss) ligne
                
                ident = 0
                
                for line in code :
                    line = line.rstrip()
                    length = len(line)
                    line = line.lstrip()
                    ident = length - len(line)
                    
                    if line == '' :
                        continue
                    if m := re.match(r'(gauche|droite|haut|bas)\(\s?([0-9]*)\s?\)', line) :
                        prefix = 'à' if m.group(1) in ['gauche', 'droite'] else 'en'
                        if m.group(2) == '' :
                            latex.append('\\blockmove{Se déplacer '+prefix+' '+m.group(1)+'}')
                        else :
                            latex.append('\\blockmove{Se déplacer '+prefix+' '+m.group(1)+' de \\ovalnum{'+m.group(2)+'} '+('cases' if int(m.group(2)) >= 2 else 'case') + '}')
                        continue
                    
                    # Impossible de convertir la ligne ...
                    latex.append('\\blockpen{'+line+'}')
                
                latex.extend([
                    '\\end{scratch}',
                    '\\end{document}'
                ])
              
                i.write('\n'.join(latex))