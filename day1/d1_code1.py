"""

#Advent Of Code | DAY 1 | Code 1

"""

def calcola_password(nome_file: str) -> int:
    posizione = 50   # punto di partenza
    password = 0     # contatore delle volte in cui si ferma su 0

    with open(nome_file, "r") as f:
        for linea in f:
            linea = linea.strip()
            if not linea:
                continue  # salta righe vuote

            direzione = linea[0]       # 'R' o 'L'
            valore = int(linea[1:])    # il numero dopo la lettera

            if direzione == 'R':
                posizione = (posizione + valore) % 100
            elif direzione == 'L':
                posizione = (posizione - valore) % 100
            else:
                raise ValueError(f"Istruzione non valida: {linea}")

            if posizione == 0:
                password += 1

    return password

if __name__ == "__main__":
    risultato = calcola_password("input.txt")
    print("La password è:", risultato)