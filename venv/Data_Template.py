# Title: 12 Days of Kill-mas
# Author: Nicholas Perez-Aguilar
# File: Data Template.py

# Imports
import Auxillary_Funcs as Aux

class DATA_DISPLAY():
    def __init__(self, iteration, day, headers, data):
        self.day = day          # Day number - string format
        self.head = headers     # Headers (1st line of file)
        self.data = data        # Data of each file - outside header (1st line of file)
        self.cnt = 0            # Num vids
        self.perc = 0.0         # Percentage complete
        self.iter = iteration   # Number represenation of day
        self.upd = []           # Update list to be appended to

    def print_day(self):
        # Get Day statistics
        self.cnt = Aux.day_vid_cnt(self.iter)   # Get cnt of vids for day from day number
        self.test_data_complete()   # Set percentage complete

        # Print Day info
        print(Aux.num_to_space(75) + Aux.num_to_dash(35))

        if(self.perc < 100):
            print(Aux.num_to_space(75) + Aux.num_to_space(4) + self.day + " -- " + "{:.2f}".format(self.perc) + "% - {0} videos".format(int(self.cnt)))
        else:
            print(Aux.num_to_space(75) + Aux.num_to_space(3) + self.day + " -- COMPLETE - {0} videos".format(int(self.cnt)))

        print(Aux.num_to_space(75) + Aux.num_to_dash(35) + '\n\n')

    def print_headers(self):
        for i in range(len(self.head)):
            print(str(self.head[i]) + Aux.num_to_space(15), end = '')
        print('\n')

    def print_data(self):
        for i in range(len(self.data)):
            temp = self.data[i]

            for j in range(len(temp)):
                print(str(temp[j]) + Aux.num_to_space(12), end = '')

            print('\n')

        print('\n')

    def test_data_complete(self):
        comp_cnt = 0

        for i in range(len(self.data)):
            temp = self.data[i] # Isolate each category folder from day

            if(temp[2] != "" and temp[3] != "" and temp[4] != ""):
                comp_cnt += 1

        self.perc = (comp_cnt / self.cnt) * 100

    def get_incomplete_data_info(self):
        get_incomplete = []
        wrap_incomplete = []

        # Start with an empty string
        self.upd = []

        # Get incomplete data into list
        for i in range(len(self.data)):
            temp = self.data[i]

            for j in range(len(temp)):
                if (temp[2] == "" and temp[3] == "" and temp[4] == ""):
                    get_incomplete.append(temp)
                    self.upd.append(temp[1])
                    break

        return get_incomplete, self.upd

    def print_incomplete_data(self, get_incomplete):
        # Print incomplete data
        for i in range(len(get_incomplete)):
            temp = get_incomplete[i]

            for j in range(len(temp)):
                print(str(temp[j]) + Aux.num_to_space(12), end='')

            print('\n')

        print('\n')

class UPDATE_DISPLAY:
    def __init__(self, day, video, game, map, type):
        self.d = day
        self.v = video
        self.g = game
        self.m = map
        self.t = type

    def disp_update(self):
        choice = ""

        Aux.clear()
        print("UPDATE INFORMATION")
        print("------------------\n")
        print("Day: " + str(self.d))
        print("Video: " + self.v)
        print("Game: " + self.g)
        print("Map: " + self.m)
        print("Game Type: " + self.t)

        input("\nPush any key to continue")
        choice = Aux.get_yn("\nIs this correct? [Y/n]: ")

        return choice