import math

n = int(input())

for _ in range(n):
    n = int(input())
    if n % 7 == 0:
        print(round(math.pow(n, 2)))
