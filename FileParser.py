import csv
import Pokemon as p

header = []
pokemon_moves = {}
pokemon_list = []

# this function likely needs redesign. Not sure how the list of moves in the CSV file will be transferred yet.
# I think the param here should be the list containing all of the pokemon objects
def ParsePokedex(pokedex):

    # do the block of code while opening the file and setting a file pointer named csvfile
    with open("pokemon-data.csv", "r") as csvfile:
        # create a parser that will read in each line and separate by comma
        parser = csv.reader(csvfile, delimiter=',')

        # eliminate the header of the file
        next(parser)
        # loop through each line in the file
        for line in parser:

            # create pokemon object for each line in the file
            curr_mon = p.Pokemon(line[0], line[1], int(line[2]), int(line[3]), 
                                 int(line[4]), int(line[5]), int(line[6]), line[7])
            # add the new pokemon to the list of existing pokemon
            pokedex.append(curr_mon)

# I think the param here should be a list of pokemon move objects
def ParseMoves(move_set):

    # do the block of code while opening the file and setting a file pointer named csvfile
    with open("moves-data.csv", "r") as csvfile:
        # create parser with delimiter set to commas
        parser = csv.reader(csvfile, delimiter=',')

        # eliminate the header of the file
        next(parser)
        # loop through each line in the file
        for line in parser:
            
            # create move objects
            curr_move = p.Move(line[0], line[1], line[3], int(line[4]), int(line[5]), int(line[6]))
            # add move object to the list of existing moves
            move_set.append(curr_move)
            
