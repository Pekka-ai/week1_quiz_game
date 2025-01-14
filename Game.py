import json

def load_questions(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)

def ask_questions(questions):
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
    
    print(f"\nPeli päättyi! Sait {score} / {total_questions} oikeaa vastausta.")

# Pääohjelma
def main():
    questions_file = "questions.json" 
    questions = load_questions(questions_file)
    ask_questions(questions)

if __name__ == "__main__":
    main()

