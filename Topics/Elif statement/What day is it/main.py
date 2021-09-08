offset = float(input())
time = 10 + offset
if time < 0:
    print('Monday')
elif time < 24:
    print('Tuesday')
else:
    print('Wednesday')
