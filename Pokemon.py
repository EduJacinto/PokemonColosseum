# class containing definition of pokemon object
class Pokemon:
    def __init__(self, name, type, hp, attack, defense, moves):
        self.name = name
        self.type = type
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.moves = moves

# class containing definition of move objects
class Move:
    def __init__(self, name, type, category, contest, pp, power, accuracy):
        self.name = name
        self.type = type
        self.category = category
        self.contest = contest
        self.pp = pp
        self.power = power
        self.accuracy = accuracy