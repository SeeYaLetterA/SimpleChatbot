import json
from difflib import get_close_matches
import random

# Load the knowledge base from the json file

def load_knowledge_base(file_path: str) -> dict:
    with open(file_path, "r") as file:
        data: dict = json.load(file)
    return data

def save_knowledge_base(file_path: str, data: dict):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)


def find_best_match(user_question: str, questions: list[str]) -> str | None:
    matches: list = get_close_matches(user_question, questions, n=1, cutoff=0.5)
    return matches[0] if matches else None

def get_answer_for_question(questions: str, knowledge_base: dict) -> str | None:
    for q in knowledge_base["questions"]:
        if q["question"] == questions:
            return q["answer"]
        

def chatbot():
    knowledge_base: dict = load_knowledge_base('knowledge_base.json')

    while True:
        user_input: str = input("Kamu: ")

        
        if user_input.lower() == "keluar":
            print("Bot: Terima kasih karena sudah memakai saya! :D")
            break
        
        
        best_match: str | None = find_best_match(user_input, [q["question"] for q in knowledge_base["questions"]])

        if best_match:
            answer:  str = get_answer_for_question(best_match, knowledge_base)
            print(f'Bot: {random.choice(answer)}')
        else:
            print("Bot: Saya tidak paham, bisakah kamu memberikan jawabannya?")
            new_answer: str = input('Jawab jawabannya atau ketik "Skip" untuk melewati: ')

            if new_answer.lower() != "skip":
                knowledge_base["questions"].append({"question": user_input, "answer": [new_answer]})
                save_knowledge_base('knowledge_base.json', knowledge_base)
                print('Bot: Terima kasih, saya belajar respons baru!')


if __name__ == '__main__':
    chatbot()