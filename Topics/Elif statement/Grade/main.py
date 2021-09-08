score = int(input())
maximum = int(input())
x = float(score / maximum * 100)
if x < 60:
    print('F')
elif x < 70:
    print('D')
elif x < 80:
    print('C')
elif x < 90:
    print('B')
else:
    print('A')
