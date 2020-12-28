#basics of a return statements
def cube(num):
    return num * num * num


result = cube(3)
print(result)
#or you can do this
def cube2(num2):
    result = num2 * num2 * num2
    return result

print(cube2(3))

#or you can also do this
def cube3(num3):
    result2 = num3 * num3 * num3
    print(result2)
    #return

cube3(3)