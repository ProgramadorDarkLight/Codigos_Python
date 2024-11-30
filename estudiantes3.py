import os  # Importa el módulo os para operaciones relacionadas con el sistema de archivos.

# Definición de la clase Estudiante
class Estudiante:

    def __init__(self, nombre, edad, carrera):

        self.nombre = nombre  # Almacena el nombre del estudiante.
        self.edad = edad      # Almacena la edad del estudiante.
        self.carrera = carrera  # Almacena la carrera del estudiante.

    def __str__(self):

        return f"Estudiante(nombre: {self.nombre}, edad: {self.edad}, carrera: {self.carrera})"

# Definición de la clase ListaDeEstudiantes
class ListaDeEstudiantes:
    def __init__(self):

        self.estudiantes = []  # Lista donde se guardarán los estudiantes.

    def agregar_estudiante(self, estudiante):

        self.estudiantes.append(estudiante)  # Agrega el estudiante a la lista.

    def mostrar_estudiantes(self):
        """
        Muestra la lista de estudiantes en la consola.
        """
        if not self.estudiantes:  # Verifica si la lista está vacía.
            print("No hay estudiantes en la lista.")
        else:
            for estudiante in self.estudiantes:  # Itera sobre los estudiantes.
                print(estudiante)

    def guardar_estudiantes(self, archivo):
        """
        Guarda la lista de estudiantes en un archivo de texto.

        Args:
            archivo (str): Nombre del archivo donde se guardarán los datos.
        """
        with open(archivo, 'w') as file:  # Abre el archivo en modo escritura.
            for estudiante in self.estudiantes:
                # Escribe los atributos de cada estudiante separados por comas.
                file.write(f"{estudiante.nombre},{estudiante.edad},{estudiante.carrera}\n")

    def cargar_estudiantes(self, archivo):
        """
        Carga la lista de estudiantes desde un archivo de texto.

        Args:
            archivo (str): Nombre del archivo desde el cual se cargarán los datos.
        """
        if os.path.exists(archivo):  # Verifica si el archivo existe.
            with open(archivo, 'r') as file:  # Abre el archivo en modo lectura.
                for linea in file:
                    # Divide cada línea en nombre, edad y carrera.
                    nombre, edad, carrera = linea.strip().split(',')
                    # Crea un nuevo objeto Estudiante con los datos y lo agrega a la lista.
                    estudiante = Estudiante(nombre, int(edad), carrera)
                    self.estudiantes.append(estudiante)


# Función principal para interactuar con el usuario.
def main():

    lista = ListaDeEstudiantes()  # Crea una instancia de ListaDeEstudiantes.
    lista.cargar_estudiantes('estudiantes.txt')  # Carga estudiantes desde un archivo si existe.

    while True:
        # Menú interactivo para gestionar la lista de estudiantes.
        print("\n--- Menú de Estudiantes ---")
        print("1. Ver estudiantes")
        print("2. Agregar estudiante")
        print("3. Guardar y salir")
        opcion = input("Elige una opción: ")  # Solicita al usuario una opción.

        if opcion == '1':  # Opción para mostrar estudiantes.

            lista.mostrar_estudiantes()

        elif opcion == '2':  # Opción para agregar un nuevo estudiante.

            nombre = input("Nombre del estudiante: ")  # Solicita el nombre.
            edad = int(input("Edad del estudiante: "))  # Solicita la edad.
            carrera = input("Carrera del estudiante: ")  # Solicita la carrera.
            estudiante = Estudiante(nombre, edad, carrera)  # Crea un objeto Estudiante.
            lista.agregar_estudiante(estudiante)  # Agrega el estudiante a la lista.

        elif opcion == '3':  # Opción para guardar estudiantes y salir.
            lista.guardar_estudiantes('estudiantes.txt')  # Guarda los datos en un archivo.
            print("Estudiantes guardados. ¡Adiós!")
            break  # Termina el bucle.

        else:  # Manejo de opciones inválidas.
            print("Opción no válida, por favor intenta de nuevo.")

# Ejecuta la función principal si este archivo es ejecutado directamente.
if __name__ == "__main__":
    main()
