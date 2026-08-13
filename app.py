import random


def game_tebak_angka():
    print("=======================================")
    print("   GAME TEBAK ANGKA (1 - 100)          ")
    print("=======================================")

    # Komputer memilih angka acak antara 1 sampai 100
    angka_rahasia = random.randint(1, 100)
    kesempatan = 7
    percobaan = 0

    print(
        f"Saya sudah memilih angka antara 1-100. Kamu punya {kesempatan} kesempatan.\n"
    )

    while kesempatan > 0:
        try:
            tebakan = int(input(f"Sisa nyawa [{kesempatan}] - Masukkan tebakanmu: "))
        except ValueError:
            print("❌ Harap masukkan ANGKA saja!\n")
            continue

        percobaan += 1

        if tebakan == angka_rahasia:
            print(
                f"\n🎉 SELAMAT! Kamu berhasil menebak angka {angka_rahasia} dalam {percobaan} kali coba!"
            )
            break
        elif tebakan < angka_rahasia:
            print("💡 Terlalu KECIL! Coba angka yang lebih besar.\n")
        else:
            print("💡 Terlalu BESAR! Coba angka yang lebih kecil.\n")

        kesempatan -= 1

    if kesempatan == 0:
        print(f"\n👻 GAME OVER! Angka yang benar adalah: {angka_rahasia}")


# Jalankan game
if __name__ == "__main__":
    game_tebak_angka()
