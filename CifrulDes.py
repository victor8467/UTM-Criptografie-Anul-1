import random
import string

tabel_ip = [
    58, 50, 42, 34, 26, 18, 10, 2,
    60, 52, 44, 36, 28, 20, 12, 4,
    62, 54, 46, 38, 30, 22, 14, 6,
    64, 56, 48, 40, 32, 24, 16, 8,
    57, 49, 41, 33, 25, 17, 9,  1,
    59, 51, 43, 35, 27, 19, 11, 3,
    61, 53, 45, 37, 29, 21, 13, 5,
    63, 55, 47, 39, 31, 23, 15, 7
]


def formateaza_biti(biti: str) -> str:
    grupuri = []
    for i in range(0, len(biti), 8):
        grupuri.append(biti[i:i+8])
    return " ".join(grupuri)


def transforma_in_biti(text: str) -> str:
    rezultat = []
    for char in text:
        cod_binar = f"{ord(char):08b}"
        rezultat.append(cod_binar)
        print(f"{char} == {cod_binar}")
    return "".join(rezultat)


def aplica_ip(biti: str) -> str:
    rezultat = []
    for pozitie in tabel_ip:
        rezultat.append(biti[pozitie - 1])
    return "".join(rezultat)


def afiseaza_tabel_ip():
    for i in range(0, 64, 8):
        print(tabel_ip[i:i+8])


def main():
    while True:
        while True:
            optiune = input("1 - Introducere manuala\n2 - Generare aleatorie\nexit - iesire din program\nAlegeti optiunea: ")
            if optiune != "1" and optiune != "2" and optiune != "exit":
                print("Alege o optiune valida! \n")
                continue
            else:
                break

        if optiune.lower() == "exit":
            exit()
        
        if optiune == "1":
            mesaj = input("Introduceti un mesaj de 8 caractere: ")
            while len(mesaj) != 8:
                mesaj = input("Mesajul trebuie sa aiba exact 8 caractere: ")
        else:
            caractere = string.ascii_letters + string.digits
            mesaj = "".join([random.choice(caractere) for _ in range(8)])
            print(f"Mesajul generat este: {mesaj}")

        print("\nTransformarea caracterelor in biti:")
        biti_mesaj = transforma_in_biti(mesaj)
        print(f"Mesajul in biti este: {formateaza_biti(biti_mesaj)}")

        print("\nTabelul IP utilizat:")
        afiseaza_tabel_ip()

        biti_permutati = aplica_ip(biti_mesaj)
        print(f"\nBlocul dupa permutarea IP: {formateaza_biti(biti_permutati)}")

        L0 = biti_permutati[:32]
        R0 = biti_permutati[32:]
        L1 = R0

        print(f"\nL0 == {formateaza_biti(L0)}")
        print(f"R0 == {formateaza_biti(R0)}")
        print(f"L1 == {formateaza_biti(L1)}")
        print(f"L1 in format hexazecimal == {int(L1, 2):08X} \n")


if __name__ == "__main__":
    main()