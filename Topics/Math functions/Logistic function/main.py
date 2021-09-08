import math

x = float(input())
if x < 0:
    print(round(1 / (1 + math.exp(-x)), 2))
else:
    print(round(math.exp(x) / (math.exp(x) + 1), 2))
