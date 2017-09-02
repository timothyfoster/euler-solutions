# This program will find the quadratic expression n^2 + an + b which produces
# The maximum number of primes for consecutive values of n for |a| and |b| < 1000

import math

def main():
    maxN = 0; maxA = 0; maxB = 0
    for a in range(-20000, 20000):
        for b in range(-20000, 20000):
            n = 0
            while (isPrime(n**2 + a*n + b)):
                n += 1
            n -= 1
            if (n > maxN):
                maxN = n
                maxA = a
                maxB = b

    print("Solution: n^2 + " + str(maxA) + "n + " + str(maxB))
    print("Max N: " + str(maxN))

    n = 0
    while (n <= maxN):
        print("N: " + str(n) + " | " + str(n**2) + " + " + str(maxA*n) + " + " + str(maxB) + " = " + str(n**2 + maxA*n + maxB))
        n += 1

def isPrime(num):
    if (num <= 1):
        return False
    elif (num <= 3):
        return True
    elif (num % 3 == 0 or num % 2 == 0):
        return False

    sqrt = math.ceil(math.sqrt(num))
    i = 5

    while (i <= sqrt):
        if (num % i == 0):
            return False
        i += 1

    return True

main()
