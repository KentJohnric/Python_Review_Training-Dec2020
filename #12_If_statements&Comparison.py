def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        print("number 1 has the greatest value")
        return num1
    elif num2 >= num1 and num2 >= num3:
        print("number 2 has the greatest value")
        return num2
    else:
        print("number 3 has the greatest value")
        return num3
num1 = int(input("Enter Number 1: "))
num2 = int(input("Enter Number 2: "))
num3 = int(input("Enter Number 3: "))

print(max_num(num1, num2, num3))
#print(max_num(300, 40, 5))