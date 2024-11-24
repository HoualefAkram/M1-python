### EXO 6


def fact(n):
    if n == 0 or n == 1:
        return 1
    return n * fact(n - 1)


def sinus(x, k):
    resultat = 0
    sign = 1
    for i in range(k):
        j = 2 * i + 1
        val = sign * x**j / fact(j)
        sign = sign * -1
        resultat += val
    return resultat


def cosinus(x, k):
    resultat = 0
    sign = 1
    for i in range(k):
        j = 2 * i
        val = sign * x**j / fact(j)
        sign = sign * -1
        resultat += val
    return resultat


def expo(x, k):
    resultat = 0
    for i in range(k):
        val = x**i / fact(i)
        resultat += val
    return resultat


while True:
    choice = int(input("1 - sin(x)\n2 - cos(x)\n3- exp(x)\nChoose: "))
    if choice > 0 and choice < 4:
        break

x, k = float(input("x: ")), int(input("k: "))

if choice == 1:
    resultat = sinus(x, k)
    print(f"sin({x}) = {resultat}")
elif choice == 2:
    resultat = cosinus(x, k)
    print(f"cos({x}) = {resultat}")
else:
    resultat = expo(x, k)
    print(f"expo({x}) = {resultat}")


### EXO 7
