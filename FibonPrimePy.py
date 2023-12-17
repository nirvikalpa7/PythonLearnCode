import math


# Print Fibonacci sequence
def fibonachi(n: int):
    a = 0
    b = 1
    print("Fib Sequence: ", a, ", ", b, ", ", end="", sep="")

    n = n - 2
    while n > 0:
        tmp = a + b
        a = b
        b = tmp
        print(b, end="")
        n -= 1
        if n > 0:
            print(", ", end="")


# Non optimized way to test if a number is prime
def is_prime_num(n: int) -> bool:
    if n % 2 == 0:
        return False
    max = int(math.sqrt(n))
    i = 3
    while i <= max:
        if n % i == 0:
            return False
        i += 2
    return True


fibonachi(15)

print("\nPrime numbers")
print(107, " - ", is_prime_num(107), sep="")
print(101, " - ", is_prime_num(101), sep="")
print(44, " - ", is_prime_num(44), sep="")
print(33, " - ", is_prime_num(33), sep="")
print(13, " - ", is_prime_num(13), sep="")
print(7, " - ", is_prime_num(7), sep="")
