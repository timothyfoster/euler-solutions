# This program will determine how many starting numbers below ten million
# will arrive at 1 or 89 if the sum of the square of their digits are added
# during each iteration to determine the next number in the chain.
# Reference: https://projecteuler.net/problem=92

import math

def main():
    count = 0
    for i in range(1, 10000000):
        chain = [i]
        digitsAdded = squareAndAdd(i)

        while digitsAdded != 1 and digitsAdded != 89 and digitsAdded not in chain:
            chain.append(digitsAdded)
            digitsAdded = squareAndAdd(digitsAdded)

        chain.append(digitsAdded)

        if (digitsAdded == 89):
            count += 1
            #printChain(chain)

    print("Total chains ending in 89 is: " + str(count))

def printChain(chain):
    chainStr = ""
    for c in chain:
        chainStr += str(c) + " --> "
    chainStr = chainStr[:-5]
    print(chainStr)

def squareAndAdd(num):
    numStr = str(num)
    total = 0

    for c in numStr:
        total += int(c)**2

    return total

main()
