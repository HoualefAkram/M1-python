# ### EXO 1
def fibo(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibo(n - 1) + fibo(n - 2)


# ### EXO 2

# Classic
n = int(input("n :"))
q = 0
r = 10
b = 1
a = 10
for i in range(n):
    q = q + 1
    r = r - b


## Recursion
def q(n):
    if n == 0:
        return 0
    return q(n - 1) + 1


def r(n):
    if n == 0:
        return a
    return r(n - 1) - b


### EXO 3

p = float(input("p: "))


def seuil(p):
    u = 3
    counter = 0
    while u <= p:
        counter += 1
        u = 0.9 * u + 1.3

    return counter - 1


def seuil_recursive(p, n=0):

    def u(n):
        if n == 0:
            return 3
        return 0.9 * u(n - 1) + 1.3

    if p >= u(n):
        return seuil_recursive(p, n + 1)
    return n - 1
