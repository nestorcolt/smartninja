import datetime
import random
import json
import os


#############################################################################################

class Engine:

    def __init__(self):
        self.secret_number = 22
        self.attempts = 0
        self.statistics = []
        self.player = "Jhon"
        self.statistics_filename = "statistics.json"
        self.statistics_path = None

        # Create file path
        self.get_statistics_path()

    def statistics_model(self, player_name, attempts, date):
        fails = attempts - 1
        #
        model = {
            "player": player_name,
            "attempts": attempts,
            "date": date,
            "fails": fails,
        }
        return model

    def get_player_name(self):
        user = input("Hey there, Welcome to guess the secret number!\n\tPlease enter your name: ")
        self.player = user
        print("-----------------------------------------------------------------------------------")

    def play(self):
        # Fetch the current player game
        self.get_player_name()

        # Game loop
        while True:
            guess = int(input("Guess the secret number (between 1 and 30): "))
            self.attempts += 1

            if guess == self.secret_number:
                print("You've guessed it - congratulations! It's number " + str(self.secret_number))
                self.update_statistics()
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

    def save_statistics(self, data=[]):
        data = self.statistics if not data else data
        #
        with open(self.statistics_path, mode='w') as score_file:
            json.dump(data, score_file, ensure_ascii=True, indent=4, separators=[",", ":"])

    def load_statistics(self):
        if not os.path.exists(self.statistics_path):
            return False

        with open(self.statistics_path, mode='r') as score_file:
            store_data = json.load(score_file)
            return store_data

    def get_statistics_path(self):
        current_working_dir = os.getcwd()
        full_statistics_path = os.path.join(current_working_dir, self.statistics_filename)
        self.statistics_path = full_statistics_path

    def create_statistics_data(self):
        model = self.statistics_model(player_name=self.player,
                                      attempts=self.attempts,
                                      date=self.get_current_time())
        return model

    def update_statistics(self):
        data = self.load_statistics()

        if data:
            model = self.create_statistics_data()
            data.append(model)
            self.save_statistics(data)
        else:
            model = self.create_statistics_data()
            self.statistics.append(model)
            # Save
            self.save_statistics()


#############################################################################################
# run
if __name__ == '__main__':
    game = Engine()
    game.play()
    # game.create_statistics_data()
