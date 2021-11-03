# Title: 12 Days of Kill-mas
# Author: Nicholas Perez-Aguilar
# File: Main.py

# Imports
import time

import Inputs as inp
import Globals as G
import File_Manipulation as FM
import Auxillary_Funcs as Aux

# Code Path
if __name__ == "__main__":
    valid = ""
    filename = ""
    again = "Yes"

    while(again == "Yes"):
        Aux.clear()
        filename = inp.set_path()
        valid = FM.test_file(filename)

        if(valid == "Yes"):
            pass
        elif(valid == "No"):
            pass
        else:
            Aux.clear()
            print("Something went wrong. Check the code.")
            time.sleep(3)

        # Again?
        again = Aux.get_yn("Add another entry? [Y/n]: ")