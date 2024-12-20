
def divisors(n):
    assert n > 0
    for t in range(1, int(n**0.5)+1):
        if n % t == 0:
            yield t
            if (d := n // t) != t:
                yield d

def is_prime(n):
    return len(tuple(divisors(n))) == 2

def is_perfect(n):
    return sum(divisors(n)) == 2*n

def perfects(max):
    return (n for n in range(1, max+1) if is_perfect(n))


if __name__ == "__main__":
    print(list(divisors(6)))
    print(list(divisors(1024)))
    print(is_prime(7))
    print(is_prime(24))
    print(is_prime(1))
    print(tuple(perfects(10000)))
