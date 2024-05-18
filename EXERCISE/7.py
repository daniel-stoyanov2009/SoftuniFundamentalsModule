command = input()

while command != "End":
    for current_char in range(0, len(command)):
        print(command[current_char]*2, end='')
    print()
    command = input()