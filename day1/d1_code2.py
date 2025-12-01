"""#Advent Of Code | DAY 1 | Code 2


"""

def calcola_password(nome_file: str) -> int:
    posizione = 50
    password = 0
    with open(nome_file, "r") as f:
        for linea in f:
            linea = linea.strip()
            if not linea:
              continue

            direzione = linea[0]
            valore = int(linea[1:])

            if direzione == 'R':
                # Simulo ogni singolo Click della rotazione
                for i in range(1, valore + 1):           #range(a,b) genera i numeri da a fino a b-1 ma devo includere anche valore quindi faccio +1
                    if (posizione + i) % 100 == 0:
                        password += 1
                posizione = (posizione + valore) % 100

            elif direzione == 'L':
                for i in range(1, valore + 1):
                    if (posizione - i) % 100 == 0:
                        password += 1
                posizione = (posizione - valore) % 100

            else:
                raise ValueError(f"Istruzione non valida: {linea}")
    return password

if __name__ == "__main__":
    risultato = calcola_password("input.txt")
    print("La password è:", risultato)