import random
import os

# Funcție pentru a citi întrebările și răspunsurile dintr-un fișier
def citeste_intrebari_din_fisier(nume_fisier):
    intrebari = []
    with open(nume_fisier, 'r', encoding='utf-8') as f:
        intrebare_curenta = None
        raspuns_corect = None
        optiuni = []

        for linie in f:
            linie = linie.strip()
            if linie.startswith("#Q"):  # Detectează începutul unei întrebări
                if intrebare_curenta:
                    # Adaugă întrebarea și răspunsul corect în lista finală
                    intrebari.append((intrebare_curenta, raspuns_corect, optiuni))
                intrebare_curenta = linie[3:].strip()  # Elimină prefixul "#Q "
                raspuns_corect = None
                optiuni = []
            elif linie.startswith("^"):  # Detectează răspunsul corect
                raspuns_corect = linie[1:].strip()
            elif linie.startswith("A") or linie.startswith("B") or linie.startswith("C") or linie.startswith("D"):  # Detectează opțiunile de răspuns
                optiuni.append(linie.strip())

        # Adaugă ultima întrebare dacă există
        if intrebare_curenta:
            intrebari.append((intrebare_curenta, raspuns_corect, optiuni))

    return intrebari


# Funcție pentru a rula jocul de trivia
def joc_trivia():
    categorii = {
        "1": ("istorie", "history.txt"),
        "2": ("geografie", "geography.txt"),
        "3": ("jocuri video", "video-games.txt")
    }

    print("Bine ai venit la jocul de Trivia!")
    print("Alege o categorie:")
    print("1. Istorie")
    print("2. Geografie")
    print("3. Jocuri Video")

    categorie_aleasa = input("Introduceți numărul categoriei dorite: ")

    if categorie_aleasa not in categorii:
        print("Categorie invalidă!")
        return

    nume_categorie, fisier_categorie = categorii[categorie_aleasa]

    fisier = os.path.join(os.path.dirname(__file__), fisier_categorie)
    intrebari = citeste_intrebari_din_fisier(fisier)

    scor = 0
    for i in range(10):
        intrebare, raspuns_corect, optiuni = random.choice(intrebari)
        print(f"\nÎntrebarea {i + 1}: {intrebare}")
        for optiune in optiuni:
            print(optiune)

        raspuns_utilizator = input("Răspunsul tău (A, B, C, D): ").strip().upper()

        # Determină litera răspunsului corect
        litera_raspuns_corect = None
        for optiune in optiuni:
            if optiune[2:].strip().lower() == raspuns_corect.lower():
                litera_raspuns_corect = optiune[0].upper()

        # Verifică dacă răspunsul utilizatorului este corect
        if raspuns_utilizator == litera_raspuns_corect:
            print("Corect!")
            scor += 1
        else:
            print(f"Greșit! Răspunsul corect era: {litera_raspuns_corect}")

    print(f"\nJoc terminat! Ai răspuns corect la {scor} din 10 întrebări.")


# Rulăm jocul
if __name__ == "__main__":
    joc_trivia()








