import math

x = int(input())
area = 2 * math.sqrt(3) * math.pow(x, 2)
volume = math.sqrt(2) * math.pow(x, 3) / 3

print(round(area, 2), round(volume, 2))
