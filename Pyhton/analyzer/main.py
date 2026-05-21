from analyzer import analyze_text

result = analyze_text("input.txt")

with open("report.txt", "w", encoding="utf-8") as file:
    file.write("=== HASIL ANALISIS TEKS ===\n\n")

    file.write(f"Jumlah baris: {result['lines']}\n")
    file.write(f"Jumlah kata: {result['words']}\n")
    file.write(f"Jumlah huruf vokal: {result['vowels']}\n")
    file.write(f"Jumlah huruf konsonan: {result['consonants']}\n\n")

    file.write("5 Kata Terbanyak:\n")

    for word, count in result['top_words']:
        file.write(f"{word}: {count}\n")

    file.write("\nGrafik Frekuensi:\n")

    for word, count in result['top_words']:
        file.write(f"{word} {'#' * count}\n")

print("Analisis selesai!")
print("Hasil disimpan ke report.txt")