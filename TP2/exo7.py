from math import cos, sin


def poly(x):
    global coeffs
    output = 0
    for i in range(len(coeffs)):
        output += coeffs[i] * (x**i)
    return output


def simpson(a, b, n, func):
    if n % 2 != 0:
        n -= 1
    h = (b - a) / n
    somme = 0
    j = a
    while j < b:
        somme += (h / 3) * (func(j) + 4 * func(j + h) + func(j + 2 * h))
        j += 2 * h
    return somme


def trapezes(a, b, n, func):
    h = (b - a) / n
    somme = 0
    j = a
    while j <= b:
        if j == a or j == b:
            c = 1
        else:
            c = 2
        somme += (h / 2) * c * func(j)
        j += h
    return somme


while True:
    func_type = int(input("1- Polynome\n2- Cos\n3- Sin\nChoose: "))
    if func_type > 0 and func_type < 4:
        break

if func_type == 1:
    degree = int(input("degree polynome: "))
    coeffs = []
    for i in range(degree + 1):
        coeff = float(input(f"coeff de x**{i}: "))
        coeffs.append(coeff)
    func = poly

elif func_type == 2:
    func = sin
else:
    func = cos


while True:
    method, a, b, n = (
        int(input("1- Simpson\n2- Trapezes\nChoose: ")),
        float(input("a = ")),
        float(input("b = ")),
        int(input("n = ")),
    )
    if n != 0 and b > a and 0 < method and method < 3:
        break
    print("n > 0 et b > a")

if method == 1:
    integral = simpson(a, b, n, func)
else:
    integral = trapezes(a, b, n, func)

print(integral)
