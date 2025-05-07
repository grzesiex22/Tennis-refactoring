class TennisGame3:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_points = 0
        self.player2_points = 0

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.player1_points += 1
        else:
            self.player2_points += 1

    def _is_early_game(self):
        return self.player1_points < 4 and self.player2_points < 4 and (self.player1_points + self.player2_points < 6)

    def _early_score(self):
        points_names = ["Love", "Fifteen", "Thirty", "Forty"]
        if self.player1_points == self.player2_points:
            return points_names[self.player1_points] + "-All"
        else:
            return points_names[self.player1_points] + "-" + points_names[self.player2_points]

    def _endgame_score(self):
        winning_player = self.player1_name if self.player1_points > self.player2_points else self.player2_name
        if abs(self.player1_points - self.player2_points) == 1:
            return "Advantage " + winning_player
        else:
            return "Win for " + winning_player

    def score(self):
        if self._is_early_game():
            return self._early_score()
        elif self.player1_points == self.player2_points:
            return "Deuce"
        else:
            return self._endgame_score()
