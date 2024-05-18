n = int(input())
prices = 0.00

for _ in range(n):
    price = float(input())
    if price < 0.01 or price > 100.00:
        continue
    days = int(input())
    capsules = int(input())
    if days not in range(1, 32):
        continue
    if capsules not in range(1, 2001):
        continue
    price = price*capsules*days
    if price <= 0:
        continue
    print(f"The price for the coffee is: ${price:0.02f}")
    prices += price

print(f"Total: ${prices:0.02f}")
