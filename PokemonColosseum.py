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

def player_turn(player_pokemon, bot):
    # choose the move that will be used
    # do the math on damage
    # assign damage to the opp pokemon
    # if the pokemon faints, back to pokeball and send dout the next one
    # randomly choose which move the opp will use
    # calc damage and aassign it to the player's pokemon
    pass

def bot_turn(player_pokemon, bot):
    # randomly choose the bot's next move
    # calc damage and assign to the player hp
    # if player curr pokemon faints, then pop the next one off of the deque
    pass

def player_first(player, opponent):
    # each move has pp == 1 until all moves have been used, then pp is replenished
    # team rocket decides randomly which attack to use so just print their move and results
    # give player choice of which move to use then print the frame of battle and results
    while True:
        curr_player_pokemon = player.team.popleft()
        curr_rocket_pokemon = opponent.popleft()

        # while both teams still have pokemon, continue battle
        while player.team and opponent:
            
            player_turn(curr_player_pokemon, curr_rocket_pokemon)
            if curr_rocket_pokemon.hp <= 0:
                print("\n" + curr_rocket_pokemon.name + " fainted and returned to its pokéball")
                
                if not opponent:
                    print("\nAll of Team Rocket's pokémon fainted! " + player.name + " wins the match!")
                else:
                    curr_rocket_pokemon = opponent.popleft()
           
            bot_turn(curr_player_pokemon, curr_rocket_pokemon)
            
            if curr_player_pokemon.hp <= 0:
                print("\n" + curr_player_pokemon.name + " fainted and returned to its pokéball!")
                
                if not player.team:
                    print("\nAll of " + player.name + "'s pokémon fainted! Team Rocket wins the match!")
                else:
                    curr_player_pokemon = player.team.popleft()

def bot_first(player, opponent):
    # each move has pp == 1 until all moves have been used, then pp is replenished
    # team rocket decides randomly which attack to use so just print their move and results
    # give player choice of which move to use then print the frame of battle and results
    while True:
        curr_player_pokemon = player.team.popleft()
        curr_rocket_pokemon = opponent.popleft()

        # while both teams still have pokemon, continue battle
        while player.team and opponent:
            
            # team rocket's turn. check if the player's pokemon fainted.
            bot_turn(curr_player_pokemon, curr_rocket_pokemon)
            
            if curr_player_pokemon.hp <= 0:
                print("\n" + curr_player_pokemon.name + " fainted and returned to its pokéball!")
                
                if not player.team:
                    print("\nAll of " + player.name + "'s pokémon fainted! Team Rocket wins the match!")
                else:
                    curr_player_pokemon = player.team.popleft()

            # player's turn. check if bot's pokemon fainted.
            player_turn(curr_player_pokemon, curr_rocket_pokemon)

            if curr_rocket_pokemon.hp <= 0:
                print("\n" + curr_rocket_pokemon.name + " fainted and returned to its pokéball")
                
                if not opponent:
                    print("\nAll of Team Rocket's pokémon fainted! " + player.name + " wins the match!")
                else:
                    curr_rocket_pokemon = opponent.popleft()
           

# main game function. Magikarp is the only pokemon that doesn't have 5 moves (1)
def StartColosseum():
    # declare the two lists and populate them by parsing the csv files
    pokedex = []
    moves = []
    fp.ParseMoves(moves)
    fp.ParsePokedex(pokedex)

    # Now that data is processed, play game
    print( "░█▀█░█▀█░█░█░█▀▀░█▄█░█▀█░█▀█░░░█▀▀░█▀█░█░░░█▀█░█▀▀░█▀▀░█▀▀░█░█░█▄█\n" +
           "░█▀▀░█░█░█▀▄░█▀▀░█░█░█░█░█░█░░░█░░░█░█░█░░░█░█░▀▀█░▀▀█░█▀▀░█░█░█░█\n" + 
           "░▀░░░▀▀▀░▀░▀░▀▀▀░▀░▀░▀▀▀░▀░▀░░░▀▀▀░▀▀▀░▀▀▀░▀▀▀░▀▀▀░▀▀▀░▀▀▀░▀▀▀░▀░▀" )

    # take input for the desired player name
    player = p.Player( input("\nWhat's your name?") )
    print("\nWelcome to the Pokémon Colosseum, " + player.name)
    # create the Team Rocket team, queue
    team_rocket = deque()

    # I think this could be condensed into one while loop
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
    # complete player object
    player.team = player_team

    # introduce both teams like in the game and declare which pokemon are in their team of three in order
    print("\nTeam Rocket enters the battlefield with " + team_rocket[0].name + ", " + team_rocket[1].name + ", and " + team_rocket[2].name + "!\n")
    print(player.name + " enters with " + player.team[0].name + ", " + player.team[1].name + ", and " + player.team[2].name + "!\n")

    # coin toss to decide who attacks first print results
    coin_toss = "Team Rocket" if random.randint(1, 2) == 1 else player.name
    print("Let the battle begin!!\n")
    print("The coin toss goes to ... " + coin_toss)

    if coin_toss == "Team Rocket":
        bot_first(player, team_rocket)
    elif coin_toss == player.name:
        player_first(player, team_rocket)


if __name__ == "__main__":
    StartColosseum()