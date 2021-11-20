# Title: 12 Days of Kill-mas
# Author: Nicholas Perez-Aguilar
# File: Auxillary Functions.py

# Used for screen clearing
from os import system, name
from collections import Counter
import time

import File_Manipulation as FM

def clear():
    '''
    Used to clear the screen.

    Returns
    -------
    None.

    '''

    # Windows
    if (name == 'nt'):
        _ = system('cls')
    # Mac/Linux
    else:
        _ = system('clear')

# Test string
def test_str(prmpt):
    val = ""    # Holds the string

    while(val == ""):
        clear()
        val = input(prmpt)

        if(val == ""):
            clear()
            print("Input cannot be empty. Follow the prompt.")
            time.sleep(3)

    return val

# Test Int
def test_int(prmpt):
    valid = False
    test_num = 0

    while(valid == False):
        try:
            test_num = int(input(prmpt))
            valid = True
        except ValueError:
            clear()
            print("Input not valid! Enter an Integer!")
            time.sleep(3)

    return test_num

# Get Yes/No
def get_yn(prmpt):
    val = ''

    while(val != 'y' and val != 'n'):    # Loop while option is not Y or N
        clear()
        val = input(prmpt)
        val = val.lower()

        if(val == ''):
            clear()
            print("Valid answers are 'y', 'Y', 'n', or 'N'")
            time.sleep(3)

    if(val == 'y'):
        val = "Yes"
    elif(val == 'n'):
        val = "No"

    return val

# Display mapping status to user
def map_status(map_list):
    valid = ""
    test_file = ""
    valid_files_link = []
    valid_files_names = []

    # Display day statuses
    clear()
    for i in range(len(map_list)):
        if(map_list[i][2] == "1"):
            print(str(map_list[i][0]) + "\tMapping Location Found: " + str(map_list[i][1]))
    time.sleep(3)
    clear()

    # Use location from days to find video files list in sub-directories
    for i in range(len(map_list)):
        if(map_list[i][2] == "1"):
            test_file = (map_list[i][1] + "\\" + map_list[i][0] + ".csv")   # Append file name to file extension
            valid = FM.test_file(test_file) # Test the concatenated file directory

            clear()
            if(valid == "No"):
                print(str(map_list[i][0]) + " NOT found!")
            elif(valid == "Yes"):
                valid_files_names.append(map_list[i][0])
                valid_files_link.append(test_file)

    # Return all days that are tested as valid
    return valid_files_names, valid_files_link

def num_to_space(num):
    space = ""

    for i in range(num):
        space += " "

    return space

def num_to_dash(num):
    dash = ""

    for i in range(num):
        dash += "-"

    return dash

def day_vid_cnt(num):
    num_vids = 0

    num_vids = (num * (num + 1))/2 # Summation for consecutively added numbers

    return num_vids

def menu_display(title, ops):
    result = -1

    while(result < 1 or result > len(ops)):
        clear()

        print(title + '\n') # Title and space
        for i in range(len(ops)):
            print(str(i + 1) + ") {0}".format(ops[i]))

        result = int(input("\nSelect an option: "))

    result -= 1
    return result

def options_display(search_list):
    for i in range(len(search_list)):
        print(str(i + 1) + ") " + str(search_list[i]))

    print('\n')