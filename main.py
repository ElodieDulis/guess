import numpy as np

# Game start 
attempts = 1
np.random.seed()
magicNumber = np.random.randint(100)
guessedNumber = int(input("Try to enter a number between 1 and 100 \n"))

# Guessing process
while (magicNumber != guessedNumber & attempts < 6) :
    if magicNumber > guessedNumber : 
        guessedNumber = int(input("Your number is too low ! try again \n"))
    else:
        guessedNumber = int(input("Your number is too high ! try again \n"))
    attempts += 1

# Game end 
if guessedNumber == magicNumber : 
    print("Good job ! The magic number is : " + str(magicNumber))
else :
    print("Loser ! The magic number was : " + str(magicNumber))

