from curso_python.clase_006 import player_manager
import importlib

# Imports
importlib.reload(player_manager)


#############################################################################################
# Basket player model
class BasketballPlayer(player_manager.Player):

    def __init__(self, first_name, last_name, height_cm, weight_kg, points, rebounds, assists):
        super().__init__(first_name=first_name,
                         last_name=last_name,
                         height_cm=height_cm,
                         weight_kg=weight_kg)

        # Properties only for BasketballPlayer
        self.points = points
        self.rebounds = rebounds
        self.assists = assists


#############################################################################################
# Basket player model
class FootballPlayer(player_manager.Player):

    def __init__(self, first_name, last_name, height_cm, weight_kg, goals, yellow_cards, red_cards):
        super().__init__(first_name=first_name,
                         last_name=last_name,
                         height_cm=height_cm,
                         weight_kg=weight_kg)

        # Properties only for BasketballPlayer
        self.goals = goals
        self.yellow_cards = yellow_cards
        self.red_cards = red_cards


#############################################################################################
kev_dur = BasketballPlayer(first_name="Kevin",
                           last_name="Durant",
                           height_cm=210,
                           weight_kg=108,
                           points=27.2,
                           rebounds=7.1,
                           assists=4)

print(kev_dur.last_name)
print(kev_dur.rebounds)
print(kev_dur.weight_to_lbs())

messi = FootballPlayer(first_name="Lionel",
                       last_name="Messi",
                       height_cm=170,
                       weight_kg=67,
                       goals=575,
                       yellow_cards=67,
                       red_cards=0)

print(messi.first_name)
print(messi.goals)
print(messi.weight_to_lbs())
