import random
from telbot.Court_piece.players import Player

# game controller class


class StandardGame:
    # a list contains cards
    H_cards = [[i, 'H'] for i in range(2, 15)]
    D_cards = [[i, 'D'] for i in range(2, 15)]
    S_cards = [[i, 'S'] for i in range(2, 15)]
    C_cards = [[i, 'C'] for i in range(2, 15)]
    cards = H_cards[:] + D_cards[:] + S_cards[:] + C_cards[:]
    # players is a list of Player objects

    def __init__(self, player0: Player, player1: Player, player2: Player, player3: Player):
        self.players = [player0, player1, player2, player3]
        self.king = random.randint(0, 3)
        self.round = 0
        # players[0] and players[2] in first_team
        self.team_one_game_score = 0
        # players[1] and players[3] in second team
        self.team_tow_game_score = 0

    def shuffle_cards(self):
        shuffled_cards = self.cards[:]
        random.shuffle(shuffled_cards)
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

    @staticmethod
    def go_turn(turn):
        if turn == 3:
            return 0
        return turn + 1

    @staticmethod
    def winner_player(trump, played_cards, background):
        print(played_cards)
        best_cards = []
        for i in played_cards:
            if i[1][1] == trump:
                best_cards.append(i)
        if best_cards:
            best_cards = sorted(best_cards, key=lambda x: (x[1][0]))
            return best_cards[-1][0]
        for i in played_cards:
            if i[1][1] == background:
                best_cards.append(i)
        best_cards = sorted(best_cards, key=lambda x: (x[1][0]))
        return best_cards[-1][0]

    @staticmethod
    def winner_team(winner_player):
        if (winner_player == 0) or (winner_player == 2):
            return 1
        return 2

    def play_trick(self, round_turn):
        played_cards = []
        background = None
        for i in range(0, 4):
            selected_card = self.players[round_turn].choose_card(played_cards, background)
            if not played_cards:
                background = selected_card[1]
            played_cards.append([round_turn, selected_card])
            round_turn = self.go_turn(round_turn)

        return played_cards, background

    def play_round(self):
        self.give_cards()
        team_one_round_score = 0
        team_tow_round_score = 0
        round_turn = self.king
        trump = self.players[self.king].choose_trump()
        while (team_one_round_score < 7) and (team_tow_round_score < 7):
            played_cards, background = self.play_trick(round_turn)
            winner_player = self.winner_player(trump, played_cards, background)
            winner_team = self.winner_team(winner_player)
            round_turn = winner_player
            if winner_team == 1:
                team_one_round_score += 1
            else:
                team_tow_round_score += 1
            print(team_one_round_score, team_tow_round_score)
        if team_one_round_score == 7:
            round_winner_team = 1
        else:
            round_winner_team = 2
        print(team_one_round_score, team_tow_round_score, round_winner_team)
        return round_winner_team

    def play_game(self):
        while (self.team_one_game_score < 7) and (self.team_tow_game_score < 7):
            winner_team = self.play_round()
            if winner_team == 1:
                self.team_one_game_score += 1
            else:
                self.team_tow_game_score += 1
        print(self.team_one_game_score, self.team_tow_game_score)
