import random
from telbot.Court_piece.players import *
# class which controls games created by bot


class StandardGame:
    # a list contains cards
    cards = ['2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', '10H', '11H', '12H', '12H', '13H',
             '2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', '10D', '11D', '12D', '12D', '13D',
             '2S', '3S', '4S', '5S', '6S', '7S', '8S', '9S', '10S', '11S', '12S', '12S', '13S',
             '2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', '10C', '11C', '12C', '12C', '13C']

    # id_list is a list that contains telegram id of players
    # __init__ chooses hakem and his friend randomly

    def __init__(self, id_list, name_list):
        # variable which specifies hakem
        self.hakem = 0
        self.name_list = name_list
        random.shuffle(id_list)
        self.id_list = id_list

        # list of players
        self.pls = []

        # making players
        self.pls.append(Player(self.id_list[0], self.name_list[0]))
        self.pls.append(Player(self.id_list[1], self.name_list[1]))
        self.pls.append(Player(self.id_list[2], self.name_list[2]))
        self.pls.append(Player(self.id_list[3], self.name_list[3]))

        # players score
        self.g1_score = 0
        self.g2_score = 0

        self.round = 1

        # making first Court_piece round to play
        cards = self.cards
        random.shuffle(cards)
        self.round = GameRound(cards, self.pls, self.id_list, self.hakem)

    def make_round(self):
        pass

    def finish_round(self):
        self.hakem, winner, score = self.round.finish()
        if winner == 1:
            self.g1_score += score
        else:
            self.g2_score += score
        return self.finish_game()

    def finish_game(self):
        if self.g1_score == 7:
            print("game finished! winner is group 2")
            return True
        if self.g2_score == 7:
            print("game finished winner is group 2!")
            return True
        return False
# the class which controls every round in game and returns the winner group


class GameRound:

    # pls as players objects list
    # sh_cards are the shuffled cards array
    # id_list is the list of players telegram id list
    # hakem specifies the hakem

    def __init__(self, sh_cards, pls, id_list, hakem):
        self.pls = pls
        self.cards = sh_cards
        self. id_list = id_list
        self.hakem = hakem
        # teams score in each round
        self.g1_score = 0
        self.g2_score = 0
        self.winner = 0
        # players turn that hakem is the first player
        self.turn = self.hakem
        self.hokm = self.pls[self.hakem].choose_hokm(self.cards[(self.hakem*13)+0:(self.hakem*13)+5])
        for i in pls:
            i.get_hokm(self.hokm)
        self.run_round()

    def run_round(self):
        for i in range(4):
            self.pls[i].get_cards(self.cards[i*13:i*13+13])
            self.pls[i].show_cards()
        while self.end_round():
            zamine = ''
            crds = ['', '', '', '']
            for i in range(4):
                self.pls[self.turn].show_cards()
                crds[self.turn] = self.pls[self.turn].choose_cards(zamine)
                if i == 0:
                    zamine = crds[self.turn][-1]
                if self.turn == 3:
                    self.turn = 0
                else:
                    self.turn += 1
            dast_winner = self.detect_winner(crds, zamine)
            self.turn = dast_winner
            if dast_winner == 1 or dast_winner == 3:
                self.g2_score += 1
                print("group 2 is winner:", self.pls[1].name, "and: ", self.pls[3].name)
            elif dast_winner == 0 or dast_winner == 2:
                self.g1_score += 1
                print("group 1 is winner:", self.pls[0].name, "and: ", self.pls[2].name)
            else:
                print("ridi!")
    # detects the player which wins the mini round

    def detect_winner(self, crds, zamine):
        val_crds = [0, 0, 0, 0]
        for i in range(4):
            if crds[i][-1] == self.hokm:
                fir = str(crds[i][:-1])
                val_crds[i] = 13 + int(fir)
            elif crds[-1] == zamine:
                fir = str(crds[i][:-1])
                val_crds[i] = int(fir)
            else:
                val_crds[i] = 0
        return val_crds.index(max(val_crds))

    def new_round(self, sh_cards, hakem):
        pass

    # the end function controls the round is over or not
    # if round is over then specifies the winner group and their added score

    def end_round(self):
        if self.g1_score == 7:
            self.winner = 1
            return False
        if self.g2_score == 7:
            self.winner = 2
            return False
        return True
    # function that returns the winner team, their score and the hakem

    def finish(self):
        score = 1
        if self.winner == 1:
            if self.g2_score == 0:
                score = 2
            # hakem is in the looser team
            if self.hakem == 1:
                self.hakem = 2

            if self.hakem == 3:
                self.hakem = 0
        if self.winner == 2:
            #if self.g1_score == 0:
            #    score = 2
            if self.hakem == 0 or self.hakem == 2:
                self.hakem += 1
                #if self.g1_score == 0:
                    #score = 3
        return self.hakem, self.winner, score

