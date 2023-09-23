from diceparser import Tokenizer, ExpressionParser
from dice import Dice

# Dice initial expression
expr = '5d10+2d6+6'

# Need to set the exression like a list
# if none add at the biginnign of the expression string a '['
if expr[0] != '[':
    expr = f"[{expr}"

# i none add at the end of the expression string a ']'
if expr[len(expr) - 1] != ']':
    expr = f"{expr}]"

# now we have:
# expr = '[5d10+2d6+6]'

# now it's time to start parsing
try:
    lexer = Tokenizer(expr)
    parser = ExpressionParser(lexer)
    parser.list()
    parser.perform_rolls()
except Exception:
    print(f"Error: {parser.error_msg}")



