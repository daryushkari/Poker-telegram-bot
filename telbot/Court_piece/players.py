import random


class Player:
    def __init__(self, player_id, player_name):
        self.player_name = player_name
        self.id = player_id
        self.cards = None

    def get_cards(self, cards):
        self.cards = sorted(cards, key=lambda x: (x[0]))
        self.cards = sorted(self.cards, key=lambda x: (x[1]))
        print(self.cards)

    def choose_trump(self):
        random_cards = self.cards[:]
        random.shuffle(random_cards)
        # Todo : should call telegram APIs
        print(random_cards[0:5])
        trump = None
        while trump not in ['S', 'H', 'D', 'C']:
            print("please choose S,H,D or C for trump", self.id)
            trump = input()
        return trump

    def validate_card(self, selected_card, background):
        if not background:
            return True
        if self.cards[selected_card][1] == background:
            return True
        x = []
        for i in self.cards:
            x.append(i[1])
        if self.cards[selected_card][1] in x:
            return False
        return True

    def choose_card(self, played_cards, background):
        # Todo : should call telegram APIs
        print("Your turn", self.id)
        print(played_cards, " ", background)
        print(self.cards)
        selected_card = -10
        while (selected_card < 0) or (selected_card >= len(self.cards)):
            try:
                selected_card = int(input())
            except ValueError:
                print("invalid input")
            if not self.validate_card(selected_card, background):
                selected_card = -10
                print("invalid card")
        return_card = self.cards[selected_card]
        del self.cards[selected_card]
        return return_card

    def get_information(self, enemy_score, your_score, enemy_round_score, your_round_score, king):
        print(enemy_score, " ", your_score, " ", enemy_round_score, " ", your_round_score, " ", king, " ", self.id)

    def get_played_cards(self, played_cards):
        print(played_cards, self.id)
