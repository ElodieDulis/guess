import numpy as np
# Game start 
magicNumber = np.random.randint(100)
guessedNumber = int(input("Try to enter a number between 1 and 100 \n"))
# Guessing process
while (magicNumber != guessedNumber):
    if magicNumber > guessedNumber : 
        guessedNumber = int(input("Your number is too low ! try again \n"))
    else:
        guessedNumber = int(input("Your number is too high ! try again \n"))
# Game end 
print("Good job ! The magic number is : " + str(magicNumber))

