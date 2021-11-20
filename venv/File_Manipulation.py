# Title: 12 Days of Kill-mas
# Author: Nicholas Perez-Aguilar
# File: File Manipulation.py

# Imports
import csv
import time

import Auxillary_Funcs as Aux
import Globals as G

import os
import glob

# Code
def test_file(filename):
    valid = ""

    Aux.clear()

    try:    # Test Existance and Opening of File
        with open(filename, "r") as file:
            reader = csv.reader(file)
            valid = "y"
    except FileNotFoundError:   # File does not exist
        print("File doesn't exist!")
        valid = "n"
        time.sleep(1)

    # Get Yes/No
    valid = "Yes" if (valid == 'y') else "No"

    Aux.clear()
    file.close()

    return valid

def get_data(filename):
    value = []

    with open(filename, 'r') as file:
        reader = csv.reader(file)

        for row in reader:
            value.append(row)

    file.close()
    return value

def find_csv(path):
    Aux.clear()
    extension = 'csv'
    os.chdir(path)
    result = glob.glob('*.{}'.format(extension))
    print(result)

    return path, result

def set_data(updated, filename):
    with open(filename, 'w', newline = '') as file:
        write = csv.writer(file)
        write.writerows(updated)

    file.close()
    Aux.clear()
    print("File updated!\n")
    time.sleep(2)