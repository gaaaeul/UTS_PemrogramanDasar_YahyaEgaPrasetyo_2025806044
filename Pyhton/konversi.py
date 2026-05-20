import csv
import json

data_mahasiswa = []

with open('../C/data_mahasiswa.csv', 'r') as file:

    reader = csv.DictReader(file)

    total = 0
    jumlah = 0

    print("=== DATA MAHASISWA ===")

    for row in reader:

        print(row)

        total += float(row['NilaiAkhir'])
        jumlah += 1

        data_mahasiswa.append({
            "nama": row['Nama'],
            "nim": row['NIM'],
            "nilai_akhir": float(row['NilaiAkhir']),
            "mutu": row['Mutu']
        })

rata_rata = total / jumlah

print("\nRata-rata nilai akhir:", rata_rata)

with open('data_mahasiswa.json', 'w') as json_file:
    json.dump(data_mahasiswa, json_file, indent=4)

print("JSON berhasil dibuat!")