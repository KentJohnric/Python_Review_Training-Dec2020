def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result
num1 = int(input("Enter the numner: "))
expo = int(input("Enter the exponent: "))

print("Exponent Result: " + str(raise_to_power(num1, expo)))