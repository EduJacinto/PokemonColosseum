import Pokemon as p
import FileParser as fp
import random
from collections import deque

'''
Series of if statements returning type efficiency for a move used

parameters:
move - the move that was cast
pokemon - the pokemon on which the move will be used on
'''
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
    

'''
Compute damage to be dealt, by pokemon a, to pokemon b

parameters:
move - the move that pokemon a will cast on pokemon b
a - pokemon casting the move
b - pokemon that will receive damage
'''
def damage(move, a, b):
    # assign same type attack bonus
    stab = 1.5 if a.type == move.type else 1

    # compute the damage that will be dealt by a move
    damage_dealt = move.power * (a.attack / b.defense) * stab * TypeEfficiency(move, b) * random.uniform(0.5, 1)
    return damage_dealt


'''
Game logic for the player's turn. Prints available move options to the player.
Takes input and handles input errors if they occur. Computes damage to be dealt
and updates opponent pokemon hp accordingly.

parameter:
player_pokemon - the player's current pokemon on the battlefield
rocket_pokemon - the npc's current pokemon on the battlefield
'''
def player_turn(player_pokemon, rocket_pokemon):

    # Check if all moves have been used. If so, restore all moves and clear the used moves deque.
    if not player_pokemon.moves:
        player_pokemon.moves = deque(player_pokemon.used_moves)
        player_pokemon.used_moves.clear()

    while True:
        try:
            print(f"Choose the move that {player_pokemon.name} will use:")
            for i, move in enumerate(player_pokemon.moves):
                print(f"{i + 1}. {move.name}")
            
            choice = int(input()) - 1
            
            if 0 <= choice < len(player_pokemon.moves):
                break
            else:
                print(f"\n{player_pokemon.name} does not understand what you mean! Try again.\n")
            
        except ValueError:
            print(f"\n{player_pokemon.name} does not understand what you mean! Try again.\n")
    
    used_move = player_pokemon.moves[choice]
    del player_pokemon.moves[choice]
    player_pokemon.used_moves.append(used_move)

    damage_dealt = damage(used_move, player_pokemon, rocket_pokemon)
    rocket_pokemon.hp -= damage_dealt
    print(f"\n{player_pokemon.name} used {used_move.name}!\nIt dealt { int(damage_dealt) } damage to {rocket_pokemon.name}!")


'''
Game logic for randomly choosing which move the npc will use on the player's pokemon.
Damage is calculated and the player's pokemon's hp is updated.

parameters:
player_pokemon - the player's current pokemon on the battlefield
rocket_pokemon - the npc's current pokemon on the battlefield
'''
def bot_turn(player_pokemon, rocket_pokemon):
   
    if not rocket_pokemon.moves:
        rocket_pokemon.moves = deque(rocket_pokemon.used_moves)
        rocket_pokemon.used_moves.clear()

    used_move = random.choice(rocket_pokemon.moves)
    rocket_pokemon.moves.remove(used_move)
    damage_dealt = damage(used_move, rocket_pokemon, player_pokemon)
    player_pokemon.hp -= damage_dealt
    print(f"\nTeam Rocket's {rocket_pokemon.name} used {used_move.name}!\nIt dealt { int(damage_dealt) } damage to {player_pokemon.name}!\n")

'''
Game logic if the player is to go first.

parameters:
player - the player object
opponent_team - the npc's team
'''
def player_first(player, opponent_team):
    
    curr_player_pokemon = player.team.popleft()
    curr_rocket_pokemon = opponent_team.popleft()
    print(f"{player.name} starts with {curr_player_pokemon.name}\nTeam Rocket starts with {curr_rocket_pokemon.name}\n")

    # while both teams still have pokemon, continue battle
    while True:  
        # player's turn. check if bot's pokemon fainted.
        player_turn(curr_player_pokemon, curr_rocket_pokemon)

        # check if team rocket pokemon fainted and then if they are all fainted
        if curr_rocket_pokemon.hp <= 0:
            print(f"{curr_rocket_pokemon.name} fainted and returned to its pokéball!")
            
            if not opponent_team:
                print(f"\nAll of Team Rocket's pokémon fainted! {player.name} wins the match!\n")
                break
            else:
                curr_rocket_pokemon = opponent_team.popleft()
                print(f"Team Rocket sent out {curr_rocket_pokemon.name}")
        
        # team rocket's turn. check if the player's pokemon fainted.
        bot_turn(curr_player_pokemon, curr_rocket_pokemon)
        
        # check if player's pokemon fainted, and then if all of them fainted
        if curr_player_pokemon.hp <= 0:
            print(f"\n{curr_player_pokemon.name} fainted and returned to its pokéball!")
            
            if not player.team:
                print(f"\nAll of {player.name}'s pokémon fainted! Team Rocket wins the match!\n")
                break
            else:
                curr_player_pokemon = player.team.popleft()
                print(f"{player.name} sent out {curr_player_pokemon.name}\n")


