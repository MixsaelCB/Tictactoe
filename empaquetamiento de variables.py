class Coordenadas:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Crear una instancia de Coordenadas y empaquetar las coordenadas en una sola variable
coordenadas = Coordenadas(3, 4)

# Desempaquetar las coordenadas
x, y = coordenadas.x, coordenadas.y

print("Coordenada X:", x)
print("Coordenada Y:", y)

#En este ejemplo, la clase Coordenadas tiene dos atributos x e y, que representan las coordenadas en el plano. 
#Al crear una instancia de Coordenadas con los valores (3, 4), estamos empaquetando dos variables (x e y) en una sola variable coordenadas. 
#Luego, desempaquetamos las coordenadas en las variables x e y para acceder a cada una de ellas por separado.