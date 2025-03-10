#Guess the number
import random

number = (random.randint(1,100))
print(number)
attempts = 0

print("Guess the number bewtween 1 and 100 !!!!!!")

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess >> number:
        print("Too high. Try Again")
    elif guess < number:
        print("Too low. Try Again")
    else:
        print("Congratulation!!!!!, you guessed correctly")

        break

#Word Scrambler
import random

words = ["Car", "bike", "Cycle", "Fligh"]
word = random.choice(words)
attempts = 0

print("Guess the Word")

while True:
    guess = input("Enter your guess: ")
    attempts += 1

    if guess == word:
        print(f"Congratulations!!!!!, you guessed correctly in {attempts} attempts!")
        break
    else:
        print("Incorrect guess. Try Again!")
