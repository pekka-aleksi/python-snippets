from decimal import Decimal, getcontext

getcontext().prec = 100_000_000
getcontext().Emax = 100_000_00

import numpy as np


def a(n):
    d = Decimal(np.sqrt(5))

    Phi = (1 + d) / 2
    phi = (1 - d) / 2

    r = (Phi ** n - phi ** n) / d

    return r


for t in range(0, 1_000_000, 100_000):
    with open(f"{t}.txt", 'wt') as file:
        print("Starting", t)
        n = a(t)
        print("Done calculating")

        file.write(str(n))
