#!/usr/bin/python3
from sys import argv

def fac(n: int) -> int:
    for i in range(2, n):
        if n % i == 0:
            return i
    return 1

if len(argv) <= 1:
    print("Usage: factors <file>")
    exit(1)

f = open(argv[1])

line = f.readline()
while line:
    n = int(line)
    q = fac(n)
    p = n // q
    print(f"{n}={p}*{q}")
    line = f.readline()
