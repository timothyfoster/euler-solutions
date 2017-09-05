# This program will find the 13 adjacent digits in series.txt which result in
# the largest possible product
# Reference: https://projecteuler.net/problem=8

from prettytable import PrettyTable

def main():
    # Open series.txt and read the digits into an array
    digits = []
    with open("series.txt", "r") as f:
        for line in f:
            line = line.strip()
            for c in line:
                digits.append(int(c))

    # Find all blocks without a zero
    allBlocks = []
    ind = 0
    while (ind < len(digits)):
        block = [digits[ind:ind+13], ind]
        if (not 0 in block[0]):
            allBlocks.append(block)
        ind += 1

    # Format a table to display the results
    table = PrettyTable(["SERIES", "POSITION", "PRODUCT", "COMMENTS"])
    table.align["PRODUCT"] = "l"

    # Find the maximum product
    prodMax = 0
    prodInd = 0
    ind = 0
    for block in allBlocks:
        total = 1
        xout = ""
        comments = ""

        for d in block[0]:
            total *= d
            xout += str(d)

        if (total > prodMax):
            prodInd = ind
            prodMax = total
            comments = "* New Max *"

        out = [str(xout), str(block[1]), str(total), comments]
        table.add_row(out)
        ind += 1

    print(table)
    print ("Series: " + str(allBlocks[prodInd][0]) + " | Index: " + str(allBlocks[prodInd][1]) + " | Product: " + str(prodMax))

main()
