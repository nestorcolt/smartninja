import datetime
import json
import random


#############################################################################################

class Engine:
    def __init__(self):
        self.secret_number = 22
        self.attempts = 0
        self.statistics = []

    def statistics_model(self, attempts, date):
        fails = attempts - 1
        #
        model = {
            "attempts": attempts,
            "date": date,
            "fails": fails,
        }
        return model

    def play(self):
        while True:
            guess = int(input("Guess the secret number (between 1 and 30): "))
            self.attempts += 1

            if guess == self.secret_number:
                print("You've guessed it - congratulations! It's number " + str(self.secret_number))
                self.statistics.append(self.statistics_model(attempts=self.attempts, date=self.get_current_time()))
                break

            elif guess > self.secret_number:
                print("Your guess is not correct... try something smaller")

            elif guess < self.secret_number:
                print("Your guess is not correct... try something bigger")

    def get_secret_number(self):
        self.secret_number = random.randint(1, 50)

    def get_current_time(self):
        current_time = datetime.datetime.now()
        result = current_time.strftime("%m/%d/%y, %H:%M:%S")
        return result


#############################################################################################
# run
if __name__ == '__main__':
    game = Engine()
    game.play()

# for item in my_info:
#     for name, data in item.items():
#         print(name, data)
#
# with open("score.txt", mode='r') as score_file:
#     store_data = int(score_file.read())
#
# if attempts < store_data:
#     with open("score.txt", mode='w') as score_file:
#         score_file.write(str(attempts))
#         store_data = attempts
