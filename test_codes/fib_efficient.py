def fib_efficient(n, d):
    '''
    return the fibonacci number in the position 'n'
    '''
    if n in d:
        return d[n]
    else:
        ans = fib_efficient(n-1, d) + fib_efficient(n-2, d)
        d[n] = ans # calculation memorization
        return ans


d = {1: 1, 2: 2}
print(fib_efficient(5, d))