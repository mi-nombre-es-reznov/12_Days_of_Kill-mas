# Title: 12 Days of Kill-mas
# Author: Nicholas Perez-Aguilar
# File: Main.py

# Imports
import Inputs as inp
import Globals as G
import File_Manipulation as FM
import Auxillary_Funcs as Aux

# Code Path
if __name__ == "__main__":
    valid = ""
    filename = ""

    Aux.clear()

    filename = inp.set_path()
    valid = FM.test_file(filename)