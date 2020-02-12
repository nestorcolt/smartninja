import datetime
import random
import json


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
                self.save_statistics()
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

    def save_statistics(self):
        with open("statistics.txt", mode='w') as score_file:
            score_file.write(str(self.statistics))
            score_file.close()

    def load_statistics(self):
        with open("statistics.txt", mode='r') as score_file:
            store_data = score_file.read()
            return store_data


#############################################################################################
# run
if __name__ == '__main__':
    game = Engine()
    game.play()
    statistics = game.load_statistics()
    print(type(statistics))
    # print(statistics[0])
