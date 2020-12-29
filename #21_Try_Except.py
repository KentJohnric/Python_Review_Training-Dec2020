#use this if you dont want to have an error output

try:
    value = 10/0
    number = int(input("Enter a Number: "))
    print(number)
except ZeroDivisionError as err:
    print("The error is: " + str(err))
except ValueError:
    print("Invalid input")