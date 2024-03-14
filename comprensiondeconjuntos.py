class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
#Aquí se asignan los valores de los parámetros titulo y autor a los atributos correspondientes de la instancia de Libro.
    def __repr__(self):
        return f"Libro('{self.titulo}', '{self.autor}')"

class Biblioteca:
    def __init__(self):
        self.libros = set()

    def agregar_libro(self, libro):
        self.libros.add(libro)

    def buscar_libros_por_autor(self, autor):
        return {libro for libro in self.libros if libro.autor == autor}

# Uso del código
libro1 = Libro("Cien años de soledad", "Gabriel García Márquez")
libro2 = Libro("Don Quijote de la Mancha", "Miguel de Cervantes")
libro3 = Libro("El amor en los tiempos del cólera", "Gabriel García Márquez")

biblioteca = Biblioteca()
biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)
biblioteca.agregar_libro(libro3)

libros_de_gabo = biblioteca.buscar_libros_por_autor("Gabriel García Márquez")
print(libros_de_gabo)  # Output: {Libro('Cien años de soledad', 'Gabriel García Márquez'), Libro('El amor en los tiempos del cólera', 'Gabriel García Márquez')}

#En este ejemplo, Libro es una clase que representa un libro con propiedades como título y autor.
# Biblioteca es otra clase que contiene una colección de libros representada como un conjunto (set).
# La función buscar_libros_por_autor utiliza comprensión de conjuntos para encontrar todos los libros de un autor dado en la biblioteca.