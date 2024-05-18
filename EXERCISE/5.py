n = int(input())
prices = 0

for _ in range(n):
    price = float(input())
    if 0.01 > price > 100.00:
        continue
    days = int(input())
    if 1 > days > 31:
        continue
    capsules = int(input())
    if 1 > capsules > 2000:
        continue
    prices += price*capsules*days
    print(f"The price for the coffee is: ${price*capsules*days:0.02f}")

print(f"Total: ${prices:0.02f}")
