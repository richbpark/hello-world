# FL - OOP IN PYTHON - RPI FOUNDATION
# OOP version of the Knock-Knock program
# knockOOP.py - The main Knock Knock Program
# Rich Park 2019-03-01

from knock import Knock

# Matrix for the intro and punchline for every Knock-Knock joke.
knock_pair_matrix = [['Atch', 'Sounds like you’ve got a cold!'], \
                     ['Kanga', 'Actually, its Kanagroo!'], \
                     ['Ozzie', 'Ozzie you later!'], \
                     ['Voodoo', 'Voodoo you think you are?' ], \
                     ['Mikey', 'My key doesn\'t work, will you let me in.']]

# Instantiate (create) a Knock object named 'knockList'
knockList = Knock()
knockList.set_knockList(knock_pair_matrix)

joke = knockList.get_jokePair()

intro = (joke[0])
punchline = (joke[1])

def main(): # Define a main program loop for better structure
    print("Knock knock")
    print("Who's there")
    print(intro + '!')
    print(intro + " who?")
    print(punchline)
    
main() # Tell a knock knock joke