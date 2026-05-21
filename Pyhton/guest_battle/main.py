from game import play_level
from scoreboard import save_score, show_top_scores
from colorama import init

init(autoreset=True)

print("=== GUESS BATTLE ===")

name = input("Masukkan nama pemain: ")

total_score = 0

for level in range(1, 4):
    score = play_level(level)
    total_score += score

print(f"\nTotal Score {name}: {total_score}")

save_score(name, total_score)

show_top_scores()