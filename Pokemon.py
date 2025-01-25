# class containing definition of pokemon object
class Pokemon:
    def __init__(self, name, type, hp, attack, defense, height, weight, moves):
        self.name = name
        self.type = type
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.height = height
        self.weight = weight
        self.moves = moves

# class containing definition of move objects
class Move:
    def __init__(self, name, type, category, contest, pp, power, accuracy=None):
        self.name = name
        self.type = type
        self.category = category
        self.contest = contest
        self.pp = pp
        self.power = power
        self.accuracy = accuracy

# create player object
class Player:
    def __init__(self, name, team):
        self.name = name
        self.team = team