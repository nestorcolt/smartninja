from curso_python.clase_005 import helpers
import math
import importlib

importlib.reload(helpers)
# A new comment
#############################################################################################
# Functions and re-usability

helpers.say_hello(name="Nestor Colt")


#############################################################################################
# Structure or syntax of a function

def add_operation(a=0, b=5):
    result = a + b
    return result


my_result = add_operation(25, 45)
# print(my_result)
#############################################################################################
# tip math module
print(math.pow(2, 5))
