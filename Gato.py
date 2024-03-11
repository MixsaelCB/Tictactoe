class Gato:
    #inicialice la instancia, y declare los atributos que defines el juego
    def __init__(self,tablero,jugador1,jugador2):
        self._tablero=tablero
        self._jugador1=jugador1
        self._jugador2=jugador2
    #diseño del tablero, si se imprime solo asi no se ve como matriz
    tablero = [
        [" ","|"," ","|"," "],
        ["-","+","-","+","-"],
        [" ","|"," ","|"," "],
        ["-","+","-","+","-"],
        [" ","|"," ","|"," "]
    ]
    #Variables que vamos a ocupar en el codigo
    turno_1=True
    jugador1=""
    jugador2=""
    turno=0
    
    #Esta variable sirve para registrar las posiciones de cada x y o en el tablero y lo muestra con las posiciones que ya fueron ocupadas, 
    #si se elije una psicion que no esta ocupada regresa un 0 lo que quiere decir que esta correcto
    def cambiar_tablero(tablero,posicion,jugador):
        
        if jugador:
            simbolo = "x"
        else:
            simbolo = "o"

        if posicion == 1:
            if tablero[4][0]==" ":
                tablero[4][0] = simbolo
                return 0
            else:
                return "Esa posicion ya esta ocupada"
        elif posicion == 2:
            if tablero[4][2]==" ":
                tablero[4][2] = simbolo
                return 0
            else:
                return "Esa posicion ya esta ocupada"
        elif posicion == 3:
            if tablero[4][4]==" ":
                tablero[4][4] = simbolo
                return 0
            else:
                return "Esa posicion ya esta ocupada"
        elif posicion == 4:
            if tablero[2][0]==" ":
                tablero[2][0] = simbolo
                return 0
            else:
                return "Esa posicion ya esta ocupada"
        elif posicion == 5:
            if tablero[2][2]==" ":
                tablero[2][2] = simbolo
                return 0
            else:
                return "Esa posicion ya esta ocupada"
        elif posicion == 6:
            if tablero[2][4]==" ":
                tablero[2][4] = simbolo
                return 0
            else:
                return "Esa posicion ya esta ocupada"
        elif posicion == 7:
            if tablero[0][0]==" ":
                tablero[0][0] = simbolo
                return 0
            else:
                return "Esa posicion ya esta ocupada"
        elif posicion == 8:
            if tablero[0][2]==" ":
                tablero[0][2] = simbolo
                return 0
            else:
                return "Esa posicion ya esta ocupada"
        elif posicion == 9:
            if tablero[0][4]==" ":
                tablero[0][4] = simbolo
                return 0
            else:
                return "Esa posicion ya esta ocupada"
        else:
            return "Esta posicion no existe"
        
    #esta funcion sirve para que el tablero se vea de 3x3        
    def imprimir_tablero (tablero):
        for fila in tablero:
            for i in range(len(fila)):
                if i == len(fila) - 1:
                    print(fila[i], end="\n")
                else:
                    print(fila[i], end=" ")
    #Esta funcion es para reconocer al ganador
    def ganador(tablero):
        for simbolo in ["x","o"]:
            fila_0 = tablero[0][0] == simbolo and tablero[0][2] == simbolo and tablero[0][4] == simbolo 
            fila_2 = tablero[2][0] == simbolo and tablero[2][2] == simbolo and tablero[2][4] == simbolo
            fila_4 = tablero[4][0] == simbolo and tablero[4][2] == simbolo and tablero[4][4] == simbolo
            columna_0 = tablero[0][0] == simbolo and tablero [2][0] == simbolo and tablero[4][0] == simbolo
            columna_2 = tablero[0][2] == simbolo and tablero [2][2] == simbolo and tablero[4][2] == simbolo
            columna_4 = tablero[0][4] == simbolo and tablero [2][4] == simbolo and tablero[4][4] == simbolo
            diagonal_abajo = tablero[0][0] == simbolo and tablero [2][2] == simbolo and tablero[4][4] == simbolo
            diagonal_arriba = tablero[4][0] == simbolo and tablero[2][2] == simbolo and tablero[0][4] == simbolo 
            #si el simbolo que hay en cada una de las coordenadas de los renglones de arriba es igual se reconoce que hay un ganador
            if fila_0 or fila_2 or fila_4 or columna_0 or columna_2 or columna_4 or diagonal_abajo or diagonal_arriba:
                if simbolo == "x":
                    return 1 #el uno es para el jugador 1
                elif simbolo == "o":
                    return 2 #el dos es para el jugador 2
                break

    imprimir_tablero(tablero)
    #Esta parte va a correr mientras los turnos sean menores a 9
    while turno < 9:
        #Aqui se registra que jugador va a jugar con que simbolo y se va a correr mientras jugador 1 no tenga valor o informacion
        if jugador1 == "":
            print("Nombre de jugador 1 (x)")
            jugador1 = input()
            print("Nombre de jugador 2 (o)")
            jugador2 = input()
        else: #cuando se registra el nombre la parte de arriba ya no corre porque no se cumple la condicion, entonces se pasa a esta
              #por eso a lo largo del juego se va a seguir ejecutando
            if turno_1:
                print(jugador1 + ", elige una posicion")
            else:
                print(jugador2 + ", elige una posicion")

            jugada = int(input())

            valor = cambiar_tablero(tablero, jugada, turno_1)
            if valor == 0: #si el valor es 0 quiere decir que todo se ejecuto bien y se puede cambiar el tabelro
                turno_1 = not turno_1 # esta parte permite que cambie la variable booleana de arriba
                turno += 1
                imprimir_tablero(tablero)
                if ganador (tablero) == 1:
                    print(jugador1 + " gano!")
                    break
                elif ganador (tablero) == 2:
                    print(jugador2 + " gano!")
                    break

            else:
                print(valor)

            if turno == 9:
                print("Empate...")

                

            
            