import Pokemon as p
import FileParser as fp
import random
from collections import deque

# series of if statements returning type efficiency for a move used
def TypeEfficiency(move, pokemon):

    if move.type == 'Normal':
        return 1
    elif move.type == 'Fire' and (pokemon.type == 'Fire' or pokemon.type == 'Water'):
        return 0.5
    elif move.type == 'Water' and (pokemon.type == 'Water' or pokemon.type == 'Grass'):
        return 0.5
    elif move.type == 'Electric' and (pokemon.type == 'Electric' or pokemon.type == 'Grass'):
        return 0.5
    elif move.type == 'Grass' and (pokemon.type == 'Fire' or pokemon.type == 'Grass'):
        return 0.5
    elif move.type == 'Fire' and pokemon.type == 'Grass':
        return 2
    elif move.type == 'Water' and pokemon.type == 'Fire':
        return 2
    elif move.type == 'Electric' and pokemon.type == 'Water':
        return 2
    elif move.type == 'Grass' and pokemon.type == 'Water':
        return 2
    else:
        return 1
    
#  compute damage to be dealt, by pokemon a, to pokemon b
def damage(move, a, b):

    # assign same type attack bonus
    stab = 1.5 if a.type == move.type else 1

    # compute the damage that will be dealt by a move
    damage_dealt = move.power * (a.attack / b.defense) * stab * TypeEfficiency(move, b) * random.uniform(0.5, 1)
    return damage_dealt

# main game function. Magikarp is the only pokemon that doesn't have 5 moves (1)
def StartColosseum():
    # declare the two lists and populate them by parsing the csv files
    pokedex = []
    moves = []
    fp.ParseMoves(moves)
    fp.ParsePokedex(pokedex)

    # Now that data is processed, play game
    print
    ( "░█▀█░█▀█░█░█░█▀▀░█▄█░█▀█░█▀█░░░█▀▀░█▀█░█░░░█▀█░█▀▀░█▀▀░█▀▀░█░█░█▄█\n"
    + "░█▀▀░█░█░█▀▄░█▀▀░█░█░█░█░█░█░░░█░░░█░█░█░░░█░█░▀▀█░▀▀█░█▀▀░█░█░█░█\n"
    + "░▀░░░▀▀▀░▀░▀░▀▀▀░▀░▀░▀▀▀░▀░▀░░░▀▀▀░▀▀▀░▀▀▀░▀▀▀░▀▀▀░▀▀▀░▀▀▀░▀▀▀░▀░▀" )

    # take input for the desired player name
    player_name = input("What's your name?")
    print("Welcome to the Pokémon Colosseum," + player_name)
    # create the Team Rocket team, queue
    team_rocket = deque()

    i = 0
    while i < 3:
        # add a random pokemon to the queue
        rand_pok = random.randint( 0, len(pokedex)-1 )
        # append to the queue by popping the generated index off of the pokedex list. Ensures that all pokemon are unique.
        team_rocket.append( pokedex.pop(rand_pok) )
        
        # only increment i after each pokemon is added to the team_rocket queue
        i += 1

    # then build the player team, stored in a queue and create the player object
    player_team = deque()
    i = 0
    while i < 3:
        rand_pok = random.randint( 0, len(pokedex) - 1 )
        player_team.append( pokedex.pop(rand_pok) )
        i += 1
    # create player object
    player = p.Player(player_name, player_team)

    # introduce both teams like in the game and declare which pokemon are in their team of three in order

    # let the battle begin

    # coin toss to decide who attacks first print results

    # team rocket decides randomly which attack to use so just print their move and results

    # give player choice of which move to use then print the frame of battle and results

    # each move has pp == 1 until all moves have been used, then pp is replenished

if __name__ == "__main__":
    StartColosseum()