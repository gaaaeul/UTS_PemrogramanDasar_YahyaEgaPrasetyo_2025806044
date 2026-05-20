#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct Mahasiswa {
    char nama[50];
    char nim[20];
    float tugas, uts, uas;
    float akhir;
    char mutu;
    struct Mahasiswa *next;
};

struct Mahasiswa *head = NULL;

int main() {

    int pilihan;

    do {

        printf("\n=== MENU DATA MAHASISWA ===\n");
        printf("1. Tambah Data\n");
        printf("2. Tampilkan Data\n");
        printf("3. Simpan CSV\n");
        printf("4. Keluar\n");
        printf("Pilih: ");
        scanf("%d", &pilihan);

        switch(pilihan) {

            case 1: {

                struct Mahasiswa *baru;
                baru = (struct Mahasiswa*) malloc(sizeof(struct Mahasiswa));

                printf("Nama : ");
                scanf("%s", baru->nama);

                printf("NIM : ");
                scanf("%s", baru->nim);

                printf("Tugas : ");
                scanf("%f", &baru->tugas);

                printf("UTS : ");
                scanf("%f", &baru->uts);

                printf("UAS : ");
                scanf("%f", &baru->uas);

                baru->akhir =
                    (0.3 * baru->tugas) +
                    (0.3 * baru->uts) +
                    (0.4 * baru->uas);

                if(baru->akhir >= 80)
                    baru->mutu = 'A';
                else if(baru->akhir >= 70)
                    baru->mutu = 'B';
                else if(baru->akhir >= 60)
                    baru->mutu = 'C';
                else if(baru->akhir >= 50)
                    baru->mutu = 'D';
                else
                    baru->mutu = 'E';

                baru->next = NULL;

                if(head == NULL) {
                    head = baru;
                } else {

                    struct Mahasiswa *temp = head;

                    while(temp->next != NULL) {
                        temp = temp->next;
                    }

                    temp->next = baru;
                }

                printf("Data berhasil ditambahkan!\n");

                break;
            }

            case 2: {

                struct Mahasiswa *temp = head;

                printf("\n=== DATA MAHASISWA ===\n");

                while(temp != NULL) {

                    printf("Nama  : %s\n", temp->nama);
                    printf("NIM   : %s\n", temp->nim);
                    printf("Nilai : %.2f\n", temp->akhir);
                    printf("Mutu  : %c\n", temp->mutu);
                    printf("-------------------\n");

                    temp = temp->next;
                }

                break;
            }

            
                case 3: {

    FILE *fp;

    fp = fopen("data_mahasiswa.csv", "w");

    fprintf(fp, "Nama,NIM,Tugas,UTS,UAS,NilaiAkhir,Mutu\n");

    struct Mahasiswa *temp = head;

    while(temp != NULL) {

        fprintf(fp, "%s,%s,%.2f,%.2f,%.2f,%.2f,%c\n",
            temp->nama,
            temp->nim,
            temp->tugas,
            temp->uts,
            temp->uas,
            temp->akhir,
            temp->mutu);

        temp = temp->next;
    }

    fclose(fp);

    printf("Data berhasil disimpan ke CSV!\n");

    break;
}
            case 4:
                printf("keluar dari program\n");
                break;
                
            default:
                printf("Pilihan tidak valid\n");
        }

    } while(pilihan != 4);

    return 0;
}