from playerReader import PlayerReader
from playerStats import PlayerStats

def main():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)

    players = stats.top_scorers_by_nationality("FIN")
    for player in players:
        print(player)

main()