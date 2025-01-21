import Pokemon as p
import FileParser as fp

def StartColosseum():
    pokedex = []
    moves = []

    fp.ParseMoves(moves)
    fp.ParsePokedex(pokedex)


if __name__ == "__main__":
    StartColosseum()