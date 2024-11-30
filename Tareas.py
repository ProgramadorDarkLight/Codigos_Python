# Importamos las librerías necesarias
import os  # Para funciones del sistema operativo

# Definimos una clase para representar una tarea
class Tarea:

    def __init__(self, descripcion):
        """Inicializa una tarea con una descripción."""
        self.descripcion = descripcion
        self.completada = False

    def marcar_completada(self):
        """Marca la tarea como completada."""
        self.completada = True

    def __str__(self):

        """Devuelve una representación en cadena de la tarea."""
        estado = "Completada" if self.completada else "Pendiente"
        
        return f"{self.descripcion} - {estado}"

# Definimos una clase para gestionar la lista de tareas
class ListaDeTareas:


    def __init__(self):
        """Inicializa una lista vacía de tareas."""
        self.tareas = []

    def agregar_tarea(self, descripcion):
        """Agrega una nueva tarea a la lista."""
        tarea = Tarea(descripcion)

        self.tareas.append(tarea)

    def eliminar_tarea(self, indice):
        """Elimina una tarea de la lista por su índice."""

        if 0 <= indice < len(self.tareas):

            del self.tareas[indice]

    def ver_tareas(self):
        """Imprime todas las tareas en la lista."""

        if not self.tareas:

            print("No hay tareas en la lista.")

        else:

            for i, tarea in enumerate(self.tareas):

                print(f"{i}. {tarea}")

    def guardar_tareas(self, archivo):
        """Guarda la lista de tareas en un archivo."""
        with open(archivo, 'w') as file:
            for tarea in self.tareas:
                file.write(f"{tarea.descripcion},{tarea.completada}\n")

    def cargar_tareas(self, archivo):
        """Carga la lista de tareas desde un archivo."""
        if os.path.exists(archivo):
            with open(archivo, 'r') as file:
                for linea in file:
                    descripcion, completada = linea.strip().split(',')
                    tarea = Tarea(descripcion)
                    if completada == 'True':
                        tarea.marcar_completada()
                    self.tareas.append(tarea)

# Función principal para interactuar con el usuario
def main():

    lista = ListaDeTareas()

    lista.cargar_tareas('tareas.txt')  # Carga las tareas desde un archivo si existe

    while True:
        print("\n--- Menú de Tareas ---")
        print("1. Ver tareas")
        print("2. Agregar tarea")
        print("3. Eliminar tarea")
        print("4. Marcar tarea como completada")
        print("5. Guardar y salir")
        opcion = input("Elige una opción: ")

        if opcion == '1':
            lista.ver_tareas()

        elif opcion == '2':
            descripcion = input("Descripción de la tarea: ")
            lista.agregar_tarea(descripcion)

        elif opcion == '3':
            indice = int(input("Índice de la tarea a eliminar: "))
            lista.eliminar_tarea(indice)

        elif opcion == '4':

            indice = int(input("Índice de la tarea a completar: "))

            if 0 <= indice < len(lista.tareas):

                lista.tareas[indice].marcar_completada()
         

        elif opcion == '5':
            lista.guardar_tareas('tareas.txt')
            print("Tareas guardadas. ¡Adiós!")
            break

        else:
            print("Opción no válida, intenta de nuevo.")

# Ejecuta la función principal si este archivo es ejecutado como el script principal
if __name__ == "__main__":
    main()
