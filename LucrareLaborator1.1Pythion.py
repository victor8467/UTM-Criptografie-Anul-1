alfabet = "AĂÂBCDEFGHIÎJKLMNOPQRSȘTȚUVWXYZ"
lungime_alfabet = len(alfabet)

alfabet_mic = "aăâbcdefghiîjklmnopqrsștțuvwxyz"


def cauta_pozitia(c: str) -> int:
    for i in range(lungime_alfabet):
        if alfabet[i] == c:
            return i
        if alfabet_mic[i] == c:
            return i
    return -1


def este_valid_text(text: str) -> bool:
    for char in text:
        if char in [" ", "\t", "\n", "\r"]:
            continue
        if cauta_pozitia(char) == -1:
            return False
    return True


def pregateste_text(text: str) -> str:
    rezultat = []
    for char in text:
        if char in [" ", "\t", "\n", "\r"]:
            continue
        pos = cauta_pozitia(char)
        rezultat.append(alfabet[pos])
    return "".join(rezultat)


def genereaza_alfabet_cheie2(k2: str) -> str:
    k2_curatat = pregateste_text(k2)
    litere_unice = []
    for char in k2_curatat:
        if char not in litere_unice:
            litere_unice.append(char)

    alfabet_derivat = list(litere_unice)
    for char in alfabet:
        if char not in alfabet_derivat:
            alfabet_derivat.append(char)

    return "".join(alfabet_derivat)


def cripteaza_cezar_1_cheie(text: str, cheie: int) -> str:
    rezultat = []
    for char in text:
        pozitie = cauta_pozitia(char)
        pozitie_noua = (pozitie + cheie) % lungime_alfabet
        rezultat.append(alfabet[pozitie_noua])
    return "".join(rezultat)


def decripteaza_cezar_1_cheie(textCriptat: str, cheie: int) -> str:
    rezultatDecriptat = []
    for char in textCriptat:
        pozitie = cauta_pozitia(char)
        pozitie_noua = (pozitie - cheie) % lungime_alfabet
        rezultatDecriptat.append(alfabet[pozitie_noua])
    return "".join(rezultatDecriptat)


def cripteaza_cezar_2_chei(text: str, k1: int, k2: str) -> str:
    alfabet_k2 = genereaza_alfabet_cheie2(k2)
    rezultat = []
    for char in text:
        pos_in_k2 = alfabet_k2.index(char)
        pos_noua = (pos_in_k2 + k1) % lungime_alfabet
        rezultat.append(alfabet_k2[pos_noua])
    return "".join(rezultat)


def decripteaza_cezar_2_chei(textCriptat: str, k1: int, k2: str) -> str:
    alfabet_k2 = genereaza_alfabet_cheie2(k2)
    rezultatDecriptat = []
    for char in textCriptat:
        pos_in_k2 = alfabet_k2.index(char)
        pos_noua = (pos_in_k2 - k1) % lungime_alfabet
        rezultatDecriptat.append(alfabet_k2[pos_noua])
    return "".join(rezultatDecriptat)


def citeste_mod_algoritm() -> str:
    while True:
        mod = input("Alegeti algoritmul (1 Cezar cu 1 cheie, 2 Cezar cu 2 chei): ")
        if mod == "1" or mod == "2":
            return mod
        print("Optiune invalida! Introduceti 1 sau 2.")


def citeste_optiune() -> str:
    while True:
        Cd = input("Vrei sa criptezi sau sa decriptezi (Criptare/Decriptare): ")
        opt = Cd.upper()
        if opt == "CRIPTARE" or opt == "DECRIPTARE":
            return opt
        print("Optiune invalida! Introduceti Criptare sau Decriptare.")


def citeste_cheie1() -> int:
    while True:
        try:
            cheie = int(input(f"Introduceti cheia (numar intre 1 si {lungime_alfabet - 1}): ") )
            if 1 <= cheie <= lungime_alfabet - 1:
                return cheie
            else:
                print(f"Valoare incorecta! Cheia trebuie sa fie intre 1 si {lungime_alfabet - 1}.")
        except ValueError:
            print( f"Valoare incorecta! Introduceti un numar intreg intre 1 si {lungime_alfabet - 1}." )


def citeste_cheie2() -> str:
    while True:
        k2 = input("Introduceti cheia 2 (text, minim 7 caractere): ")
        if len(k2) < 7:
            print("Cheia 2 invalida! Lungimea trebuie sa fie de cel putin 7 caractere.")
            continue
        if not este_valid_text(k2):
            print("Cheia 2 invalida! Folositi doar litere din alfabetul roman.")
            continue
        return k2


def citeste_text(prompter: str) -> str:
    while True:
        raw_text = input(prompter)
        if raw_text and este_valid_text(raw_text):
            text_curat = pregateste_text(raw_text)
            if len(text_curat) > 0:
                return text_curat
        print("Text invalid! Se permit doar litere din alfabetul roman (A-Z, a-z, ă, â, î, ș, ț).")


def main():
    mod = citeste_mod_algoritm()
    optiune = citeste_optiune()

    if mod == "1":
        k1 = citeste_cheie1()
        if optiune == "CRIPTARE":
            text_curatat = citeste_text("Introduceti un text care sa fie criptat: ")
            text_criptat = cripteaza_cezar_1_cheie(text_curatat, k1)
            print(f"Textul criptat este: {text_criptat}")
        else:
            text_curatat = citeste_text("Introduceti textul ca sa fie decriptat: ")
            text_decriptat = decripteaza_cezar_1_cheie(text_curatat, k1)
            print(f"Textul decriptat este: {text_decriptat}")
    else:
        k1 = citeste_cheie1()
        k2 = citeste_cheie2()
        if optiune == "CRIPTARE":
            text_curatat = citeste_text("Introduceti un text care sa fie criptat: ")
            text_criptat = cripteaza_cezar_2_chei(text_curatat, k1, k2)
            print(f"Textul criptat este: {text_criptat}")
        else:
            text_curatat = citeste_text("Introduceti textul ca sa fie decriptat: ")
            text_decriptat = decripteaza_cezar_2_chei(text_curatat, k1, k2)
            print(f"Textul decriptat este: {text_decriptat}")


if __name__ == "__main__":
    main()
