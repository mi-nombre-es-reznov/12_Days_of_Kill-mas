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
    map_data = []

    while(again == "Yes"):
        # Get & Test user-input location
        Aux.clear()                     # Clear the screen from the start/loop at beginning of program
        filename = inp.set_path()       # Get path from user
        valid = FM.test_file(filename)  # Test user-entered path for validity

        # Program mapping based on given location
        Aux.clear()
        if(valid == "Yes"):
            map_data = FM.get_data(filename)
            Aux.map_status(map_data)
        elif(valid == "No"):
            print("Location provided does not exist!")
            time.sleep(3)
        else:
            print("Something went wrong. Check the code.")
            time.sleep(3)

        # Again?
        again = Aux.get_yn("Add another entry? [Y/n]: ")