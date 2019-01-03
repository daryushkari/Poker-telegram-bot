import random


class Player:
    def __init__(self, player_id):
        self.id = player_id
        self.cards = None
        self.game_score = 0
        self.enemy_game_score = 0
        self.round_score = 0
        self.enemy_round_score = 0

    def get_cards(self, cards):
        self.cards = sorted(cards, key=lambda x: (x[0]))
        self.cards = sorted(self.cards, key=lambda x: (x[1]))

