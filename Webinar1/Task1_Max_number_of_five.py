# Программа, которая принимает 5 чисел и находит
#  максимальное из них

def number(a, b, c, d, e):
    max = a
    if b > max:
        max = b
    if c > max:
        max = c
    if d > max:
        max = d
    if e > max:
        max = e

    print(f"Наибольшее число {max}")

number(15, 25, 35, 16, 14)

