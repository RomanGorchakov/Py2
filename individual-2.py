a, b, c = list(map(float, input("Введите три числа: ").split()))
up = []
up.append(a)
up.append(b)
up.append(c)

i = 0
while i < 2:
    j = 0
    while j < 2 - i:
        if up[j] > up[j+1]:
            up[j], up[j+1] = up[j+1], up[j]
        j += 1
    i += 1
print(up)
up.reverse()
print(up)