class Player:
    def __init__(self, dict):
        self.name = dict['name']
        self.nationality = dict['nationality']
        self.assists = dict['assists']
        self.goals = dict['goals']
        self.penalties = dict['penalties']
        self.team = dict['team']
        self.games = dict['games']
    
    def __str__(self):
        return f"{self.name} {self.nationality}, team {self.team}, goals {self.goals}, assists {self.assists}"
    
    def goals_and_assists(self):
        return int(self.goals + self.assists)