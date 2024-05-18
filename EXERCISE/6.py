n = int(input())

for _ in range(n):
    string = input()
    if "," not in string and "." not in string and "_" not in string:
        print(f"{string} is pure.")
    else:
        print(f"{string} is not pure!")