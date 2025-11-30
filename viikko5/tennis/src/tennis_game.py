class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def __str__(self):
        return self.name

    def score_point(self):
        self.score += 1

    def points(self):
        return self.score

class TennisGame:
    def __init__(self, player1, player2):
        self.player1 = Player(player1)
        self.player2 = Player(player2)

    def won_point(self, player):
        if player == str(self.player1):
            self.player1.score_point()
        elif player == str(self.player2):
            self.player2.score_point()
        else:
            raise ValueError(f"Player name '{player}' does not match either player in the game.")
    def get_score(self):
        score = ""
        advantage = self.check_advantage()
        win = self.check_win()

        if win:
            score = f"Win for {str(win)}"
        elif advantage:
            score = f"Advantage {str(advantage)}"
        elif self.player1.points() == self.player2.points():
            score = self.get_even_points(self.player1.points())
        else:
            score = f"{self.get_points(self.player1.points())}-{self.get_points(self.player2.points())}"

        return score

    def get_points(self, score):
        if score == 0:
            return "Love"
        elif score == 1:
            return "Fifteen"
        elif score == 2:
            return "Thirty"
        elif score == 3:
            return "Forty"
        else:
            raise ValueError(f"Invalid score for get_points: {score}")
    def get_even_points(self, points):
        if points == 0:
            return "Love-All"
        elif points == 1:
            return "Fifteen-All"
        elif points == 2:
            return "Thirty-All"
        else:
            return "Deuce"

    def check_advantage(self):
        if self.player1.points() >= 4 and self.player1.points() - self.player2.points() == 1:
            return self.player1
        elif self.player2.points() >= 4 and self.player2.points() - self.player1.points() == 1:
            return self.player2
        return None

    def check_win(self):
        if self.player1.points() >= 4 and self.player1.points() - self.player2.points() >= 2:
            return self.player1
        elif self.player2.points() >= 4 and self.player2.points() - self.player1.points() >= 2:
            return self.player2
        return None