ages = int(input())
if ages <= 14:
    drink = "toddy"
elif ages <= 18:
    drink = "coke"
elif ages <= 21:
    drink = "beer"
else:
    drink = "whisky"
print(drink)
