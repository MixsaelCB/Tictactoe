import openai

class Gato:
    def __init__(self, tablero, jugador1, jugador2):
        self._tablero = tablero
        self._jugador1 = jugador1
        self._jugador2 = jugador2
        self.turno_1 = True
        self.turno = 0
        openai.api_key = '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'

    tablero = [
        [" ", "|", " ", "|", " "],
        ["-", "+", "-", "+", "-"],
        [" ", "|", " ", "|", " "],
        ["-", "+", "-", "+", "-"],
        [" ", "|", " ", "|", " "]
    ]

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

    def imprimir_tablero(self):
        for fila in self._tablero:
            print(" ".join(fila))

    def ganador(self):
        lineas_victoria = [
            [(i, j) for i, j in zip([0, 0, 0], [0, 2, 4])],
            [(i, j) for i, j in zip([2, 2, 2], [0, 2, 4])],
            [(i, j) for i, j in zip([4, 4, 4], [0, 2, 4])],
            [(i, j) for i, j in zip([0, 2, 4], [0, 0, 0])],
            [(i, j) for i, j in zip([0, 2, 4], [2, 2, 2])],
            [(i, j) for i, j in zip([0, 2, 4], [4, 4, 4])],
            [(i, j) for i, j in zip([0, 2, 4], [0, 2, 4])],
            [(i, j) for i, j in zip([0, 2, 4], [4, 2, 0])]
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

    def iniciar_juego(self):
        self.imprimir_tablero()
        while self.turno < 9:
            if self._jugador1 == "":
                self._jugador1, self._jugador2 = input("Nombre de jugador 1 (x): "), input("Nombre de jugador 2 (o): ")
            else:
                jugador_actual = self._jugador1 if self.turno_1 else self._jugador2
                print(f"{jugador_actual}, elige una posición (1-9): ")
                jugada = int(input())

                resultado = self.cambiar_tablero(jugada, self.turno_1)
                if resultado == 0:
                    self.turno_1 = not self.turno_1
                    self.turno += 1
                    self.imprimir_tablero()
                    ganador = self.ganador()
                    if ganador:
                        ganador_nombre = self._jugador1 if ganador == 1 else self._jugador2
                        perdedor_nombre = self._jugador2 if ganador == 1 else self._jugador1
                        messages = [
                            {
                                "role": "user",
                                "content": f"Genera un mensaje motivacional de no más de 50 caracteres felicitando a un jugador llamado {ganador_nombre} que acaba de ganar una partida de Gato, y ánima a {perdedor_nombre} a seguir intentándolo"
                            }
                        ]
                        response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
                        reply = response.choices[0].message.content
                        print(reply)
                        break

if __name__ == "__main__":
    # Inicia el juego.
    juego = Gato(tablero=Gato.tablero, jugador1="", jugador2="")
    juego.iniciar_juego()
