import random
import string

def generate_random_strings(count=100, length=7, filename="nickler.txt", include_digits=True):
    with open(filename, "w") as file:
        for _ in range(count):
            if include_digits:

                nick = ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))
            else:

                nick = ''.join(random.choices(string.ascii_lowercase, k=length))
            file.write(nick + "\n")
    print(f"{count} adet rastgele {length} karakterli nick {filename} dosyasına kaydedildi.")
    input("Çıkmak için Enter'a bas...")

if __name__ == "__main__":
    while True:
        try:

            count = int(input("Kaç tane nick oluşturmak istiyorsun? "))
            length = int(input("Kaç karakterli olsun? "))
            if length <= 0:
                print("Karakter uzunluğu 1 veya daha büyük olmalı!")
                continue


            print("1 - Sadece harflerden oluşsun")
            print("2 - Harf ve rakam karışık olsun")
            choice = input("Hangi tür nick oluşturmak istiyorsun (1 veya 2)? ")

            if choice not in ["1", "2"]:
                print("Geçersiz seçim! Lütfen 1 veya 2 gir.")
                continue

            include_digits = choice == "2"
            break
        except ValueError:
            print("Lütfen geçerli bir sayı gir!")

    generate_random_strings(count, length, include_digits=include_digits)
