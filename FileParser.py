import csv
import ast
import Pokemon as p

'''
This function parses pokemon data out of the csv file named 
pokemon-data.csv and creates objects with the data. In order to 
create pokemon objects with moves that contain data, the move_set list
is used to match move names with move_set objects that have the same name.

Parameters:
pokedex - a list that will contain all pokemon objects
move_set - a list of move objects that were created by the ParseMoves function
'''
def ParsePokedex(pokedex, move_set):

    # do the block of code while opening the file and setting a file pointer named csvfile
    with open("pokemon-data.csv", "r") as csvfile:
        
        # create a parser object that will read in each line and separate by comma
        parser = csv.reader(csvfile, delimiter=',')

        # eliminate the header of the file
        next(parser)

        # loop through each line in the file
        for line in parser:

            # this parses the moves list out of each row in the moves column
            move_names = ast.literal_eval(line[7])

            # the list in move_names only contains string literals, no objects that hold key data necessary for battle logic
            # if the current string in move_names, matches the name of a move object in move_set, 
            # set the current index in move_names to be the matching object.
            pokemon_moves = [move for move in move_set if move.name in move_names]

            # create pokemon object for each line in the file
            curr_mon = p.Pokemon(line[0], line[1], int(line[2]), int(line[3]), int(line[4]), int(line[5]), int(line[6]), pokemon_moves)
           
            # append the new pokemon object to the list
            pokedex.append(curr_mon)

'''
This function parses data out of the file named moves-data.csv, and
creates objects for each move.

parameters:
move_set - a list that contains all available pokemon move objects
'''
def ParseMoves(move_set):

    # do the following block of code while opening the file and setting a file pointer named csvfile
    with open("moves-data.csv", "r") as csvfile:

        # create parser object with delimiter set to commas
        parser = csv.reader(csvfile, delimiter=',')

        # eliminate the header of the file
        next(parser)

        # loop through each line in the file
        for line in parser:

            # this handles type error if current row in accuracy column is 'None'
            accuracy = None if line[6].strip() == 'None' else int(line[6])

            # create move objects
            curr_move = p.Move(line[0], line[1], line[2], line[3], int(line[4]), int(line[5]), accuracy)
            # append move object to the list of existing moves
            move_set.append(curr_move)