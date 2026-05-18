def sum():
    a = int(input("Введіть перше число: "))
    b = int(input("Введіть введіть останнє число: "))

    if a > b:
        a, b = b, a

    s = 0
    for i in range(a, b + 1):
        s += i

    return s


def sum_gauss():
    a = int(input("Введіть перше число: "))
    b = int(input("Введіть введіть останнє число: "))

    if a > b:
        a, b = b, a

    return (a + b) * (b - a + 1) // 2


r = sum()
print(f"Сума діапазону дорівнює {r}")

r2 = sum_gauss()
print(f"Сума діапазону (формула Гауса) дорівнює {r2}")
