# This program will find the sum of all the prime numbers up to a given number
# Reference: https://projecteuler.net/problem=10

import math

def main():
    num = int(input("Please enter a number: "))
    while (num < 0):
        num = int(input("Please enter a positive integer: "))

    total = 0
    for i in range(0, num):
        if (isPrime(i)):
            total += i

    print("The sum of primes up to " + str(num) + " is : " + str(total))

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
