def while_loop(arg1, increment):
    i = 0
    numbers = []
    while i <= arg1:
        print("At the top i is %d" % i)
        numbers.append(i)
        i = i + increment
        print("Numbers now: ", numbers)
    print("At the bottom i is %d" % i)
    print("The numbers: ")
    for num in numbers:
        print(num)


while_loop(13, 2)
