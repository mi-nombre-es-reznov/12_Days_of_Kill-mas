# Title: 12 Days of Kill-mas
# Author: Nicholas Perez-Aguilar
# File: Inputs.py

# Imports
import Auxillary_Funcs as Aux
import Globals as G

# Code
def set_path():
    filename = ""
    valid = ""

    while(filename == ""):
        Aux.clear()
        filename = Aux.test_str("Enter the file location: ")

    return filename

def get_update(choices):
    choice = -1
    temp = -1
    vid = ""
    day = 0
    available = []
    temp_list = []

    # Get all days that have something to complete
    for i in range(len(choices)):
        if(choices[i] != []):
            available.append(((i + 1), choices[i]))

    # Select day to update
    while(choice < 1 or choice > len(available)):
        for i in range(len(available)):
            print(str(i + 1) + ") - Day " + str(available[i][0]))

        choice = Aux.test_int("\nSelect a Day by number: ")   # Get the day from the avaiable, non-empty days
        temp = choice - 1                                     # Adjust for list

    # Get day from list
    day = int(available[temp][0])

    choice = -1
    print("\n\n")

    # Select which video to assign
    while(choice < 1 or choice > len(available[temp][1])):
        for i in range(len(available[temp][1])):
            temp_list.append(available[temp][1][i])

        Aux.options_display(temp_list)

        choice = Aux.test_int("\nSelect a video folder to update: ")    # Get specific game type to update

    choice -= 1                                                         # Adjust choice for list
    vid = available[temp][1][choice]

    return day, vid

def set_game():
    choice = -1

    while(choice < 1 or choice > len(G.GAMES)):
        Aux.options_display(G.GAMES)
        choice = Aux.test_int("Which Game? ")

    return G.GAMES[choice - 1]


def set_Game_Type():
    choice = -1
    g_type = ""

    while(choice < 1 or choice > len(G.GAME_MODE)):
        Aux.options_display(G.GAME_MODE)
        choice = Aux.test_int("Which Game Mode? ")

    if(G.GAME_MODE[choice - 1] == "Other"):
        g_type = Aux.test_str("Enter Game Mode: ")
    else:
        g_type = G.GAME_MODE[choice - 1]

    return g_type

def set_map(game):
    choice = -1
    maps = []

    # Determine what game maps are available for choices
    if(game == "Call of Duty: Mobile"):
        maps = G.MAP_COD_MOBILE
    elif(game == "Call of Duty: Modern Warfare"):
        maps = G.MAP_COD_MODERN_WARFARE
    elif(game == "Call of Duty: Cold War"):
        maps = G.MAP_COD_COLD_WAR
    elif(game == "Call of Duty: Vanguard"):
        maps = G.MAP_COD_VANGUARD
    elif(game == "Call of Duty: Warzone"):
        maps = G.MAP_COD_WARZONE
    else:
        print("Something went wrong. Check the code!\n")

    # Allow for selection from game
    while (choice < 1 or choice > len(maps)):
        Aux.options_display(maps)
        choice = Aux.test_int("Which Map? ")

    return maps[choice - 1]

def cross_check_map_loc(day, mapping):
    location = ""

    for i in range(len(mapping)):
        if(mapping[i][0] == day):
            location = mapping[i][1]
            break

    location = (location + "\\" + day + ".csv")

    return location

def update_curr_data(curr, match, g, t, m):
    update = []

    for i in range(len(curr)):
        if(curr[i][1] == match):
            curr[i][2] = g
            curr[i][3] = t
            curr[i][4] = m

        update.append(curr[i])

    return update