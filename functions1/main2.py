def reverse():
    s = input("Введіть ваш рядок: ")
    r = ""
    for i in s:
        r = i + r

    return r


def reverse_slice():
    s = input("Введіть ваш рядок: ")
    return s[::-1]


r, r2 = reverse(), reverse_slice()
print("Перевертень:", r, r2)

# r2 = reverse_slice()
# print("Перевертень (зрізи):", r2)
