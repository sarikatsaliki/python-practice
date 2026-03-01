def highest_even():
    numbers = input("Enter numbers separated by space: ")
    numbers = numbers.split()   # makes it a list of strings
    numbers = [int(num) for num in numbers]  # convert to integers
    highest = 0
    for value in numbers:
       if value%2==0:
         value%2> highest
         highest = value
    print(highest)
highest_even()