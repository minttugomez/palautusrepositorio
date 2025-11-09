import requests
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.text import Text
from player import Player

console = Console()

class PlayerReader:
    def __init__(self, url):
        self.url = url

    def get_players(self):
        return requests.get(self.url).json()

class PlayerStats:
    def __init__(self, reader):
        self.reader = reader
        self.players = []
        for player_dict in reader.get_players():
            player = Player(player_dict)
            self.players.append(player)

    def top_scorers_by_nationality(self, nationality):
        players_by_nationality = []
        return_list = []
        for player in self.players:
            if player.nationality == nationality:
                players_by_nationality.append(player)

        sorted_players = sorted(players_by_nationality, key=lambda player: player.goals + player.assists, reverse=True)
        for player in sorted_players:
            return_list.append(player)

        return return_list

def main():
    season = input("Pick season (i.e. 2024-25): ").strip()
    nationality = input("Pick country code (i.e. FIN, SWE, CAN): ").strip().upper()

    url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    players = stats.top_scorers_by_nationality(nationality)

    console.print(f"\n[bold magenta]Season [green]{season}[/green] players from [cyan]{nationality}[/cyan]:[/bold magenta]\n")

    table = Table(show_header=True, header_style="bold magenta", border_style="bright_black")
    table.add_column("Released", style="cyan", no_wrap=True)
    table.add_column("teams", style="yellow")
    table.add_column("goals", justify="right", style="green")
    table.add_column("assists", justify="right", style="green")
    table.add_column("points", justify="right", style="bold white")

    for player in players:
        name = str(player.name)
        team = str(player.team)
        goals = str(player.goals)
        assists = str(player.assists)
        points = str(player.goals + player.assists)
        table.add_row(name, team, goals, assists, points)

    console.print(table)
    console.print(Panel(f"[italic]Season {season} players from {nationality}[/italic]", style="dim magenta"))

if __name__ == "__main__":
    main()
