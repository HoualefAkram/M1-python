from math import sqrt, log


# #### EXO 9 ####
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
print(f"n: {counter}")

# # Using direct calculations
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
