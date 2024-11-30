def generar_n_caracteres(n, caracter):
    """
    Devuelve una cadena con el carácter repetido n veces.

    Args:
        n (int): Número de repeticiones.
        caracter (str): Carácter a repetir.

    Returns:
        str: Cadena con el carácter repetido n veces.
    """
    return caracter * n

# Ejemplo de uso
print(generar_n_caracteres(5, "x"))  # Salida: "xxxxx"
