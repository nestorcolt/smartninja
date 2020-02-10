# Listas
some_list = [1, 34, 12, 17, 87]
# print(some_list)

another_list = ["tesla", "toyota", "nissan"]
# print(another_list)

mixed_list = [22, 22, "elon", True, "SmartNinja", 3.14, [], {}]

# sort
mixed_list.append(100)
mixed_list.append(22)
mixed_list.append("casa")
mixed_list.insert(2, False)
# some_list.sort()
# some_list.reverse()
# print(some_list)
# some_list.clear()
# print(mixed_list)
# print(mixed_list.count(22))
# print(mixed_list.index(22))

# dictionaries
box = {"height": 20, "width": 45, "length": 30}
result = box.get("patata", False)
# result = box["patata"]
box["patata"] = {0: "muy cara"}
# print(box)

# tweak our game with dics

#############################################################################################
import datetime

current_time = datetime.datetime.now()
secret = 22
attempts = 0
my_info = []

while True:
    guess = int(input("Guess the secret number (between 1 and 30): "))
    attempts += 1

    if guess == secret:
        print("You've guessed it - congratulations! It's number " + str(secret))
        my_info.append({"attempts": attempts,
                        "date": current_time.strftime("%m/%d/%y, %H:%M:%S"),
                        "wrong": attempts - 1})
        break

    elif guess > secret:
        print("Your guess is not correct... try something smaller")
    elif guess < secret:
        print("Your guess is not correct... try something bigger")

for item in my_info:
    for name, data in item.items():
        print(name, data)

with open("score.txt", mode='r') as score_file:
    store_data = int(score_file.read())

if attempts < store_data:
    with open("score.txt", mode='w') as score_file:
        score_file.write(str(attempts))
        store_data = attempts

print("Top score: " + str(store_data))
