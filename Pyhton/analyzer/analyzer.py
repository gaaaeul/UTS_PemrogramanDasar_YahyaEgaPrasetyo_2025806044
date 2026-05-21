from collections import Counter

def analyze_text(filename):
    with open(filename, "r", encoding="utf-8") as file:
        text = file.read()

    lines = text.splitlines()
    words = text.lower().split()

    vowels = "aiueo"
    vowel_count = 0
    consonant_count = 0

    for char in text.lower():
        if char.isalpha():
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1

    word_count = Counter(words)
    top_words = word_count.most_common(5)

    return {
        "lines": len(lines),
        "words": len(words),
        "top_words": top_words,
        "vowels": vowel_count,
        "consonants": consonant_count
    }