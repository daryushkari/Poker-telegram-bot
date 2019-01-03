import random
from telbot.Court_piece.players import Player

# game controller class


class StandardGame:
    # a list contains cards
    H_cards = [[i, 'H'] for i in range(2, 14)]
    D_cards = [[i, 'D'] for i in range(2, 14)]
    S_cards = [[i, 'S'] for i in range(2, 14)]
    C_cards = [[i, 'C'] for i in range(2, 14)]
    cards = [H_cards[:], D_cards[:], S_cards[:], C_cards[:]]
    # players is a list of Player objects

    def __init__(self, player0: Player, player1: Player, player2: Player, player3: Player):
        self.players = [player0, player1, player2, player3]
        self.king = None
        self.round = 0
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

    def give_cards(self):
        shuffled_cards = self.shuffle_cards()
        self.players[0].get_cards(shuffled_cards['player0'])
        self.players[1].get_cards(shuffled_cards['player1'])
        self.players[2].get_cards(shuffled_cards['player2'])
        self.players[3].get_cards(shuffled_cards['player3'])

    def choose_king(self):
        if self.round == 0:
            self.king = random.randint(0,3)
        else:
            if self.king == 3:
                self.king = 0
            else:
                self.king += 1


    def play_round(self):
        self.give_cards()
        team_one_round_score = 0
        team_tow_round_score = 0
        round_turn = self.king
        trump = self.players[self.king].choose_trump()
        while (team_one_round_score >= 7 ) or (team_tow_round_score >= 7):
            played_cards = []

