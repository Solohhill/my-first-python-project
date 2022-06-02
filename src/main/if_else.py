print("Welcome to my Calculator!!")
print("To end type "'quit ' "when prompted ""'What do you want to do next?'")
print("_________________________________________________________________")

while True:
    val1 = int(input("What is the first value?"))
    val2 = int(input("What is the second value?"))

    operation = input("What do you want to do next?")

    if "+" == operation:
        print(val1 + val2)
    if "-" == operation:
        print(val1 - val2)
    if "%" == operation:
        print(val1 % val2)
    if "*" == operation:
        print(val1 * val2)
    if "/" == operation:
        print(val1 / val2)
    if "quit" == operation:
        break