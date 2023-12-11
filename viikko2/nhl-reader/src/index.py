import requests
from player import Player

class PlayerReader:

    def __init__(self, url):
        self.url = url
        self.players = []

    def __fetch(self):
        response = requests.get(self.url).json()
        for player_dict in response:
            player = Player(player_dict)
            self.players.append(player)

    def list(self):
        self.__fetch()
        return self.players

    def __str__(self):
        self.__fetch()
        player_info = [str(player) for player in self.players]
        return '\n'.join(player_info)
    
class PlayerStats:

    def __init__(self, playerreader, nationality = ""):
        self.reader = playerreader
        self.playerlist = []
        self.nationality = nationality

    def __stats(self):
        players = self.reader.list()

        if self.nationality != "":
            for player in players:
                if player.nationality == self.nationality:
                    self.playerlist.append(player)
        else:
            for player in players:
                self.playerlist.append(player)
        
        self.playerlist = sorted(self.playerlist, key=lambda x: x.goals_and_assists(), reverse=True)

    def __str__(self):
        self.__stats()
        string = f"Players from {self.nationality}\n"
        for player in self.playerlist:
            string += "\n" + str(player)
        return string

def main():
    Reader = PlayerReader("https://studies.cs.helsinki.fi/nhlstats/2022-23/players")
    Stats = PlayerStats(Reader, "FIN")
    print(Stats)