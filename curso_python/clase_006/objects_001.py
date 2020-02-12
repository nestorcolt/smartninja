class BasketballPlayer:

    def __init__(self, first_name, last_name, height_cm, weight_kg, points, rebounds, assists):
        # print("Init method called from {}".format(self.__class__.__name__))

        self.first_name = first_name
        self.last_name = last_name
        self.height_cm = height_cm
        self.weight_kg = weight_kg
        self.points = points
        self.rebounds = rebounds
        self.assists = assists

    def weight_to_lbs(self):
        pounds = self.weight_kg * 2.20462262
        return pounds


#############################################################################################
message = """
        Player name: {}
        Last name: {}
        Rebounds: {}
        """

lebron = BasketballPlayer(first_name="Lebron",
                          last_name="James",
                          height_cm=203,
                          weight_kg=113,
                          points=27.2,
                          rebounds=7.4,
                          assists=7.2)

kev_dur = BasketballPlayer(first_name="Kevin",
                           last_name="Durant",
                           height_cm=210,
                           weight_kg=108,
                           points=27.2,
                           rebounds=7.1,
                           assists=4)

#############################################################################################
# print(message.format(lebron.first_name, lebron.last_name, lebron.rebounds))
# print()
# print(message.format(kev_dur.first_name, kev_dur.last_name, kev_dur.rebounds))

#############################################################################################
# OBJECTS VS DICTIONARY
lebron_dict = {"first_name": "Lebron",
               "last_name": "James",
               "height_cm": 203,
               "weight_kg": 113,
               "points": 27.2,
               "rebounds": 7.4,
               "assists": 7.2}


# print(lebron_dict["first_name"])
# print(lebron_dict["height_cm"])

#############################################################################################
# CLASS METHODS
# print("The conversion of the total weight from kilograms to pounds from {} is: {} pounds".format(lebron.first_name,
#                                                                                                  lebron.weight_to_lbs()))
#

#############################################################################################

class FootballPlayer:
    def __init__(self, first_name, last_name, height_cm, weight_kg, goals, yellow_cards, red_cards):
        self.first_name = first_name
        self.last_name = last_name
        self.height_cm = height_cm
        self.weight_kg = weight_kg
        self.goals = goals
        self.yellow_cards = yellow_cards
        self.red_cards = red_cards


ronaldo = FootballPlayer(first_name="Cristiano", last_name="Ronaldo", height_cm=184, weight_kg=79, goals=586,
                         yellow_cards=95, red_cards=11)

messi = FootballPlayer(first_name="Lionel", last_name="Messi", height_cm=170, weight_kg=67, goals=575, yellow_cards=67,
                       red_cards=0)

print(ronaldo.first_name)
print(ronaldo.goals)
print(messi.first_name)
print(messi.goals)
