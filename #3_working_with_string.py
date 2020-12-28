print("Giraffe\nAcademy")

print("Giraffe\"Academy")

phrase = "Giraffe Academy"
phrase2 = "is cool"
print(phrase + phrase2)

#To output a Lower Case string
print(phrase.lower())
print(phrase.upper())
#Checking if the phrase is all upper case
print(phrase.isupper())
#Converting the phrase to upper and then check if it is all upper case
print(phrase.upper().isupper())
#checking the lenght of the phrase
print(len(phrase))
#ouputting a index 
print(phrase[0:5])
#checking the index of the letter
print(phrase.index("f"))
print(phrase.index("Acad"))
#Changing the phrase Giraffe to Elephant
print(phrase.replace("Giraffe", "Elephant"))