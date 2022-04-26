a = int(input("Enter a: "))
b = int(input("Enter b: "))

d = a
n = 1
while (d < b):
    d = d + 0.1 * d
    n = n + 1

print(n)
