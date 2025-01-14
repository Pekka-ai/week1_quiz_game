import json

from high_score_board import ScoreBoard

scoreboard = ScoreBoard()
scoreboard.read_file()

def ask_name():
    players=scoreboard.get_players()

    while True:
        name=input("Name: ")
   
        if name not in players:
            scoreboard.add_player(name)
            break
        else:
            print("Nimi on jo käytössä. Yritä uudelleen.")
    return name

def load_questions(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)

def ask_questions(questions, name):
    score = 0
    total_questions = len(questions)
    
    for question_data in questions:
        question = question_data["question"]
        options = question_data["options"]
        correct_answer = question_data["answer"]
        
        # Näytetään kysymys ja vastausvaihtoehdot
        print(f"\n{question}")
        for option in options:
            print(option)
        
        # Pyydetään pelaajan vastaus
        player_answer = input("Vastauksesi (esim. a, b, c, d): ").strip().lower()
        
        # Tarkistetaan vastaus
        if player_answer == correct_answer:
            print("Oikein!")
            score += 1
        else:
            print(f"Väärin! Oikea vastaus on: {correct_answer}.")
    
    scoreboard.save_results(name, score)
    
    print(f"\nPeli päättyi! Sait {score} / {total_questions} oikeaa vastausta.")

# Pääohjelma
def main():
    questions_file = "questions.json" 
    questions = load_questions(questions_file)
    name=ask_name()
    ask_questions(questions, name)
    print("\nTulostaulu:")
    print(scoreboard.get_scoreboard())

if __name__ == "__main__":
    main()

