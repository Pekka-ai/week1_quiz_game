class ScoreBoard:

    def __init__(self,players:dict):
        self.players = players

    def add_player(self,name:str):
        self.players[name] =0

    def get_players(self):
        return self.players.keys()
    
    def save_results(self,name:str,score:int):
        self.players[name] = score

    def get_scoreboard(self):
        sorted_players = sorted(self.players.items(), key=lambda x: x[1], reverse=True)
        formatted_scoreboard = "\n".join([f"{name}: {score}" for name, score in sorted_players])
        return formatted_scoreboard