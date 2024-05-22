string_one = input()
string_two = input()

last_printed = string_one

for chars in range(len(string_one)):
    left_part = string_two[:chars + 1]
    right_part = string_one[chars + 1:]
    result = left_part + right_part
    if result != last_printed:
        print(result)
        last_printed = result

if string_one == string_two:
    print(string_two)
