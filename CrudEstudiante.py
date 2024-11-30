class Estudiante:
    def __init__(self, id, nombre, edad, carrera):
        self.id = id
        self.nombre = nombre
        self.edad = edad
        self.carrera = carrera

    def __str__(self):
        return f"Estudiante(id: {self.id}, nombre: {self.nombre}, edad: {self.edad}, carrera: {self.carrera})"

class CRUDMemoria:

    def __init__(self):
    
        self.estudiantes = []
        self.id_counter = 1

    def crear_estudiante(self, nombre, edad, carrera):
        estudiante = Estudiante(self.id_counter, nombre, edad, carrera)
        self.estudiantes.append(estudiante)
        self.id_counter += 1

    def leer_estudiantes(self):
        return self.estudiantes

    def actualizar_estudiante(self, id, nombre, edad, carrera):
        
        for estudiante in self.estudiantes:
            
            if estudiante.id == id:

                estudiante.nombre = nombre
                estudiante.edad = edad
                estudiante.carrera = carrera

                return True
            
        return False

    def borrar_estudiante(self, id):
        for estudiante in self.estudiantes:
            if estudiante.id == id:
                self.estudiantes.remove(estudiante)
                return True
        return False

# Ejemplos de uso
crud = CRUDMemoria()

crud.crear_estudiante("Carlos", 22, "Ingeniería")

crud.crear_estudiante("Ana", 23, "Derecho")


print("Estudiantes después de la creación:")

for estudiante in crud.leer_estudiantes():

    print(estudiante)

crud.actualizar_estudiante(1, "Carlos", 23, "Ingeniería Civil")

print("Estudiantes después de la actualización:")

for estudiante in crud.leer_estudiantes():

    print(estudiante)

crud.borrar_estudiante(2)
print("Estudiantes después de la eliminación:")
for estudiante in crud.leer_estudiantes():
    print(estudiante)
