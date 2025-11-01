import unittest
from statistics_service import StatisticsService, SortBy

class Player:
    def __init__(self, name, team, goals, assists):
        self.name = name
        self.team = team
        self.goals = goals
        self.assists = assists

    @property
    def points(self):
        return self.goals + self.assists

    def __str__(self):
        return f"{self.name} {self.team} {self.goals} + {self.assists} = {self.points}"

class PlayerReaderStub:
    def __init__(self):
        self.players = [
            Player("Semenko", "EDM", 4, 12),     # 16
            Player("Lemieux", "PIT", 45, 54),    # 99
            Player("Kurri", "EDM", 37, 53),      # 90
            Player("Yzerman", "DET", 42, 56),    # 98
            Player("Gretzky", "EDM", 35, 89)     # 124
        ]

    def get_players(self):
        return self.players


class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.stats = StatisticsService(PlayerReaderStub())

    def test_search_finds_exact_match(self):
        player = self.stats.search("Lemieux")
        self.assertIsNotNone(player)
        self.assertEqual(player.name, "Lemieux")

    def test_search_returns_none_if_not_found(self):
        player = self.stats.search("Nonexistent")
        self.assertIsNone(player)

    def test_search_partial_name_match(self):
        player = self.stats.search("men")
        self.assertIsNotNone(player)
        self.assertEqual(player.name, "Semenko")

    def test_team_returns_correct_players(self):
        edm_players = self.stats.team("EDM")
        names = [p.name for p in edm_players]
        self.assertCountEqual(names, ["Semenko", "Kurri", "Gretzky"])

    def test_team_returns_empty_list_for_nonexistent_team(self):
        result = self.stats.team("XYZ")
        self.assertEqual(result, [])

    def test_top_by_points(self):
        top_players = self.stats.top(2, SortBy.POINTS)
        # returns how_many + 1 = 3 players
        self.assertEqual(len(top_players), 3)
        # top 3 by points: Gretzky (124), Lemieux (99), Yzerman (98)
        self.assertEqual([p.name for p in top_players],
                         ["Gretzky", "Lemieux", "Yzerman"])

    def test_top_by_goals(self):
        top_players = self.stats.top(1, SortBy.GOALS)
        # returns how_many + 1 = 2 players
        self.assertEqual([p.name for p in top_players],
                         ["Lemieux", "Yzerman"])

    def test_top_by_assists(self):
        top_players = self.stats.top(1, SortBy.ASSISTS)
        self.assertEqual([p.name for p in top_players],
                         ["Gretzky", "Yzerman"])

    def test_top_zero_returns_one_player(self):
        result = self.stats.top(0, SortBy.POINTS)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].name, "Gretzky")

    def test_top_how_many_greater_than_list_length_raises_indexerror(self):
        # while loop uses <=, so exceeding list size causes IndexError
        with self.assertRaises(IndexError):
            self.stats.top(10, SortBy.POINTS)
