n = int(input())

for _ in range(n):
    num = int(input())
    msg = "Bye."
    if num == 88:
        msg = "Hello"
    elif num == 86:
        msg = "How are you?"
    elif num < 88:
        msg = "GREAT!"
    print(msg)
