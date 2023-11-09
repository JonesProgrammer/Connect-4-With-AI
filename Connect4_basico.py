import numpy as np

# Definir el tamaño del tablero
ROWS = 6
COLS = 7

# Crear un tablero vacío
def crear_tablero():
    return np.zeros((ROWS, COLS))

# Colocar una ficha en el tablero
def hacer_movimiento(tablero, fila, columna, jugador):
    tablero[fila][columna] = jugador

# Verificar si una columna está llena
def columna_llena(tablero, columna):
    return tablero[0][columna] != 0

# Obtener las columnas disponibles para moverse
def columnas_disponibles(tablero):
    return [c for c in range(COLS) if not columna_llena(tablero, c)]

# Verificar si alguien ganó
def verificar_victoria(tablero, jugador):
    # Comprobar las filas
    for r in range(ROWS):
        for c in range(COLS - 3):
            if tablero[r][c] == jugador and tablero[r][c+1] == jugador and tablero[r][c+2] == jugador and tablero[r][c+3] == jugador:
                return True

    # Comprobar las columnas
    for r in range(ROWS - 3):
        for c in range(COLS):
            if tablero[r][c] == jugador and tablero[r+1][c] == jugador and tablero[r+2][c] == jugador and tablero[r+3][c] == jugador:
                return True

    # Comprobar las diagonales hacia arriba
    for r in range(3, ROWS):
        for c in range(COLS - 3):
            if tablero[r][c] == jugador and tablero[r-1][c+1] == jugador and tablero[r-2][c+2] == jugador and tablero[r-3][c+3] == jugador:
                return True

    # Comprobar las diagonales hacia abajo
    for r in range(3, ROWS):
        for c in range(3, COLS):
            if tablero[r][c] == jugador and tablero[r-1][c-1] == jugador and tablero[r-2][c-2] == jugador and tablero[r-3][c-3] == jugador:
                return True

    return False
