#!/usr/bin/python3
import sys

def factorize(n):
    f = []
    for i in range(2, n+1):
        while n % i == 0:
            f.append(i)
            n //= i
        if n == 1:
            break
    return f

def main(file_name):
    with open(file_name, 'r') as file:
        for line in file:
            n = int(line.strip())
            f = factorize(n)
            if len(f) == 2:
                print(f"{n}={f[0]}*{f[1]}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: factors <file>")
        sys.exit(1)
    file_name = sys.argv[1]
    main(file_name)
