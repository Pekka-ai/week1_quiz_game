class ScoreBoard:

    def __init__(self):
        self.players = {}

    def add_player(self,name:str):
        self.players[name] = 0

    def get_players(self):
        return list(self.players.keys())
    
    def save_results(self,name:str,score:int):
        self.players[name] = score
        self.update_file()

    def get_scoreboard(self):
        sorted_players = sorted(self.players.items(), key=lambda x: x[1], reverse=True)
        formatted_scoreboard = "\n".join([f"{name}: {score}" for name, score in sorted_players])
        return formatted_scoreboard
    
    def read_file(self):
        with open("high_score.txt", 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()  
                if line:  
                    name, value = line.split(';')  
                    self.players[name] = int(value)

    def update_file(self):
        with open("high_score.txt", 'w', encoding='utf-8') as file:
            for name, score in self.players.items():
                file.write(f"{name};{score}\n")

if __name__ == "__main__":
    scores = ScoreBoard()
    scores.read_file()