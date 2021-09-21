import importlib.util
import os

import sys
from pathlib import Path

os.chdir("..")

sys.path.insert(0, os.path.join(Path(__file__), ".."))

def ss(*args) :
    pass

def module_from_file(module_name, file_path):
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

r = module_from_file("1","./1.py")