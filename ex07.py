from functools import lru_cache
from sys import setrecursionlimit

setrecursionlimit(100000)

@lru_cache
def factorielle(n):
    if n == 1:
        return n
    else:
        return factorielle(n-1) * n

@lru_cache
def hyperfactorielle(n):
    if n == 1:
        return n
    else:
        return hyperfactorielle(n-1) * n**n
    
@lru_cache
def superfactorielle(n):
    if n == 1:
        return n
    else:
        return superfactorielle(n-1) * factorielle(n)

@lru_cache
def hyperpuissance(a, n):
    p = a
    for _ in range(n):
        


print(superfactorielle(5))