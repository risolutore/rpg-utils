# rpg-utils
python scripts for useful utils for rpg games.
I'm working on a Web app for Role Players in Django and i need a lot of tools to make the site functional.

## Dice 
is  a simple class created for roll dice, it can return one roll or more roll at same time. 
The roll method create a list of 5000 dice rolls and get one result from 3999 to 4999 - one of last 1000 rolls for more accurate randome result,example usage:

### Ecxample 1
'''
from dice import Dice

d20 = Dice(20)
print(f"Roll 1d20: {d20.roll()}")
'''
### Ecxample 2
'''
from dice import Dice

d10 = Dice(10)
throws = 3
print(f"Roll {throws}d10; {d10.multiRoll(throws)}")
'''




