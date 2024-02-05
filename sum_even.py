number = list()
even_number = list()
while True:
    inp = input("Please enter a number: ")
    if inp == "done":
        break
    try:
        value = int(inp)
        number.append(value)
        if value % 2 == 0:
            even_number.append(value)
    except ValueError:
        print("Invalid number: ")
result = sum(even_number)
print("The sum of the even numbers is: ", result) 
