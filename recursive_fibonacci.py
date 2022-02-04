
# n = (n-1)+(n-2)
# 1,1,2,3,5,8,13,21,34,55
# 1 2 3 4 5 6 7  8  9  10

def fibboRecursive(n): # O(2^n) - bardzo wolna
    if n<3:
        return 1

    return fibboRecursive(n-1) + fibboRecursive(n-2)


def fibboIterative(n): #O(n)
    pierwszy = 1
    drugi = 1
    #count = 0
    liczba = 0
    for i in range(0,n-2): #odejmujemy 2 bo startujemy z dwoma liczbami od 3 indeksu
        # count += 1
        # if count == (n-1):
        #     return liczba
        liczba = pierwszy + drugi
        pierwszy = drugi
        drugi = liczba
    return liczba

print(fibboIterative(42))
print(fibboRecursive(42))