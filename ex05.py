def ordenar(lista):
    pares = []
    impares = []
    for i in lista:
        if i % 2 == 0:
            pares.append(i)
        else:
            impares.append(i)

    pares.sort()
    impares.sort(reverse=True)
    lista = pares
    for i in impares:
        lista.append(i)
    
    return lista

lista = range(0,10)
print(ordenar(lista))