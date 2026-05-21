import random
from colorama import Fore

def play_level(level):
    if level == 1:
        max_num = 10
        attempts = 3
    elif level == 2:
        max_num = 50
        attempts = 5
    else:
        max_num = 100
        attempts = 7

    secret = random.randint(1, max_num)

    print(Fore.CYAN + f"\nLEVEL {level}")
    print(f"Tebak angka 1 - {max_num}")

    for i in range(attempts):
        try:
            guess = int(input(f"Percobaan ke-{i+1}: "))

            if guess == secret:
                print(Fore.GREEN + "BENAR!")
                return (attempts - i) * 10

            elif guess < secret:
                print(Fore.YELLOW + "Terlalu kecil!")

            else:
                print(Fore.YELLOW + "Terlalu besar!")

        except:
            print(Fore.RED + "Input harus angka!")

    print(Fore.RED + f"Gagal! Angka benar: {secret}")
    return 0