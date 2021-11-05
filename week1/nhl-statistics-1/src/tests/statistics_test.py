import unittest
from statistics import Statistics
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        # annetaan Statistics-luokan oliolle "stub"-luokan olio
        self.statistics = Statistics(
            PlayerReaderStub()
        )
    
    def test_team_works(self):
        name = self.statistics.team("PIT")
        self.assertEqual(name[0].name, "Lemieux")
    
    def test_search(self):
        player = self.statistics.search("Lemieux")
        self.assertEqual(player, self.statistics._players[1])

    def test_search_doesnt_exist(self):
        player = self.statistics.search("Pena")
        self.assertEqual(player,None)

    def test_top_scorers(self):
        top_scorer = self.statistics.top_scorers(1)

        self.assertEqual(top_scorer[0].name,"Gretzky")