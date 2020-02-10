import time

# Class 2 Re-cap
start = time.time()

customer_names = ["pedro", "pablo", "javier", "jhon"]
customer_surnames = ["ramirez", "casanovas", "perez", "doe"]

for index in range(1000):
    # print(index)
    pass

stop = time.time()

"""
Documentation:

"""

#############################################################################################
import random

# secret = random.randint(1, 30)
secret = 22
attempts = 0


while True:
    guess = int(input("Guess the secret number (between 1 and 30): "))
    attempts += 1

    if guess == secret:
        print("You've guessed it - congratulations! It's number " + str(secret))
        break

    elif guess > secret:
        print("Your guess is not correct... try something smaller")
    elif guess < secret:
        print("Your guess is not correct... try something bigger")


with open("score.txt", mode='r') as score_file:
    store_data = int(score_file.read())

if attempts < store_data:
    with open("score.txt", mode='w') as score_file:
        score_file.write(str(attempts))
        store_data = attempts

print("Top score: " + str(store_data))

#############################################################################################
print("Total execution time: ", stop - start)
