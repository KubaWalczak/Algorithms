# n = (n-1)+(n-2)
# 1,1,2,3,5,8,13,21,34,55
# 1 2 3 4 5 6 7  8  9  10

count = 0
def dynamic_fibonacci():  # O(n)
    cache = {}

    def fibonacci(num):
        global count
        count += 1
        if num < 3:
            return 1
        elif num in cache:
            return cache[num]
        else:
            cache[num] = fibonacci(num - 1) + fibonacci(num - 2)
            return cache[num]

    return fibonacci

count2 = 0
def dynamic_fibonacci2(num): #called bottom-up
    answer = [1,1]
    global count2
    for i in range(2,num):
        count2 += 1
        answer.append(answer[i-2] + answer[i-1])
    return answer[-1]

fibo = dynamic_fibonacci()
fibo2 = dynamic_fibonacci2(10)

print('fibo1:', fibo(10), '- count:', count)
print('fibo2:', fibo2, '- count2:', count2)
