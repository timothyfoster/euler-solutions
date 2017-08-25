# This program will print the Fibonacci sequence up to a given number of terms

def main():
    terms = 0
    while (terms <= 0):
        terms = int(input("Please enter a positive integer: "))

    m = 0
    n = 1
    count = 1
    out = "0, "

    if (terms > 1):
        while (count < terms):
            count += 1
            temp = n
            n += m
            m = temp
            out += str(m) + ", "

    out = out.strip(', ')
    print(out)

main()
