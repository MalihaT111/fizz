def fizzbuzz():
    # - For each number from 1-100, the program prints the number (using print)
    for i in range(1,101):
        # - If the number is evenly divisible by 3, the program also prints "fizz"
        # - If it's evenly divisible by both, it prints "fizzbuzz"
        if (i % 3 == 0 and i % 5 == 0):
            print(i, "fizzbuzz")
        elif (i % 3 == 0):
            print(i, "fizz")
        # - If the number is evenly divisible by 5, the program also prints "buzz"
        elif (i % 5 == 0):
            print(i, "buzz")
        else: 
            print(i)
        # - The program should use a method to determine what to print.
fizzbuzz()