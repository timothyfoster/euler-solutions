# This program will find a counterexample to Goldbach's conjecture that
# every odd composite can be written as the sum of a prime and 2 times a square
# Reference: https://projecteuler.net/problem=46

import math

def main():

    composite = 9
    itsTrue = True
    while (itsTrue):
        itsTrue = False
        compositeReduced = math.ceil(math.sqrt(composite))

        for prime in range(2,composite):
            if (isPrime(prime)):
                for square in range(0,compositeReduced):
                    if (composite - prime - (2*(square**2)) == 0):
                        # print("Composite: " + str(composite) + " = " + str(prime) + " + 2 * " + str(square) + "^2")
                        # ^^ Uncomment this line to print out all the composites where the conjecture is true
                        itsTrue = True # The conjecture is true!
                        break
                if (itsTrue):
                    break

        if (not itsTrue):
            print("We found a counterexample!")
            print("The composite: " + str(composite) + " cannot be written as the sum of a prime and 2 * a square.")

        composite += 2
        while (not isComposite(composite)):
            composite += 2


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

def isComposite(num):
    factor = 0
    for i in range(1,num):
        if num % i == 0:
            factor = i
        if factor > 1:
            return True

    return False

main()
