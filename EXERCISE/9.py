command = input()
success = True

while command != "Welcome!":
    name = command
    if name == "Voldemort":
        success = False
        print("You must not speak of that name!")
        break
    if len(name) < 5:
        print(f"{name} goes to Gryffindor.")
    elif len(name) == 5:
        print(f"{name} goes to Slytherin.")
    elif len(name) == 6:
        print(f"{name} goes to Ravenclaw.")
    elif len(name) > 6:
        print(f"{name} goes to Hufflepuff.")
    command = input()

if success:
    print("Welcome to Hogwarts.")
