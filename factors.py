#!/usr/bin/python3
from sys import argv

def fac(n: int) -> int:
    i = 2
    while i < n:
        x = n // i
        if x * i == n:
            return x, i
        i += 1
    return None

if len(argv) <= 1:
    print("Usage: factors <file>")
    exit(1)

f = open(argv[1])

line = f.readline()
while line:
    n = int(line)
    p, q = fac(n)
    print(f"{n}={p}*{q}")
    line = f.readline()
