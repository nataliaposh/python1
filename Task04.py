number = int(input("Enter an integer: "))
maximum = 0
while (number > 0):
    maximum = max(maximum, number % 10)
    number = number // 10

print(maximum)
