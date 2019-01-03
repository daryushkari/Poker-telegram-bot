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

    def choose_trump(self):
        random_cards = self.cards[:]
        random.shuffle(random_cards)
        # Todo : should call telegram APIs
        print(random_cards[0:5])
        trump = None
        while trump not in ['S', 'H', 'D', 'C']:
            print("please choose S,H,D or C for trump")
            trump = input()
        return trump

