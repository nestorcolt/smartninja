#  Adivina el numero

# parte 1
# secret = 22
# guess = int(input("Guess the secret number (between 1 and 30): "))
#
# if guess == secret:
#     print("You've guessed it - congratulations! It's number 22.")
# else:
#     print("Sorry, your guess is not correct... The secret number is not " + str(guess))


# parte 2
# while loop
# secret = 22
# guess = None
#
# while guess != secret:
#
#     guess = int(input("Guess the secret number (between 1 and 30): "))
#
#     if guess == secret:
#         print("You guessed it - congratulations! It's number 22.")
#     else:
#         print("Sorry, your guess is not correct... The secret number is not " + str(guess))

# parte 2
# for loop
# secret = 22
#
# #
# for index in range(5):
#     guess = int(input("Guess the secret number (between 1 and 30): "))
#
#     if guess == secret:
#         print("You've guessed it - congratulations! It's number 22.")
#         break
#     else:
#         print("Sorry, your guess is not correct... The secret number is not " + str(guess))

#
# using break on while
secret = 22

# while True:
#     guess = int(input("Guess the secret number (between 1 and 30): "))
#
#     if guess == secret:
#         print("You've guessed it - congratulations! It's number 22.")
#         break
#     else:
#         print("Sorry, your guess is not correct... The secret number is not " + str(guess))


# haciendo mas didactico nuestro juego:

secret = 22

# while True:
#     guess = int(input("Guess the secret number (between 1 and 30): "))
#
#     if guess == secret:
#         print("You've guessed it - congratulations! It's number 22.")
#         break
#     elif guess > secret:
#         print("Your guess is not correct... try something smaller")
#     elif guess < secret:
#         print("Your guess is not correct... try something bigger")

#

# Imports y numeros aleatorios
# Siempre los imports se deben hacer al inicio del fichero. (ojo)
import random


secret = random.randint(1, 30)


while True:
    guess = int(input("Guess the secret number (between 1 and 30): "))
    if guess == secret:
        print("You've guessed it - congratulations! It's number " + str(secret))
        break
    elif guess > secret:
        print("Your guess is not correct... try something smaller")
    elif guess < secret:
        print("Your guess is not correct... try something bigger")