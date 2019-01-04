from telbot.Court_piece.games import *
from telbot.Court_piece.players import *


def main():
    p0 = Player(0, 0)
    p1 = Player(1, 1)
    p2 = Player(2, 2)
    p3 = Player(3, 3)
    game = StandardGame(p0, p1, p2, p3)
    game.play_round()


if __name__ == "__main__":
    main()
