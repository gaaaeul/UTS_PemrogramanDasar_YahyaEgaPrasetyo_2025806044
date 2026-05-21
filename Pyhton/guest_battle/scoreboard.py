import json
import os

FILE_NAME = "scores.json"

def load_scores():
    if not os.path.exists(FILE_NAME):
        return []

    with open(FILE_NAME, "r") as file:
        return json.load(file)

def save_score(name, score):
    scores = load_scores()

    scores.append({
        "nama": name,
        "score": score
    })

    with open(FILE_NAME, "w") as file:
        json.dump(scores, file, indent=4)

def show_top_scores():
    scores = load_scores()

    scores.sort(key=lambda x: x["score"], reverse=True)

    print("\n=== TOP 5 SCORE ===")

    for i, player in enumerate(scores[:5], start=1):
        print(f"{i}. {player['nama']} - {player['score']} pts")