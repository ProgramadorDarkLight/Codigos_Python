def superposicion(lista1, lista2):

    for elemento in lista1:
        if elemento in lista2:
            return True
    return false

print(superposicion([1,2,3],[3,4,5]))