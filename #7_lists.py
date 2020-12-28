lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kent", "Chow", "Rod", "Jeremy", "Charles", "Kent", "Simon"]
print(friends)
#index output
print(friends[1])
#output index 1 up to last
print(friends[1:])
#range index
print(friends[1:3])
#changing the value in the lists
friends[1] = "Ariadne"
print(friends)
#extend the new list
friends.extend(lucky_numbers)
print(friends)
#adding a new string in the list
friends.append("AC4")
print(friends)
#inserting a new string in the list with specific index
friends.insert(1, "Tnek")
print(friends)
#removing a string in the list
friends.remove("Tnek")
print(friends)
#removes the last element in the lists
friends.pop()
print(friends)
#check if name exists
print(friends.index("Jeremy"))
#count the same element 
print(friends.count("Kent"))
#sort the list also works with string
lucky_numbers.sort()
print(lucky_numbers)
#reverse the sort list
lucky_numbers.reverse()
print(lucky_numbers)
#copy a list
friends2 = friends.copy()
print(friends2)
#clearing the list
friends.clear()
print(friends)