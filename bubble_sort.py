
przyklad = [7,5,2,1,3,23,33]

def bubble_sort(lista):

    for i in range(len(lista)-1):
        for y in range(len(lista)-1):
            if lista[y] > lista[y+1]:
                temp = lista[y]
                lista[y] = lista[y+1]
                lista[y+1] = temp
                # lista[y], lista[y+1] = lista[y+1], lista[y]


    return lista

print(bubble_sort(przyklad))
