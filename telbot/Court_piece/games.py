import random
import telbot.Court_piece.players

# game controller class


class StandardGame:
    # a list contains cards
    cards = ['2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', '10H', '11H', '12H', '12H', '13H',
             '2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', '10D', '11D', '12D', '12D', '13D',
             '2S', '3S', '4S', '5S', '6S', '7S', '8S', '9S', '10S', '11S', '12S', '12S', '13S',
             '2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', '10C', '11C', '12C', '12C', '13C']

    # players is a list of Player objects

    def __init__(self, players):
        self.players = players
        self.round_king = None
        # players[0] and players[2] in first_team
        self.team_one_game_score = 0
        # players[1] and players[3] in second team
        self.team_tow_game_score = 0

    def shuffle_cards(self):
        shuffled_cards = random.shuffle(self.cards)
        shuffled_cards = {'player0': shuffled_cards[0:13],
                          'player1': shuffled_cards[13:26],
                          'player2': shuffled_cards[26:39],
                          'player3': shuffled_cards[39:],}
        return shuffled_cards

    def choose_trump(self):
