def ordenar_lista(lista):

    n = len(lista)

    for i in range(n):

        min_indice = i

        for j in range(i+1, n):

            if  lista[j]< lista[min_indice]:

                min_indice = j


        lista[i], lista[min_indice] = lista[min_indice], lista[i]

    return lista



print(ordenar_lista([64,25,12,22,11]))