revenue = float(input("Enter revenue: "))
costs = float(input("Enter expenses: "))

if revenue > costs:
    profit = revenue - costs
    print("Profit is %4.2f" % (profit))
    staff = int(input("Enter staff number: "))
    margin = 100. * (revenue - costs) / revenue
    print("Margin is %4.2f %%" % margin)
    print("Profit per employee is %4.2f" % (profit / staff))

if revenue < costs: print("Loss")
if revenue == costs: print("Zero profit")
