# FL - OOP IN PYTHON - RPI FOUNDATION
# OOP version of the Knock-Knock program
# knock.py - The class definition for the Knock Knock Program
# Rich Park 2019-03-01

from random import choice

class Knock():

    # Create a constructor with an attribute
    def __init__(self):
        self.knock_list = None
        
    # A method to SET the list of the Knock Knock joke content:
    def set_knockList(self, knock_pair_matrix):
        self.knock_list = knock_pair_matrix
        
    # A method to GET a random intro/punchline pair for Knock Knock
    def get_jokePair(self):
        joke_pair = (self.knock_list)
        return choice(joke_pair)
