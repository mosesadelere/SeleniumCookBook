import random as rand

myGuess = rand.randint(1,20)

print("Make a guess between 1 and 20.")
print("You have 7 guess life")

for guessIn in range(1, 8):
    print("Take a guess")
    guess = int(input())

    if guess.__gt__(20):
        print("Your guess can not be greater than 20.")

    if guess.__eq__(myGuess):
        with open('myguess.txt', 'a') as f:
            f.write('Nice Try Baby!!!!\n')
print("My guess is acyually " + str(myGuess))    
