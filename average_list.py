the_list = list()
while True:
    inp = input("Please enter a number: ")
    if inp == "done":
        break

    try:
        value = float(inp)
        the_list.append(value)
    except ValueError:
        print("please enter an int or a float")

average = sum(the_list) / len(the_list)
print("The average is: ", average)