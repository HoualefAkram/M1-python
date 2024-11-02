from math import log, sin, cos, sqrt


#### EXO 1 ####

# Q1
a, b = float(input("Enter A: ")), float(input("Enter B: "))
print(f"A^B={a**b}")
# Q2
a, b = float(input("Enter A: ")), float(input("Enter B: "))
c = sqrt((a**2) + (b**2))
print(f"c={c}")
# Q3
a = float(input("Enter A: "))
tanA = sin(a) / cos(a)
print(f"tan(a)={tanA}")
# Q4
a, b = float(input("Enter A: ")), float(input("Enter B: "))
c = round(a / b, 3)
print(f"c={c}")


#### EXO 2 ####

# Q1
a, b, c = (
    float(input("Enter A: ")),
    float(input("Enter B: ")),
    float(input("Enter C: ")),
)

if a < b:
    if a < c:
        print(f"Min: {a}")
    else:
        print(f"Min: {c}")

else:
    if b < c:
        print(f"Min: {b}")
    else:
        print(f"Min: {c}")
# Q2

# Using if/else
if a < b:
    if a < c:
        if b < c:
            print("A B C")
        else:
            print("A C B")
    else:
        if a < b:
            print("C A B")


else:
    if b < c:
        if c < a:
            print("B C A")
        else:
            print("B A C")
    else:
        print("C B A")

# using sorted
print(sorted([a, b, c]))

#### EXO 3 ####
while True:
    a, b, c = (
        int(input("Enter A: ")),
        int(input("Enter B: ")),
        int(input("Enter C: ")),
    )
    if not a:
        print("a must be an integer greater than 0")
        continue
    # Leave the loop if a > 0, note: b and c can be 0
    break

delta = b**2 - 4 * a * c
if delta > 0:
    x1 = (-b - sqrt(delta)) / (a * 2)
    x2 = (-b + sqrt(delta)) / (a * 2)
    print(f"x1={x1}, x2={x2}")
elif delta == 0:
    x = (-b) / (a * 2)
    print(f"x={x}")
else:
    print("No Solutions")


#### EXO 4 ####


# Q1
def get_positive(data):
    positive = 0
    for i in data:
        if i > 0:
            positive = positive + 1
    return positive


def get_negative(data):
    negative = 0
    for i in data:
        if i < 0:
            negative = negative + 1
    return negative


def get_null(data):
    null = 0
    for i in data:
        if i == 0:
            null = null + 1
    return null


N = [-1, 2, 3, -10, 5, 10, 0, 1, 0, 0, 2, -3, 0]

print(f"positive: {get_positive(N)}, negative: {get_negative(N)}, null: {get_null(N)}")


# Q2
def get_dividers(x):
    dividers = []
    for i in range(1, x + 1):
        if x % i == 0:
            dividers.append(i)
    return dividers


x = int(input("Enter X: "))
dividers = get_dividers(x)
is_prime = len(dividers) == 2
print(f"dividers: {dividers}, is prime: {is_prime}")


#### EXO 5 ####
def get_dividers_without_self(x):
    dividers = []
    for i in range(1, x):
        if x % i == 0:
            dividers.append(i)
    return dividers


x = int(input("Enter X: "))
dividers = get_dividers_without_self(x)
is_perfect = x == sum(dividers)
print(f"is perfect: {is_perfect}")

#### EXO 6 ####
phrase = "aaEecfgeEeeKlm"
e = 0
E = 0
for letter in phrase:
    if letter == "e":
        e = e + 1
    elif letter == "E":
        E = E + 1
print("e:", e, "E:", E)

#### EXO 7 ####
n = int(input("Enter n: "))
output = 0
u_n = 1
for _ in range(n + 1):
    old_output = output
    output = output + u_n
    u_n = old_output
print(output)


#### EXO 8 ####

x = int(input("Enter X: "))
counter = 0
while x != 1:
    if x % 2 == 0:
        x = x / 2
    else:
        x = x * 3 + 1
    counter = counter + 1
    print(f"Syracuse(", counter, ") = ", x)
print("iterations: ", counter)


#### EXO 9 ####
def factorial(n):
    if n == 1:
        return 1
    counter = n - 1
    while counter > 1:
        n = n * counter
        counter = counter - 1
    return n


x = float(input("Enter x: "))
k = int(input("Enter k: "))
output = 0
sign = 1
for i in range(k):
    i = i * 2 + 1
    val = sign * (x**i) / factorial(i)
    output = output + val
    sign = sign * -1
print(output)


### EXO 10
g = 9.81
while True:
    h0, ep, n = (
        float(input("initial height: ")),
        float(input("epsilon: ")),
        int(input("n: ")),
    )
    if h0 > 0 and ep >= 0 and ep < 1 and n >= 0:
        break
v0 = sqrt(2 * g * h0)
v = v0 * (ep**n)
h = (v**2) / (2 * g)
print(f"height: {h}")


### EXO 11
# Using a while loop
g = 9.81
while True:
    h0, ep, h_fin = (
        float(input("initial height: ")),
        float(input("epsilon: ")),
        float(input("final height: ")),
    )
    if ep >= 0 and ep < 1 and h0 > 0 and h_fin > 0 and h_fin < h0:
        break
v0 = sqrt(2 * g * h0)
v = v0
counter = 0
while True:
    counter = counter + 1
    v = v * ep
    h = (v**2) / (2 * g)
    if h <= h_fin:
        break
print(f"n: {h_fin}")

# Using direct calculations
g = 9.81
while True:
    h0, ep, h_fin = (
        float(input("initial height: ")),
        float(input("epsilon: ")),
        float(input("final height: ")),
    )
    if ep >= 0 and ep < 1 and h0 > 0 and h_fin > 0 and h_fin < h0:
        break

v1 = sqrt(2 * g * h_fin)
v0 = sqrt(2 * g * h0)
n = log(v1 / v0) / log(ep)
print(f"n: {round(n)}")