'''
Game logic if the npc is to go first.

parameters:
player - player object
opponent_team - npc team
'''
def bot_first(player, opponent_team):
    
    curr_player_pokemon = player.team.popleft()
    curr_rocket_pokemon = opponent_team.popleft()
    print(f"Team Rocket starts with {curr_rocket_pokemon.name}\n{player.name} starts with {curr_player_pokemon.name}")

    # while both teams still have pokemon, continue battle
    while True:
        # team rocket's turn. check if the player's pokemon fainted.
        bot_turn(curr_player_pokemon, curr_rocket_pokemon)
        
        # check if player's pokemon fainted, and then if all of them fainted
        if curr_player_pokemon.hp <= 0:
            print(f"{curr_player_pokemon.name} fainted and returned to its pokéball!")
            
            if not player.team:
                print(f"\nAll of {player.name}'s pokémon fainted! Team Rocket wins the match!")
                break
            else:
                curr_player_pokemon = player.team.popleft()
                print(f"{player.name} sent out {curr_player_pokemon.name}\n")

        # player's turn. check if bot's pokemon fainted.
        player_turn(curr_player_pokemon, curr_rocket_pokemon)

        # check if team rocket pokemon fainted and then if they are all fainted
        if curr_rocket_pokemon.hp <= 0:
            print(f"\n{curr_rocket_pokemon.name} fainted and returned to its pokéball")
            
            if not opponent_team:
                print(f"\nAll of Team Rocket's pokémon fainted! {player.name} wins the match!")
                break
            else:
                curr_rocket_pokemon = opponent_team.popleft()
                print(f"Team Rocket sent out {curr_rocket_pokemon.name}")
           

# main game function
def StartColosseum():
    # declare the two lists and populate them by parsing the csv files
    pokedex = []
    moves = []
    fp.ParseMoves(moves)
    fp.ParsePokedex(pokedex, moves)

    # Now that data is processed, start game by printing the title
    print( "░█▀█░█▀█░█░█░█▀▀░█▄█░█▀█░█▀█░░░█▀▀░█▀█░█░░░█▀█░█▀▀░█▀▀░█▀▀░█░█░█▄█\n" +
           "░█▀▀░█░█░█▀▄░█▀▀░█░█░█░█░█░█░░░█░░░█░█░█░░░█░█░▀▀█░▀▀█░█▀▀░█░█░█░█\n" + 
           "░▀░░░▀▀▀░▀░▀░▀▀▀░▀░▀░▀▀▀░▀░▀░░░▀▀▀░▀▀▀░▀▀▀░▀▀▀░▀▀▀░▀▀▀░▀▀▀░▀▀▀░▀░▀" )

    # take input for the desired player name, trim white space, and welcome player
    player = p.Player(input("\nWhat's your name?").strip() )
    print(f"\nWelcome to the Pokémon Colosseum, {player.name}")

    # create the Team Rocket and player teams
    team_rocket = deque()
    player_team = deque()
    for i in range(3):

        rand_pok = random.randint( 0, len(pokedex) - 1 )
        player_team.append( pokedex.pop(rand_pok) )

        rand_pok = random.randint( 0, len(pokedex)-1 )
        team_rocket.append( pokedex.pop(rand_pok) )
        
    # complete player object
    player.team = player_team

    # introduce both teams like in the game and declare which pokemon are in their team of three
    print(f"\nTeam Rocket enters the battlefield with {team_rocket[0].name}, {team_rocket[1].name}, and {team_rocket[2].name}!\n")
    print(f"{player.name} enters with {player.team[0].name}, {player.team[1].name}, and {player.team[2].name}!\n")

    # coin toss to decide who attacks first print results
    coin_toss = "Team Rocket" if random.randint(1, 2) == 1 else player.name
    
    print("The coin toss goes to ... " + coin_toss)
    print("Let the battle begin!!\n")

    # start battle depending on coin toss
    if coin_toss == "Team Rocket":
        bot_first(player, team_rocket)
    elif coin_toss == player.name:
        player_first(player, team_rocket)


if __name__ == "__main__":
    StartColosseum()