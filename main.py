import numpy as np
guessedNumber = input("Try to enter a number between 1 and 100 \n")
print("Your first guess is : " + guessedNumber)
magicNumber = np.random.randint(100)
print("The magic number is : " + str(magicNumber))

