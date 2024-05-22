year = int(input())

while True:
    if len(str(year)) == 1:
        year_string = f"000{year}"
    elif len(str(year)) == 2:
        year_string = f"00{year}"
    elif len(str(year)) == 3:
        year_string = f"0{year}"
    else:
        year_string = f"{year}"
    check = {year_string[0], year_string[1], year_string[2], year_string[3]}
    if len(check) == 4:
        print(year_string)
        break
    year += 1
