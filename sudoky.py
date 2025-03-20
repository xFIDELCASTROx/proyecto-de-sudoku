# proyecto-de-sudoku
# Juego de Sudoku 
def inicializar_tablero():
    n_tablero = {
        (1, 1): 5, (1, 2): 3, (1, 5): 7,
        (2, 1): 6, (2, 4): 1, (2, 5): 9, (2, 6): 5,
        (3, 2): 9, (3, 3): 8, (3, 8): 6,
        (4, 1): 8, (4, 5): 6, (4, 9): 3,
        (5, 1): 4, (5, 4): 8, (5, 6): 3, (5, 9): 1,
        (6, 1): 7, (6, 5): 2, (6, 9): 6,
        (7, 2): 6, (7, 7): 2, (7, 8): 8,
        (8, 4): 4, (8, 5): 1, (8, 6): 9, (8, 9): 5,
        (9, 5): 8, (9, 8): 7, (9, 9): 9
    }
    return n_tablero

def imprimir_tablero(n_tablero, n_pistas):
    for n_fila in range(1, 10):
        for n_columna in range(1, 10):
            n_posicion = (n_fila, n_columna)
            if n_posicion in n_pistas:
                print(f"\033[94m{n_tablero.get(n_posicion, ' ')}\033[0m", end=" ")
            elif n_posicion in n_tablero and not es_valido(n_tablero, n_fila, n_columna, n_tablero[n_posicion]):
                print(f"\033[91m{n_tablero[n_posicion]}\033[0m", end=" ")
            else:
                print(n_tablero.get(n_posicion, ' '), end=" ")
            if n_columna % 3 == 0 and n_columna != 9:
                print("|", end=" ")
        print()
        if n_fila % 3 == 0 and n_fila != 9:
            print("-" * 21)



def es_valido(n_tablero, n_fila, n_columna, n_numero):
    for n_i in range(1, 10):
        if n_tablero.get((n_fila, n_i)) == n_numero or n_tablero.get((n_i, n_columna)) == n_numero:
            return False
    n_cuadrante_fila = (n_fila - 1) // 3
    n_cuadrante_columna = (n_columna - 1) // 3
    for n_i in range(1, 4):
        for n_j in range(1, 4):
            if n_tablero.get((n_cuadrante_fila * 3 + n_i, n_cuadrante_columna * 3 + n_j)) == n_numero:
                return False
    return True



def jugar_sudoku():
    n_tablero = inicializar_tablero()
    n_pistas = set(n_tablero.keys())
    n_resuelto = {
        (1, 1): 5, (1, 2): 3, (1, 3): 4, (1, 4): 6, (1, 5): 7, (1, 6): 8, (1, 7): 9, (1, 8): 1, (1, 9): 2,
        (2, 1): 6, (2, 2): 7, (2, 3): 2, (2, 4): 1, (2, 5): 9, (2, 6): 5, (2, 7): 3, (2, 8): 4, (2, 9): 8,
        (3, 1): 1, (3, 2): 9, (3, 3): 8, (3, 4): 3, (3, 5): 4, (3, 6): 2, (3, 7): 5, (3, 8): 6, (3, 9): 7,
        (4, 1): 8, (4, 2): 5, (4, 3): 9, (4, 4): 7, (4, 5): 6, (4, 6): 1, (4, 7): 4, (4, 8): 2, (4, 9): 3,
        (5, 1): 4, (5, 2): 2, (5, 3): 6, (5, 4): 8, (5, 5): 5, (5, 6): 3, (5, 7): 7, (5, 8): 9, (5, 9): 1,
        (6, 1): 7, (6, 2): 1, (6, 3): 3, (6, 4): 9, (6, 5): 2, (6, 6): 4, (6, 7): 8, (6, 8): 5, (6, 9): 6,
        (7, 1): 9, (7, 2): 6, (7, 3): 1, (7, 4): 5, (7, 5): 3, (7, 6): 7, (7, 7): 2, (7, 8): 8, (7, 9): 4,
        (8, 1): 2, (8, 2): 8, (8, 3): 7, (8, 4): 4, (8, 5): 1, (8, 6): 9, (8, 7): 6, (8, 8): 3, (8, 9): 5,
        (9, 1): 3, (9, 2): 4, (9, 3): 5, (9, 4): 2, (9, 5): 8, (9, 6): 6, (9, 7): 1, (9, 8): 7, (9, 9): 9
    }

    while True:
        imprimir_tablero(n_tablero, n_pistas)
        n_fila = int(input('ingrese la fila (1-9): '))
        n_columna = int(input('ingrese la columna (1-9): '))
        n_posicion = (n_fila, n_columna)

        if n_posicion in n_pistas:
            print('no puedes sobre escribir una pista. intentaas de nuevo.')
            continue

        if n_fila < 1 or n_fila > 9 or n_columna < 1 or n_columna > 9:
            print('posición inválida. intenta de nuevo.')
            continue

        n_numero = int(input('ingrese el número (1-9): '))
        if n_numero < 1 or n_numero > 9:
            print('número inválido. inta de nuevo.')
            continue

        if es_valido(n_tablero, n_fila, n_columna, n_numero):
            n_tablero[n_posicion] = n_numero
        else:
            print('número inválido. intenta de nuevo.')

        if all(n_tablero.get((n_fila, n_columna)) == n_resuelto.get((n_fila, n_columna)) for n_fila in range(1, 10) for n_columna in range(1, 10)):
            print("felicidades has resuelto el sudoku.")
            break

        n_opcion = input('deseas rendirte? (s/n): ')
        if n_opcion.lower() == 's':
            print('tablero resuelto:')
            imprimir_tablero(n_resuelto, n_pistas)
            break  

if __name__ == '__main__':
    jugar_sudoku()
