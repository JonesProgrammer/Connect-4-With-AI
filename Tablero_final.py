from Connect4_basico import crear_tablero
from Connect4_basico import hacer_movimiento
from Connect4_minimax_poda_alfa-beta import minimax

# Función de utilidad para evaluar el tablero
def evaluar_tablero(tablero):
    if verificar_victoria(tablero, 1):
        return 1
    elif verificar_victoria(tablero, 2):
        return -1
    else:
        return 0


# Función para obtener la fila vacía en una columna
def obtener_fila_vacia(tablero, columna):
    for r in range(ROWS-1, -1, -1):
        if tablero[r][columna] == 0:
            return r

# Función principal para jugar el juego
def jugar_connect4(log_file):
    tablero = crear_tablero()
    turno = 1  # El jugador 1 inicia
    fin_del_juego = False

    while not fin_del_juego:
        imprimir_tablero(tablero)
        if turno == 1:
            print("Turno del Jugador A ")
            columna = int(input("Elije una columna (0-6): "))
        else:
            profundidad = 4  # Profundidad de búsqueda
            print(f"Turno del Jugador B ")

            columna, _ = minimax(tablero, 4, float("-inf"), float("inf"), True, log_file)
            print(f"Jugando en columna {columna}")

        fila = obtener_fila_vacia(tablero, columna)
        hacer_movimiento(tablero, fila, columna, turno)

        if verificar_victoria(tablero, turno):
            imprimir_tablero(tablero)
            if turno == 1:
              print(f"¡El Jugador A gana!")
            else:
              print(f"¡El Jugador B gana!")
            fin_del_juego = True
        elif len(columnas_disponibles(tablero)) == 0:
            imprimir_tablero(tablero)
            print("¡Empate!")
            fin_del_juego = True

        turno = 3 - turno  # Alternar el turno entre 1 y 2

# Función para imprimir el tablero
def imprimir_tablero(tablero):
    for r in range(ROWS):
        for c in range(COLS):
            if tablero[r][c] == 0:
                print(". ", end="")
            elif tablero[r][c] == 1:
                print("X ", end="")
            else:
                print("O ", end="")
        print()
    print()

if __name__ == "__main__":
    with open("connect4_log.txt", "w") as log_file:
        jugar_connect4(log_file)
