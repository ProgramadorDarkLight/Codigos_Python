# Definimos una función para sumar dos números
def suma(a, b):
    return a + b  # Devuelve la suma de a y b

# Definimos una función para restar dos números
def resta(a, b):
    return a - b  # Devuelve la resta de a y b

# Definimos una función para multiplicar dos números
def multiplicacion(a, b):
    return a * b  # Devuelve la multiplicación de a y b

# Definimos una función para dividir dos números
def division(a, b):
    if b != 0:  # Verificamos que el divisor no sea cero
        return a / b  # Devuelve la división de a por b
    else:
        return "Error: División por cero"  # Devuelve un mensaje de error si el divisor es cero

# Función para mostrar el menú de opciones al usuario
def menu():
    print("Selecciona una operación:")  # Imprime el título del menú
    print("1. Suma")  # Opción para suma
    print("2. Resta")  # Opción para resta
    print("3. Multiplicación")  # Opción para multiplicación
    print("4. División")  # Opción para división
    print("5. Salir")  # Opción para salir del programa

# Función principal donde se ejecuta el bucle principal del programa
def main():
    while True:  # Bucle infinito que se ejecuta hasta que el usuario elige salir
        menu()  # Llama a la función menú para mostrar las opciones
        eleccion = input("Introduce tu elección (1/2/3/4/5): ")  # Solicita al usuario que elija una opción

        if eleccion in ['1', '2', '3', '4']:  # Verifica si la elección es válida
            num1 = float(input("Introduce el primer número: "))  # Solicita el primer número
            num2 = float(input("Introduce el segundo número: "))  # Solicita el segundo número

            if eleccion == '1':  # Si la elección es 1, realiza una suma
                print("Resultado:", suma(num1, num2))  # Imprime el resultado de la suma
            elif eleccion == '2':  # Si la elección es 2, realiza una resta
                print("Resultado:", resta(num1, num2))  # Imprime el resultado de la resta
            elif eleccion == '3':  # Si la elección es 3, realiza una multiplicación
                print("Resultado:", multiplicacion(num1, num2))  # Imprime el resultado de la multiplicación
            elif eleccion == '4':  # Si la elección es 4, realiza una división
                print("Resultado:", division(num1, num2))  # Imprime el resultado de la división

        elif eleccion == '5':  # Si la elección es 5, el usuario quiere salir
            print("Saliendo...")  # Imprime un mensaje de salida
            break  # Termina el bucle, saliendo del programa
        else:
            print("Opción no válida, por favor intenta de nuevo.")  # Imprime un mensaje de error si la elección no es válida

# Verifica si este archivo se está ejecutando como el script principal
if __name__ == "__main__":
    main()  # Llama a la función principal
