import sqlite3

# Conexión a la base de datos (se creará si no existe)
conn = sqlite3.connect('estudiantes.db')
c = conn.cursor()

# Creación de la tabla estudiantes
c.execute('''
CREATE TABLE IF NOT EXISTS estudiantes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT,
    edad INTEGER,
    carrera TEXT
)
''')
conn.commit()

# Funciones CRUD
def crear_estudiante(nombre, edad, carrera):
    c.execute('INSERT INTO estudiantes (nombre, edad, carrera) VALUES (?, ?, ?)', (nombre, edad, carrera))
    conn.commit()

def leer_estudiantes():
    c.execute('SELECT * FROM estudiantes')
    return c.fetchall()

def actualizar_estudiante(id, nombre, edad, carrera):
    c.execute('UPDATE estudiantes SET nombre = ?, edad = ?, carrera = ? WHERE id = ?', (nombre, edad, carrera, id))
    conn.commit()

def borrar_estudiante(id):
    c.execute('DELETE FROM estudiantes WHERE id = ?', (id,))
    conn.commit()

# Ejemplos de uso
crear_estudiante("Carlos", 22, "Ingeniería")
crear_estudiante("Ana", 23, "Derecho")
print("Estudiantes después de la creación:")
print(leer_estudiantes())

actualizar_estudiante(1, "Carlos", 23, "Ingeniería Civil")
print("Estudiantes después de la actualización:")
print(leer_estudiantes())

borrar_estudiante(2)
print("Estudiantes después de la eliminación:")
print(leer_estudiantes())

# Cerrar la conexión
conn.close()
