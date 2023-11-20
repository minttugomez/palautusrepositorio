import unittest
from statistics_service import StatisticsService, SortBy
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri", "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_players_are_set_correctly(self):
        players = self.stats._players
        list=[]
        for item in players:
            list.append(str(item))

        self.assertEqual(list, [
            str(Player("Semenko", "EDM", 4, 12)),
            str(Player("Lemieux", "PIT", 45, 54)),
            str(Player("Kurri",   "EDM", 37, 53)),
            str(Player("Yzerman", "DET", 42, 56)),
            str(Player("Gretzky", "EDM", 35, 89))
        ])
    
    def test_search_finds_player(self):
        player = str(self.stats.search("Kurri"))

        self.assertEqual(player, "Kurri EDM 37 + 53 = 90")
    
    def test_nonexistent_players_not_found(self):
        player = str(self.stats.search("Karri"))

        self.assertEqual(player, 'None')

    def test_filter_players_correctly(self):
        players = self.stats.team('EDM')
        list=[]
        for item in players:
            list.append(str(item))
        
        self.assertEqual(list, [
            str(Player("Semenko", "EDM", 4, 12)),
            str(Player("Kurri",   "EDM", 37, 53)),
            str(Player("Gretzky", "EDM", 35, 89))
        ])
    
    def test_sort_top_players_correctly_by_points(self):
        players = self.stats.top(2, SortBy.POINTS)
        list=[]
        for item in players:
            list.append(str(item))

        self.assertEqual(list, [
            str(Player("Gretzky", "EDM", 35, 89)),
            str(Player("Lemieux", "PIT", 45, 54))
        ])

    def test_sort_top_players_correctly_by_goals(self):
        players = self.stats.top(2, SortBy.GOALS)
        list=[]
        for item in players:
            list.append(str(item))

        self.assertEqual(list, [
            str(Player("Lemieux", "PIT", 45, 54)),
            str(Player("Yzerman", "DET", 42, 56))
        ])

    def test_sort_top_players_correctly_by_assists(self):
        players = self.stats.top(2, SortBy.ASSISTS)
        list=[]
        for item in players:
            list.append(str(item))

        self.assertEqual(list, [
            str(Player("Gretzky", "EDM", 35, 89)),
            str(Player("Yzerman", "DET", 42, 56))
        ])