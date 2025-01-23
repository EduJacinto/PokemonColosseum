import Pokemon as p
import FileParser as fp
import random

# series of if statements returning type efficiency
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
    

def damage(move, a, b):

    # assign same type attack bonus
    stab = 1.5 if a.type == move.type else 1
    
    # compute the damage that will be dealt by a move
    damage_dealt = move.power * (a.attack / b.defense) * stab * TypeEfficiency(move, b) * random.random(0.5, 1)
    return damage_dealt

def StartColosseum():
    pokedex = []
    moves = []

    fp.ParseMoves(moves)
    fp.ParsePokedex(pokedex)


if __name__ == "__main__":
    StartColosseum()