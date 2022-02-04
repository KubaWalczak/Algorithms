
#SILNIA! 5!= 5*4*3*2*1

def recursiveFactorial(number): #O(n)
    if number == 1:
        return 1
    return number * recursiveFactorial(number-1)

def iterativeFactorial(number): #O(n)
    suma = number
    next = number - 1

    for i in range(0,number-1):
        suma = suma * next
        next -= 1
    return suma


print(iterativeFactorial(5))
print(recursiveFactorial(5))

