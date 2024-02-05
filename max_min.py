numbers = list()
while True:
    inp = input("Please enter a number: ")
    if inp == "done":
        inp.isupper()
        break
    try:
        value = int(inp)
        numbers.append(value)
    except ValueError:
        print("Invalid number, try again")

max_number = max(numbers)
min_number = min(numbers)

print("Maximum number is: ", max_number)
print("Minimum number is: ", min_number)
