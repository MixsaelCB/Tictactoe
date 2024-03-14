class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def distancia_entre_puntos(punto1, punto2):
    """
    Calcula la distancia entre dos puntos en el plano cartesiano utilizando el teorema de Pitágoras.
    """
    dx = punto2.x - punto1.x
    dy = punto2.y - punto1.y
    distancia = (dx ** 2 + dy ** 2) ** 0.5
    return distancia

# Crear instancias de la clase Punto
punto1 = Punto(1, 2)
punto2 = Punto(4, 6)

# Desempaquetar los atributos de los objetos Punto como argumentos de la función
distancia = distancia_entre_puntos(*[punto1, punto2])

print("La distancia entre los puntos es:", distancia)

#la función distancia_entre_puntos calcula la distancia entre dos puntos en el plano cartesiano. 
#Se define una clase Punto que tiene dos atributos, x e y, que representan las coordenadas del punto. 
#Luego, se crean dos instancias de la clase Punto, punto1 y punto2.
#Cuando llamamos a la función distancia_entre_puntos, pasamos los objetos punto1 y punto2 
#empaquetados en una lista utilizando el operador *, lo que desempaqueta los argumentos dentro de la función.
#Esto nos permite tratar cada punto como un argumento separado dentro de la función, sin necesidad de pasarlos uno por uno.
# La función luego calcula la distancia entre los puntos y devuelve el resultado.