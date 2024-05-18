n = int(input())
prices = 0

for _ in range(n):
    price = float(input())
    days = int(input())
    capsules = int(input())
    prices += price*capsules*days
    print(f"The price for the coffee is: ${price*capsules*days:0.02f}")

print(f"Total: ${prices:0.02f}")
