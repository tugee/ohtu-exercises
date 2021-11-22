class PlayerStats:
    def __init__(self,reader):
        self.reader = reader
    
    def top_scorers_by_nationality(self,nationality):
        players = self.reader.get_players()
        return sorted(list(filter(lambda player : player.nationality == nationality,players)),key= lambda player: player.goals,reverse=True)
