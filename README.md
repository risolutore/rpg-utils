# rpg-utils
python scripts for useful utils for rpg games.
I'm working on a Web app for Role Players in Django and i need a lot of tools to make the site functional.

## Dice 
is  a simple class created for roll dice, it can return one roll or more roll at same time. 
The roll method create a list of 5000 dice rolls and get one result from 3999 to 4999 - one of last 1000 rolls for more accurate randome result,example usage:

### Ecxample 1
```python
from dice import Dice

d20 = Dice(20)
print(f"Roll 1d20: {d20.roll()}")
```
### Ecxample 2
```python
from dice import Dice

d10 = Dice(10)
throws = 3

print(f"Roll {throws}d10; {d10.multiRoll(throws)}")
```
## DiceParser
are som class definition for parsing dice expression like 'd20+3d10+2d6-5'. There is a lexer Tokenizer class and a parser DiceParser class. I developed this in python with the help of the book of Terence Parr [Language Implementation Patterns](https://pragprog.com/titles/tpdsl/language-implementation-patterns/) - great book.   

### Example usage
```python
from diceparser import Tokenizer, ExpressionParser
from dice import Dice

expression = '[5d10+2d6+6]'

if expr[0] != '[':
    expr = f"[{expr}"

if expr[len(expr) - 1] != ']':
    expr = f"{expr}]"

try:
    lexer = Tokenizer(expr)
    parser = ExpressionParser(lexer)
    parser.list()
    parser.perform_rolls()
except Exception:
    print(f"Error: {parser.error_msg}")
```


