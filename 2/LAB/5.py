n = int(input())

for n in range(1, n+1):
    sum_of_digits = 0
    number = str(n)
    for i in range(len(number)):
        sum_of_digits += int(number[i])
    if sum_of_digits == 5 or sum_of_digits == 7 or sum_of_digits == 11:
        print(number + " -> True")
    else:
        print(number + " -> False")
