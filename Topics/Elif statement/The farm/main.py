chicken = 23
goat = 678
pig = 1296
cow = 3848
sheep = 6769
count = 1
money = int(input())
if money < chicken:
    print('None')
elif goat > money >= chicken:
    n = money // chicken
    if n == count:
        print(f'{n} chicken')
    else:
        print(f'{n} chickens')
elif pig > money >= goat:
    n = money // goat
    if n == count:
        print(f'{n} goat')
    else:
        print(f'{n} goats')
elif cow > money >= pig:
    n = money // pig
    if n == count:
        print(f'{n} pig')
    else:
        print(f'{n} pigs')
elif sheep > money >= cow:
    n = money // cow
    if n == count:
        print(f'{n} cow')
    else:
        print(f'{n} cows')
else:
    n = money // sheep
    print(f'{n} sheep')
