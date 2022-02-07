

przyklad = [7,5,2,33,10,0,3,33,23,0,12,3,99]

def selective_sort(array):
    for i in range(len(array)):
        index_minimum = i

        for y in range(i + 1, len(array)): #przesuwamy index od ktorego przegladamy liste w poszukiwaniu minimum
            #temp = array[i]
            if array[index_minimum] > array[y]:
                index_minimum = y


        array[i], array[index_minimum] = array[index_minimum], array[i]

    return array

print(selective_sort(przyklad))