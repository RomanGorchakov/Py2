n = 10

for i in range(1, 100):
    n += n / 10
    if n > 15:
        print(i)
        break