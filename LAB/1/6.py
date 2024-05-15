budget = int(input())
total_price = 0

cmd = input()

while cmd != "End":
    total_price += int(cmd)
    if total_price > budget:
        print("You went in overdraft!")
        break
    cmd = input()
else:
    print("You bought everything needed.")
