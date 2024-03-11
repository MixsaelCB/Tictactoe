class Gato:
    # Constructor de la clase, inicializa el tablero y los nombres de los jugadores.
    def __init__(self, tablero, jugador1, jugador2):
        self._tablero, self._jugador1, self._jugador2 = tablero, jugador1, jugador2

    # Diseño inicial del tablero, representando un tablero de 3x3 con separadores.
    tablero = [
        [" ", "|", " ", "|", " "],
        ["-", "+", "-", "+", "-"],
        [" ", "|", " ", "|", " "],
        ["-", "+", "-", "+", "-"],
        [" ", "|", " ", "|", " "]
    ]

    # Variables para controlar el estado del juego.
    turno_1, jugador1, jugador2, turno = True, "", "", 0

    # Método para modificar el tablero basado en la posición elegida por el jugador.
    def cambiar_tablero(self, posicion, jugador):
        simbolo = "x" if jugador else "o"
        coordenadas = [
            (4, 0), (4, 2), (4, 4),
            (2, 0), (2, 2), (2, 4),
            (0, 0), (0, 2), (0, 4)
        ]
        fila, columna = coordenadas[posicion - 1]
        if self._tablero[fila][columna] == " ":
            self._tablero[fila][columna] = simbolo
            return 0
        else:
            return "Esa posición ya está ocupada"

    # Método para imprimir el estado actual del tablero.
    def imprimir_tablero(self):
        for fila in self._tablero:
            print(" ".join(fila))

    # Método para determinar si hay un ganador
    def ganador(self):
        # Definición de las líneas de victoria utilizando zip para crear pares de coordenadas.
        lineas_victoria = [
            # Usando zip y asignación múltiple para definir líneas de victoria
            [(i, j) for i, j in zip([0, 0, 0], [0, 2, 4])],  # Filas
            [(i, j) for i, j in zip([2, 2, 2], [0, 2, 4])],
            [(i, j) for i, j in zip([4, 4, 4], [0, 2, 4])],
            [(i, j) for i, j in zip([0, 2, 4], [0, 0, 0])],  # Columnas
            [(i, j) for i, j in zip([0, 2, 4], [2, 2, 2])],
            [(i, j) for i, j in zip([0, 2, 4], [4, 4, 4])],
            [(i, j) for i, j in zip([0, 2, 4], [0, 2, 4])],  # Diagonales
            [(i, j) for i, j in zip([0, 2, 4], [4, 2, 0])]
        ]

        # Comprensión de diccionarios para verificar las condiciones de victoria por símbolo.
        victoria_por_simbolo = {
            simbolo: any(all(self._tablero[fila][columna] == simbolo for fila, columna in linea) for linea in lineas_victoria)
            for simbolo in ["x", "o"]
        }

        if victoria_por_simbolo["x"]:
            return 1  # Jugador 1 gana.
        elif victoria_por_simbolo["o"]:
            return 2  # Jugador 2 gana.
        return None  # Sin ganador aún.

    # Método principal para ejecutar el juego, maneja la lógica del juego y el intercambio de turnos.
    def iniciar_juego(self):
        self.imprimir_tablero()
        while self.turno < 9:
            if self.jugador1 == "":
                self.jugador1, self.jugador2 = input("Nombre de jugador 1 (x): "), input("Nombre de jugador 2 (o): ")
            else:
                jugador_actual = self.jugador1 if self.turno_1 else self.jugador2
                print(f"{jugador_actual}, elige una posición (1-9): ")
                jugada = int(input())

                resultado = self.cambiar_tablero(jugada, self.turno_1)
                if resultado == 0:
                    self.turno_1 = not self.turno_1
                    self.turno += 1
                    self.imprimir_tablero()
                    ganador = self.ganador()
                    if ganador:
                        ganador_nombre = self.jugador1 if ganador == 1 else self.jugador2
                        print(f"{ganador_nombre} ganó!")
                        break
                else:
                    print(resultado)

                if self.turno == 9:
                    print("Empate...")

# Creación e inicialización del juego con un tablero vacío y sin nombres de jugadores.
tablero_inicial = [
    [" ", "|", " ", "|", " "],
    ["-", "+", "-", "+", "-"],
    [" ", "|", " ", "|", " "],
    ["-", "+", "-", "+", "-"],
    [" ", "|", " ", "|", " "]
]
juego = Gato(tablero_inicial, "", "")
juego.iniciar_juego()
