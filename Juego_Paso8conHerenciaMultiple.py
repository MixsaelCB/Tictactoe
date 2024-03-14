class Tablero:
    # Inicializa el tablero de juego
    def __init__(self):
        self.tablero = [
            [" ", "|", " ", "|", " "],
            ["-", "+", "-", "+", "-"],
            [" ", "|", " ", "|", " "],
            ["-", "+", "-", "+", "-"],
            [" ", "|", " ", "|", " "]
        ]

    # Método para imprimir el estado actual del tablero.
    def imprimir_tablero(self):
        for fila in self.tablero:
            print(" ".join(fila))

class LogicaJuego:
    # Controla la lógica del juego, como verificar el ganador
    def __init__(self, tablero):
        self.tablero = tablero

    # Verifica si hay un ganador
    def ganador(self):
        lineas_victoria = [
            [(i, j) for j in range(0, 5, 2)] for i in range(0, 5, 2)
        ] + [
            [(i, j) for i in range(0, 5, 2)] for j in range(0, 5, 2)
        ] + [
            [(i, i) for i in range(0, 5, 2)],
            [(i, 4 - i) for i in range(0, 5, 2)]
        ]

        victoria_por_simbolo = {
            simbolo: any(all(self.tablero[fila][columna] == simbolo for fila, columna in linea) for linea in lineas_victoria)
            for simbolo in ["x", "o"]
        }

        if victoria_por_simbolo["x"]:
            return 1
        elif victoria_por_simbolo["o"]:
            return 2
        return None

class Gato(Tablero, LogicaJuego):
    # Constructor de la clase, inicializa el tablero y los nombres de los jugadores.
    def __init__(self):
        Tablero.__init__(self)
        LogicaJuego.__init__(self, self.tablero)
        self.turno_1, self.jugador1, self.jugador2, self.turno = True, "", "", 0

    # Método para modificar el tablero basado en la posición elegida por el jugador.
    def cambiar_tablero(self, posicion, jugador):
        simbolo = "x" if jugador else "o"
        coordenadas = [(i, j) for i in range(0, 5, 2) for j in range(0, 5, 2)]
        fila, columna = coordenadas[posicion - 1]
        if self.tablero[fila][columna] == " ":
            self.tablero[fila][columna] = simbolo
            return 0
        else:
            return "Esa posición ya está ocupada"

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

# Creación e inicialización del juego.
juego = Gato()
juego.iniciar_juego()
