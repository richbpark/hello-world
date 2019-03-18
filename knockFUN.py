# FL - OOP IN PYTHON - RPI FOUNDATION
# Function version of the Knock-Knock program
# Rich Park 2019-02-26

from random import choice

# Matrix for the intro and punchline for every Knock Knock joke.
knockPair = [['Atch', 'Sounds like you’ve got a cold!'], \
             ['Kanga', 'Actually, its Kanagroo!'], \
             ['Ozzie', 'Ozzie you later!'], \
             ['Tank', 'Tank you are welcome!'],
             ['Voodoo', 'Voodoo you think you are?' ], \
             ['Mikey', 'My key doesn\'t work, will you let me in.']]

# Using the choice method from Python's built-in random class
#  choose an intro/punchline pair
jokePair = choice(knockPair)


# The knock function breaks out the joke pair elements
#  puts them into the intro and punchline variables for clarity
def knock(joke):
    intro = (joke[0])
    punchline = joke[1]
    
    print("Knock knock")
    print("Who's there")
    print(intro + '!')
    print(intro + " who?")
    print(punchline)
    
    
def main(): # Define a main program loop for better structure
    knock(jokePair)
    
    
main() # Tell a knock knock joke
