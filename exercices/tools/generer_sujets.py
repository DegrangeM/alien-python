import os
from pygments import highlight
from pygments import lexers
from pygments.formatters.img import ImageFormatter
from pygments.styles import get_style_by_name


for f in os.listdir("../"):
    if os.path.isfile("../" + f):
        with open('../' + f, 'r') as c :
            with open('../sujets/'+f.split('.')[0]+'.png', 'wb') as i:
                
                code = c.readlines()
                
                code = code[1:-1] # on retire la première (import) et dernière (ss) ligne
                
                while code[0] == '' :
                    code = code [1:]
                    
                while code[-1] == '' :
                    code = code [:-1]
                
                lexer = lexers.get_lexer_by_name('python')
                style = get_style_by_name('autumn')
                formatter = ImageFormatter(full=True, style=style, font_size=20*2, line_pad=4, image_pad=4, line_number_bg="#FFF", line_number_fg="#777")
                i.write(highlight(''.join(code), lexer, formatter))