import os

# Definición de la clase Estudiante
class Estudiante:

    def __init__(self, nombre, edad, carrera):
        """
        Inicializa una nueva instancia de la clase Estudiante.

        Args:
            nombre (str): Nombre del estudiante.
            edad (int): Edad del estudiante.
            carrera (str): Carrera del estudiante.
        """
        self.nombre = nombre
        self.edad = edad
        self.carrera = carrera

    def __str__(self):
        """
        Devuelve una representación en cadena del objeto Estudiante.

        Returns:
            str: Una representación legible del objeto Estudiante.
        """
        return f"Estudiante(nombre: {self.nombre}, edad: {self.edad}, carrera: {self.carrera})"

# Definición de la clase ListaDeEstudiantes
class ListaDeEstudiantes:
    def __init__(self):
        """Inicializa una lista vacía de estudiantes."""
        self.estudiantes = []

    def agregar_estudiante(self, estudiante):
        """
        Agrega un nuevo estudiante a la lista.

        Args:
            estudiante (Estudiante): Un objeto de la clase Estudiante.
        """
        self.estudiantes.append(estudiante)

    def mostrar_estudiantes(self):
        """Imprime todos los estudiantes en la lista."""
        if not self.estudiantes:
            print("No hay estudiantes en la lista.")
        else:
            for estudiante in self.estudiantes:
                print(estudiante)

    def guardar_estudiantes(self, archivo):
        """
        Guarda la lista de estudiantes en un archivo.

        Args:
            archivo (str): Nombre del archivo donde se guardarán los datos.
        """
        with open(archivo, 'w') as file:
            for estudiante in self.estudiantes:
                file.write(f"{estudiante.nombre},{estudiante.edad},{estudiante.carrera}\n")

    def cargar_estudiantes(self, archivo):
        """
        Carga la lista de estudiantes desde un archivo.

        Args:
            archivo (str): Nombre del archivo desde el cual se cargarán los datos.
        """
        if os.path.exists(archivo):
            with open(archivo, 'r') as file:
                for linea in file:
                    nombre, edad, carrera = linea.strip().split(',')
                    estudiante = Estudiante(nombre, int(edad), carrera)
                    self.estudiantes.append(estudiante)

# Función principal para interactuar con el usuario
def main():
    lista = ListaDeEstudiantes()
    lista.cargar_estudiantes('estudiantes.txt')  # Carga estudiantes desde un archivo, si existe

    while True:
        print("\n--- Menú de Estudiantes ---")
        print("1. Ver estudiantes")
        print("2. Agregar estudiante")
        print("3. Guardar y salir")
        opcion = input("Elige una opción: ")

        if opcion == '1':
            lista.mostrar_estudiantes()
        elif opcion == '2':
            nombre = input("Nombre del estudiante: ")
            edad = int(input("Edad del estudiante: "))
            carrera = input("Carrera del estudiante: ")
            estudiante = Estudiante(nombre, edad, carrera)
            lista.agregar_estudiante(estudiante)
        elif opcion == '3':
            lista.guardar_estudiantes('estudiantes.txt')
            print("Estudiantes guardados. ¡Adiós!")
            break
        else:
            print("Opción no válida, por favor intenta de nuevo.")

# Ejecuta la función principal si este archivo es ejecutado como script principal
if __name__ == "__main__":
    main()
