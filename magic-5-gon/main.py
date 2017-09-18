# This program will find
# Reference: https://projecteuler.net/problem=68

range1 = lambda start, end: range(start, end+1)

def main():

    a1 = 0
    a2 = 0
    a3 = 0
    b1 = 0
    b2 = a3
    b3 = 0
    c1 = 0
    c2 = b3
    c3 = 0
    d1 = 0
    d2 = c3
    d3 = 0
    e1 = 0
    e2 = d3
    e3 = a2

    used = []

    for i in range1(1,10):
        if i in used:
            break
        used.append(i)
        a1 = i
        checkSoln(a1, a2, a3, b1, b2, b3, c1, c2, c3, d1, d2, d3, e1, e2, e3)
        for j in range1(1,10):
            if j in used:
                break
            used.append(j)
            a2 = j
            e3 = a2
            checkSoln(a1, a2, a3, b1, b2, b3, c1, c2, c3, d1, d2, d3, e1, e2, e3)
            for k in range1(1,10):
                if k in used:
                    break
                used.append(k)
                a3 = k
                b2 = a3
                checkSoln(a1, a2, a3, b1, b2, b3, c1, c2, c3, d1, d2, d3, e1, e2, e3)
                for l in range1(1,10):
                    if l in used:
                        break
                    used.append(l)
                    b1 = l
                    checkSoln(a1, a2, a3, b1, b2, b3, c1, c2, c3, d1, d2, d3, e1, e2, e3)
                    for m in range1(1,10):
                        if m in used:
                            break
                        used.append(m)
                        b3 = m
                        c2 = b3
                        checkSoln(a1, a2, a3, b1, b2, b3, c1, c2, c3, d1, d2, d3, e1, e2, e3)
                        for n in range1(1,10):
                            if n in used:
                                break
                            used.append(n)
                            c1 = n
                            checkSoln(a1, a2, a3, b1, b2, b3, c1, c2, c3, d1, d2, d3, e1, e2, e3)
                            for o in range1(1,10):
                                if o in used:
                                    break
                                used.append(o)
                                c3 = o
                                d2 = c3
                                checkSoln(a1, a2, a3, b1, b2, b3, c1, c2, c3, d1, d2, d3, e1, e2, e3)
                                for p in range1(1,10):
                                    if p in used:
                                        break
                                    used.append(p)
                                    d1 = p
                                    checkSoln(a1, a2, a3, b1, b2, b3, c1, c2, c3, d1, d2, d3, e1, e2, e3)
                                    for q in range1(1,10):
                                        if q in used:
                                            break
                                        used.append(q)
                                        d3 = q
                                        e2 = d3
                                        checkSoln(a1, a2, a3, b1, b2, b3, c1, c2, c3, d1, d2, d3, e1, e2, e3)
                                        for r in range1(1,10):
                                            if r in used:
                                                break
                                            e1 = r
                                            checkSoln(a1, a2, a3, b1, b2, b3, c1, c2, c3, d1, d2, d3, e1, e2, e3)
                                        used.remove(q)
                                    used.remove(p)
                                used.remove(o)
                            used.remove(n)
                        used.remove(m)
                    used.remove(l)
                used.remove(k)
            used.remove(j)
        used.remove(i)
        a1 = 0
        a2 = 0
        a3 = 0
        b1 = 0
        b2 = 0
        b3 = 0
        c1 = 0
        c2 = 0
        c3 = 0
        d1 = 0
        d2 = 0
        d3 = 0
        e1 = 0
        e2 = 0
        e3 = 0

def checkSoln(a1, a2, a3, b1, b2, b3, c1, c2, c3, d1, d2, d3, e1, e2, e3):
    aT = a1 + a2 + a3
    bT = b1 + b2 + b3
    cT = c1 + c2 + c3
    dT = d1 + d2 + d3
    eT = e1 + e2 + e3

    print(a1, a2, a3, b1, b3, c1, c3, d1, d3, e1)

    # if (aT == bT and bT == cT and cT == dT and dT == eT):
    #     print(str(a1) + " " + str(a2) + " " + str(a3) + " " +
    #     str(b1) + " " + str(b2) + " " + str(b3) + " " +
    #     str(c1) + " " + str(c2) + " " + str(c3) + " " +
    #     str(d1) + " " + str(d2) + " " + str(d3) + " " +
    #     str(e1) + " " + str(e2) + " " + str(e3))
    #     return True
    # else:
    #     return False

main()
