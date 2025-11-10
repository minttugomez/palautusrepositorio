""" docstring """

class Player:
    """ docstring """
    def __init__(self, dictionary):
        """ docstring """
        self.name = dictionary['name']
        self.nationality = dictionary['nationality']
        self.assists = dictionary['assists']
        self.goals = dictionary['goals']
        self.team = dictionary['team']
        self.games = dictionary['games']
        self.id = dictionary['id']

    def __str__(self):
        """ docstring """
        return f"{self.name:25} {self.team:20} {self.goals} + {self.assists} = {self.goals + self.assists}"
