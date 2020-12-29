num1 = float(input("Enter First Number: "))
op = input("Enter Operator: ")
num2 = float(input("Enter Second Number: "))

if op == "+":
    result = num1 + num2
    print(result)
elif op == "-":
    result = num1 - num2
    print(result)
elif op == "*":
    result = num1 * num2
    print(result)
elif op == "/":
    result = num1 / num2
    result2 = num1 % num2
    print(str(result) + "remainder of: " + str(result2))
else:
    print("Invalid Operator")
