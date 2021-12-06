class TennisGame:
    ZERO = 0
    FIFTEEN = 1
    THIRTY = 2
    FORTY = 3
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0
        self.scores = ["Love","Fifteen","Thirty","Forty"]



    def won_point(self, player_name):
        if player_name == "player1":
            self.player1_score += 1
        else:
            self.player2_score += 1

    def get_score(self):
        if max(self.player1_score,self.player2_score) >= 4:
            return self.get_score_when_winning_possible_for_one_player()
        else:
            return self.get_score_both_playes_below_forty()
        

    def get_score_when_winning_possible_for_one_player(self):
        score_differential = self.player1_score - self.player2_score
        if score_differential == 0:
            score = "Deuce"
        elif score_differential == 1:
            score = "Advantage player1"
        elif score_differential == -1:
            score = "Advantage player2"
        elif score_differential >= 2:
            score = "Win for player1"
        else:
            score = "Win for player2"
        return score

    def get_score_both_playes_below_forty(self):
        if self.player1_score == self.player2_score:
            score = self.scores[self.player1_score]+"-"+"All" 
        else:
            score = self.scores[self.player1_score]+"-"+self.scores[self.player2_score]
        return score