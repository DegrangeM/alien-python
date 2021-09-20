import importlib.util
import os

# Spaghetti magic

def module_from_file(module_name, file_path):
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

a = module_from_file("alien","./libs/alien.py")

for f in [f for f in dir(a) if not f.startswith('_')] :
    print(f,getattr(a,f),type(getattr(a,f)))
    if True :
        print(f)
        globals()[f] = getattr(a.alien, f)
    if f in ['ss', 'show', 'save'] : 
        globals()[f] = lambda *args : None