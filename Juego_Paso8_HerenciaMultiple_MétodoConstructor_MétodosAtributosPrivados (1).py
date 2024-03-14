class Tablero:
    def __init__(self):
        self._tablero = [
            [" ", "|", " ", "|", " "],
            ["-", "+", "-", "+", "-"],
            [" ", "|", " ", "|", " "],
            ["-", "+", "-", "+", "-"],
            [" ", "|", " ", "|", " "]
        ]

    def imprimir_tablero(self):
        for fila in self._tablero:
            print(" ".join(fila))

class LogicaJuego:
    def __init__(self, tablero):
        self._tablero = tablero

    def _ganador(self):
        lineas_victoria = [
            [(i, j) for j in range(0, 5, 2)] for i in range(0, 5, 2)
        ] + [
            [(i, j) for i in range(0, 5, 2)] for j in range(0, 5, 2)
        ] + [
            [(i, i) for i in range(0, 5, 2)],
            [(i, 4 - i) for i in range(0, 5, 2)]
        ]

        victoria_por_simbolo = {
            simbolo: any(all(self._tablero[fila][columna] == simbolo for fila, columna in linea) for linea in lineas_victoria)
            for simbolo in ["x", "o"]
        }

        if victoria_por_simbolo["x"]:
            return 1
        elif victoria_por_simbolo["o"]:
            return 2
        return None

class Gato(Tablero, LogicaJuego):
    def __init__(self):
        super().__init__()
        self._turno_1 = True
        self._jugador1 = ""
        self._jugador2 = ""
        self._turno = 0
        LogicaJuego.__init__(self, self._tablero)

    def _cambiar_tablero(self, posicion, jugador):
        simbolo = "x" if jugador else "o"
        coordenadas = [(i, j) for i in range(0, 5, 2) for j in range(0, 5, 2)]
        fila, columna = coordenadas[posicion - 1]
        if self._tablero[fila][columna] == " ":
            self._tablero[fila][columna] = simbolo
            return 0
        else:
            return "Esa posición ya está ocupada"

    def iniciar_juego(self):
        self.imprimir_tablero()
        while self._turno < 9:
            if self._jugador1 == "":
                self._jugador1, self._jugador2 = input("Nombre de jugador 1 (x): "), input("Nombre de jugador 2 (o): ")
            else:
                jugador_actual = self._jugador1 if self._turno_1 else self._jugador2
                print(f"{jugador_actual}, elige una posición (1-9): ")
                jugada = int(input())

                resultado = self._cambiar_tablero(jugada, self._turno_1)
                if resultado == 0:
                    self._turno_1 = not self._turno_1
                    self._turno += 1
                    self.imprimir_tablero()
                    ganador = self._ganador()
                    if ganador:
                        ganador_nombre = self._jugador1 if ganador == 1 else self._jugador2
                        print(f"{ganador_nombre} ganó!")
                        break
                else:
                    print(resultado)

                if self._turno == 9:
                    print("Empate...")

juego = Gato()
juego.iniciar_juego()
