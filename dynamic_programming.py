

def memoizedAddto80():
    cache = {}
    def inner_memo(num):
        if num in cache:
            return cache[num]
        else:
            print('long time')
            cache[num] = num + 80
            return cache[num]
    return inner_memo

memoized = memoizedAddto80()
print(memoized(5))
print(memoized(5))