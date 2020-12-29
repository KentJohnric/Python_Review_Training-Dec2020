#Limit of 3 Guesses only
secret_word = "giraffe"
guess = ""
guess_count = 1
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    if(guess_count <= guess_limit):
        guess = input("Enter Guess: ")
        print("Number of Guess: " + str(guess_count))
        res = guess_limit - guess_count
        print("Guesses Left: " + str(res))
        guess_count +=1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Out of Guesses, YOU LOSE!")
else:
    print("You Win!")