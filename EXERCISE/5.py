n = int(input())
total_price = 0

for _ in range(n):
    price_per_capsule = float(input())
    days = int(input())
    capsules = int(input())
    if price_per_capsule < 0.01 or price_per_capsule > 100.00:
        continue
    elif days < 1 or days > 31:
        continue
    elif capsules < 1 or capsules > 2000:
        continue
    price = price_per_capsule * capsules * days
    total_price += price
    print(f"The price for the coffee is: ${price:0.02f}")
print(f"Total: ${total_price:0.02f}")
