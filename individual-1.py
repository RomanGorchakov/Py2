n = int(input("Введите число: "))
k = n // 7
r = n % 7

if r == 0:
    print(f"n == 7 * {k}")
else:
    print(f"n == 7 * {k} + {r}")