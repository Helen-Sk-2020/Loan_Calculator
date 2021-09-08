s = input()

for c in s:
    if c.isupper():
        s = s.replace(c, '_' + c.lower())
        s = s.lstrip("_")

print(s)
