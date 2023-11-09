# Implementación del algoritmo Minimax con poda alfa-beta
def minimax(tablero, profundidad, alfa, beta, max_turn, log_file):
    columnas_disp = columnas_disponibles(tablero)
    if profundidad == 0 or len(columnas_disp) == 0:
        return None, evaluar_tablero(tablero)

    if max_turn:
        valor_max = float("-inf")
        mejor_col = None
        for columna in columnas_disp:
            fila = obtener_fila_vacia(tablero, columna)
            nuevo_tablero = tablero.copy()
            hacer_movimiento(nuevo_tablero, fila, columna, 1)
            _, valor = minimax(nuevo_tablero, profundidad - 1, alfa, beta, False, log_file)
            if valor > valor_max:
                valor_max = valor
                mejor_col = columna
            alfa = max(alfa, valor_max)
            if alfa >= beta:
                break
        log_file.write(f"Max (1) elige columna {mejor_col}, valor = {valor_max}\n")
        return mejor_col, valor_max
    else:
        valor_min = float("inf")
        peor_col = None
        for columna in columnas_disp:
            fila = obtener_fila_vacia(tablero, columna)
            nuevo_tablero = tablero.copy()
            hacer_movimiento(nuevo_tablero, fila, columna, 2)
            _, valor = minimax(nuevo_tablero, profundidad - 1, alfa, beta, True, log_file)
            if valor < valor_min:
                valor_min = valor
                peor_col = columna
            beta = min(beta, valor_min)
            if alfa >= beta:
                break
        log_file.write(f"Min (2) elige columna {peor_col}, valor = {valor_min}\n")
        return peor_col, valor_min
