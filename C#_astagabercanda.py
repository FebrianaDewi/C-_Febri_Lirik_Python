import os
import time
import sys

lyrics = [
    ("Semua-mua yang aku mau", 1.8),
    ("Ada padamu, kok bisa gitu?", 1.7),
    ("A-aduh, pusing kepala, ci-cinta segitiga", 2.1),
    ("Ku mau-mau aja jadi yang kedua", 2.0),
    ("Eh, astaga, bercanda", 1.4),
    ("Aku tunggu aja jadi yang pertama", 2.9),
    ("Astaga, bercanda", 1.9),
    ("Kalau kau serius, coba sekarang putus, eh!", 1.8),
    ("Aku serius, eh, tapi bercanda", 1.8),
    ("Aku serius, eh, tapi bercanda", 1.8),
    ("A-a-aku serius, eh, tapi bercanda", 1.6),
]

typing_speed = 0.045

os.system("cls" if os.name == "nt" else "clear")

print("=" * 55)
print("           🎵 LIRIK LAGU 🎵")
print("=" * 55)

def ketik(teks, speed=typing_speed):
    """Menampilkan teks dengan efek mengetik."""
    for karakter in teks:
        sys.stdout.write(karakter)
        sys.stdout.flush()
        time.sleep(speed)
    print()

time.sleep(1)

for lyric, delay in lyrics:
    sys.stdout.write("♪ ")
    sys.stdout.flush()
    ketik(lyric)
    time.sleep(delay)
    print()

print("=" * 55)
print("                 SELESAI 🎶")
print("=" * 55)
