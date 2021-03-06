# Title: 12 Days of Kill-mas
# Author: Nicholas Perez-Aguilar
# File: Main.py

# Imports
import sys
import time

import Inputs as inp
import Globals as G
import File_Manipulation as FM
import Auxillary_Funcs as Aux
import Data_Template as DT

# Code Path
if __name__ == "__main__":
    valid = ""
    filename = "G:\\Shared drives\\NCompEng Technologies\\0) Global Information\\Worker Resources\\Business created Software\\12 Days of Kill-mas\\venv\\Killmas_Days\\Killmas_data_mapping.csv"
    again = "Yes"
    map_data = []
    killmas_data = []

    while(again == "Yes"):
        # Get & Test user-input location
        Aux.clear()                     # Clear the screen from the start/loop at beginning of program
        if(filename == ""):
            filename = inp.set_path()       # Get path from user
        valid = FM.test_file(filename)  # Test user-entered path for validity

        # Program mapping based on given location
        Aux.clear()
        if(valid == "Yes"):
            choice = Aux.menu_display("Main Menu", G.MAIN_MENU) # Display Main Menu

            # Gather Data
            map_data = FM.get_data(filename)  # Getting data from mapping file
            vfn, vfl = Aux.map_status(map_data)  # Getting valid file names and links

            # Get data for every Day in Killmas files
            for i in range(len(vfl)):
                data = FM.get_data(vfl[i])
                killmas_data.append(data)

            # Run Selected Choice
            if(choice == 0):
                # Seperate killmas data and display
                for i in range(len(killmas_data)):
                    temp_data = killmas_data.pop(0)
                    header = temp_data.pop(0)

                    # Set up and overwrite class object
                    dd = DT.DATA_DISPLAY((i + 1), vfn[i], header, temp_data)
                    dd.print_day()
                    dd.print_headers()
                    dd.print_data()

                input("\n\nPress any key to continue.")
            elif(choice == 1):
                incomplete = vfn
                day_update = [] # Used to hold update info
                game = ""
                game_type = ""
                game_map = ""
                day_curr = []   # Used to hold current data

                # Seperate killmas data and display
                for i in range(len(killmas_data)):
                    temp_data = killmas_data.pop(0)                             # Break each video from day up into list
                    header = temp_data.pop(0)                                   # Pop headers from day files

                    # Set up and overwrite class object - ITERATES by Day
                    ud = DT.DATA_DISPLAY((i + 1), vfn[i], header, temp_data)    # Create class object
                    ud.print_day()                                              # Print days
                    ud.print_headers()                                          # Print Headers
                    incomplete, vid_choices = ud.get_incomplete_data_info()     # Get all incomplete videos by day
                    day_update.append(vid_choices)                              # Append before class overwrite per day
                    ud.print_incomplete_data(incomplete)                        # Print incomplete data list

                # Get video number
                day, vid = inp.get_update(day_update)    # Get update parameter (video number) - Location

                # Get video update info
                Aux.clear()
                game = inp.set_game()                                           # Get Game
                Aux.clear()
                game_type = inp.set_Game_Type()                                 # Get Game Type
                Aux.clear()
                game_map = inp.set_map(game)                                    # Get Game Map
                Aux.clear()
                upd = DT.UPDATE_DISPLAY(day, vid, game, game_map, game_type)     # Display and Verify
                cont = upd.disp_update()

                # Update file
                Aux.clear()
                if(cont == "Yes"):
                    day_s = ("Day " + str(day))                                 # Get day in proper format
                    loca = inp.cross_check_map_loc(day_s, map_data)             # Cross-check day against day files
                    day_curr = FM.get_data(loca)                                # Get current location for day
                    day_update = inp.update_curr_data(day_curr, vid, game, game_type, game_map) # Get updated info
                    FM.set_data(day_update, loca)                               # Update data at file location
                elif(cont == "No"):
                    print("No has been selected. No further changes are made.\n\n")
                else:
                    print("Something went wrong. Check the code!\n")

                input("\n\nPress any key to continue.")
            elif(choice == 2):
                Aux.clear()
                print("Thank you for using NCompEng Technologies!")
                time.sleep(3)
                sys.exit()
            else:
                Aux.clear()
                print("Something went wrong! Check the code!\n")
                time.sleep(5)


        elif(valid == "No"):
            print("Location provided does not exist!")
            time.sleep(3)
        else:
            print("Something went wrong. Check the code.")
            time.sleep(3)

        # Again?
        again = Aux.get_yn("Add another entry? [Y/n]: ")