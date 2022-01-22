import random
ranNumber = random.randint(1,100)
userGuess = None
guesses = 0
while(userGuess != ranNumber):
    userGuess = int(input("Enter your guess: "))
    if(userGuess==ranNumber):
        print("You guess right")
    else:
        if userGuess>ranNumber:
            print("You guess wrong! Less number please")
        elif userGuess<ranNumber:
            print("You guess wrong! larger number please")
    guesses+=1
print(f"You guessed the number in {guesses} guesses")

with open("game/hiscore.txt", "r") as f:
    hiscore = int(f.read())
if guesses<hiscore:
    print("High score!")
    with open("game/hiscore.txt", "w") as f:
        f.write(str(guesses))