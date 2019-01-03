import random
import telbot.Court_piece.players

# game controller class


class StandardGame:
    # a list contains cards
    H_cards = [[i, 'H'] for i in range(2, 14)]
    D_cards = [[i, 'D'] for i in range(2, 14)]
    S_cards = [[i, 'S'] for i in range(2, 14)]
    C_cards = [[i, 'C'] for i in range(2, 14)]
    cards = [H_cards[:], D_cards[:], S_cards[:], C_cards[:]]
    # players is a list of Player objects

    def __init__(self, players):
        self.players = players
        # players[0] and players[2] in first_team
        self.team_one_game_score = 0
        # players[1] and players[3] in second team
        self.team_tow_game_score = 0

    def shuffle_cards(self):
        shuffled_cards = self.cards[:]
        random.shuffle(self.shuffle_cards)
        shuffled_cards = {'player0': shuffled_cards[0:13],
                          'player1': shuffled_cards[13:26],
                          'player2': shuffled_cards[26:39],
                          'player3': shuffled_cards[39:]}
        return shuffled_cards


