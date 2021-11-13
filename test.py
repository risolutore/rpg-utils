from diceparser import Tokenizer, ExpressionParser
from dice import Dice


expr = '5d10+2d6+6'

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



