
# n = (n-1)+(n-2)
# 1,1,2,3,5,8,13,21,34,55
# 1 2 3 4 5 6 7  8  9  10

count_rec = 0
count_iter = 0
def fibboRecursive(n): # O(2^n) - bardzo wolna
    global count_rec
    count_rec += 1
    if n<3:
        return 1

    return fibboRecursive(n-1) + fibboRecursive(n-2)


def fibboIterative(n): #O(n)
    pierwszy = 1
    drugi = 1
    #count = 0
    liczba = 0
    if n < 3:
        return 1
    else:
        for i in range(0,n-2): #odejmujemy 2 bo startujemy z dwoma liczbami od 3 indeksu
            global count_iter
            count_iter += 1

            liczba = pierwszy + drugi
            pierwszy = drugi
            drugi = liczba
        return liczba

print(fibboIterative(10))
print(fibboRecursive(10))
print(count_rec)
print(count_iter)
