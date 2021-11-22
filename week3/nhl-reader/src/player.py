class Player:
    def __init__(self,name,nationality,assists,goals,penalties,team,games):
        self.name = name
        self.nationality = nationality
        self.assists = assists
        self.goals = goals
        self.penalties = penalties
        self.team = team
        self.games = games
    
    def __str__(self):
        printable = str(self.name) + " team " + str(self.team) + " goals " + str(self.goals) + " assits " + str(self.assists)
        return printable
