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

    def choose_card(self, enemy_score, your_score, enemy_round_score, your_round_score, played_cards):
        print("Your turn")
        print(enemy_score, " ", your_score, " ", enemy_round_score, " ", your_round_score, played_cards)
        print(self.cards)
        selected_card = -10
        while (selected_card < 0) or (selected_card >= len(self.cards)):
            try:
                selected_card = int(input())
            except ValueError:
                print("invalid input")
        return_card = self.cards[selected_card]
        del self.cards[selected_card]
        return return_card
