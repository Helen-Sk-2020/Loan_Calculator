import math
a = int(input())
b = int(input()) 
if b <= 1:
    log = math.log(a)
else:
    log = math.log(a, b)
print(round(log, 2))
