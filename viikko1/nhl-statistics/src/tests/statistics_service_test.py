import unittest
from statistics_service import StatisticsService

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
        self.players= [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri", "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
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
        player = self.stats.search("em")
        self.assertIsNotNone(player)
        self.assertEqual(player.name, "Semenko")

    def test_team_returns_correct_players(self):
        edm_players = self.stats.team("EDM")
        names = [p.name for p in edm_players]
        self.assertCountEqual(names, ["Semenko", "Kurri", "Gretzky"])

    def test_team_returns_empty_list_for_nonexistent_team(self):
        result = self.stats.team("XYZ")
        self.assertEqual(result, [])

    def test_top_returns_correct_number_of_players(self):
        top_players = self.stats.top(2)
        self.assertEqual(len(top_players), 3)
        self.assertEqual(top_players[0].name, "Gretzky")

    def test_top_zero_returns_one_player(self):
        top_players = self.stats.top(0)
        self.assertEqual(len(top_players), 1)
        self.assertEqual(top_players[0].name, "Gretzky")

    def test_top_raises_indexerror_if_how_many_too_large(self):
        with self.assertRaises(IndexError):
            self.stats.top(10)
