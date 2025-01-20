import csv
import Pokemon as p

header = []
pokemon_moves = []
pokemon_list = []
def ParseMoves(move_set):

    with open("moves-data.csv", "r") as csvfile:
        # create parser with delimiter set to commas
        parser = csv.reader(csvfile, delimiter=',')

        # eliminate the header of the file
        next(parser)
        for line in parser:
            
            # create move objects
            curr_move = p.Move(line[0], line[1], line[3], line[4], line[5], line[6])
            move_set.append(curr_move)

def ParsePokedex(pokedex):

    with open("pokemon-data.csv", "r") as csvfile:
        # create a parser that will read in each line and separate by comma
        parser = csv.reader(csvfile, delimiter=',')

        # eliminate the header of the file
        next(parser)
        for line in parser:
            # create pokemon objects
            curr_mon = p.Pokemon(line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7])
            pokedex.append(curr_mon)
            
