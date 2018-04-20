


class Player:
    def __init__(self, player_id, name):
        self.cards = []
        self.id = player_id
        self.name = name
        self.hokm = ''

    # players get the hokm

    def get_hokm(self, hokm):
        self.hokm = hokm

    # player gets cards and then cards will be sorted by their type

    def get_cards(self, cards):
        self.cards = sorted(cards, key=lambda x: (x[-1]))



    # if player is hakem chooses the Court piece
    # !! must be changed!!

    def choose_hokm(self, cards):
        print(self.name, " you'r hakem! please select a card it must be 'C', 'S', 'H' or 'D'  ", cards)
        hokm = input()
        h = ['H', 'D', 'S', 'C']
        while hokm not in h:
            print("please select a card")
            hokm = input()
        return hokm

    # !! must be changed!!

    def show_cards(self):
        print("player name:", self.name, " : ", self.cards, "the Court piece is:", self.hokm)

    # !must be changed!!

    def choose_cards(self, zamine):
        print("zamine is:", zamine)
        free = True
        ch = int(input())
        if zamine != '':
            for i in self.cards:
                if zamine in i:
                    free = False
            if not free:
                while self.cards[ch][-1] != zamine:
                    print("invalid card!! zamine is:", zamine)
                    ch = int(input())
        card = self.cards[ch]
        del(self.cards[ch])
        print("your choice:", card)
        return card

    # must be changed!

    def loose_game(self, g1_score, g2_score):
        print("Game finished you lost!,your score is: ", g1_score, g2_score, self.id)

    #must be changed

    def win_game(self, g1_score, g2_score):
        print("Game finished you won the game!,your score is: ", g1_score, g2_score, self.id)

