from abc import ABC, abstractmethod
from dice import Dice


class Token:
    def __init__(self, type, text, index):
        self.type = type   # Token Type
        self.text = text   # Token textual value
        self.index = index # Token index in expression input

    def toString(self):
        token_name = Tokenizer.tokenNames[self.type]
        return f"<'{self.text}', {token_name}, '{self.index}'>"

    def __str__(self) -> str:
        token_name = Tokenizer.tokenNames[self.type]
        return f"<'{self.text}', {token_name}, '{self.index}'>"
    


class Lexer(ABC):
    EOF = -1
    EOF_TYPE = 1
    char_counter = 0
    character = ""

    def __init__(self, input) -> None:
        self.input = input
        self.character = self.input[self.char_counter]
    
    def consume(self) -> None:
        self.advance()
        self.WS()
    
    # Advance pointer index character to next char
    def advance(self):
        self.char_counter += 1
        if self.char_counter >= len(self.input):
            self.character = self.EOF  
        else:
            self.character = self.input[self.char_counter]

    def match(self, x) -> None:
        if self.character == x:
            self.consume()
        else:
            raise Exception("Excepted " + str(x) + "; was " + str(self.character))

    # Declaration of some abstract methods
    @abstractmethod
    def nextToken(self):
        pass

    @abstractmethod
    def WS(self):
        pass

    @abstractmethod
    def getTokenName(self, tokenType):
        pass



class Tokenizer(Lexer):
    NAME = 2
    DIGIT = 3
    PLUS = 4
    MINUS = 5
    LBRACK = 6
    RBRACK = 7
    ASSIGNEMENT = 8
    COMMA = 9
    tokenNames = ['n/a', '<EOF>', 'NAME', 'DIGIT', 'PLUS', 'MINUS', 'LBRACK', 'RBRACK', 'ASSIGNEMENT', 'COMMA']
    letters = "abcdefghijklmnopqrstuvwxyz"
    numbers = "0123456789"

    def __init__(self, input) -> None:
        super().__init__(input)
    
    def isLETTER(self) -> bool:
        if self.character in self.letters or self.character in self.letters.upper():
            return True
        else:
            return False

    def isNUMBER(self) -> bool:
        if str(self.character) in str(self.numbers):
            return True
        else:
            return False

    def getTokenName(self, x):
        return super().getTokenName(x)

    def nextToken(self) -> Token:
        while self.character != self.EOF:
            if self.character in [' ', '\t', '\n', '\r']:
                self.WS()
            elif self.character == ',':
                self.consume()
                return Token(self.COMMA, ',', self.char_counter - 1)
            elif self.character == '+':
                self.consume()
                return Token(self.PLUS, '+', self.char_counter - 1)
            elif self.character == '-':
                self.consume()
                return Token(self.MINUS, '-', self.char_counter - 1)
            elif self.character == '[':
                self.consume()
                return Token(self.LBRACK, '[', self.char_counter - 1)
            elif self.character == ']':
                self.consume()
                return Token(self.RBRACK, ']', self.char_counter - 1)
            elif self.character == '=':
                self.consume()
                return Token(self.ASSIGNEMENT, '=', self.char_counter - 1)
            else:
                if self.isLETTER():
                    return self.Name()
                elif self.isNUMBER():
                    return self.numbersc()
                else:
                    raise Exception("Not valid char " + str(self.character))

        return Token(self.EOF_TYPE, '<EOF>', self.char_counter)

    def Name(self) -> Token:
        buf = ""
        while self.isLETTER():
            buf += self.character
            self.LETTER()
        
        return Token(self.NAME, buf, self.char_counter - len(buf))
    
    def numbersc(self) -> Token:
        buf = ""
        while self.isNUMBER():
            buf += str(self.character)
            self.NUMBER()
        
        return Token(self.DIGIT, buf, self.char_counter - len(buf))
    
    def LETTER(self):
        if self.isLETTER():
            self.consume()
        else:
            raise Exception("Excepted LETTER; was " + str(self.character))

    def NUMBER(self):
        if self.isNUMBER():
            self.consume()
        else:
            raise Exception("Excepted NUMBER; was " + str(self.character))

    def WS(self):
        while self.character in [' ', '\t', '\n', '\r']:
            self.advance()



class TokenTester():
    def __init__(self, input_string) -> None:
        self.lexer = Tokenizer(input_string)
        self.tk = self.lexer.nextToken()
        self.tokens = []
        self.listing()

    def listing(self):
        self.tokens.append(self.tk)

        while self.tk.type != Lexer.EOF_TYPE:
            self.tk = self.lexer.nextToken()
            self.tokens.append(self.tk)
    
    def getAllTokens(self):
        return self.tokens
    
    def getToken(self, index_of_token):
        if index_of_token < len(self.tokens):
            return self.tokens[index_of_token]
        else:
            raise Exception("Index out of tokens list")

    def printAllTokens(self):
        for token in self.tokens:
            print(f"Type: <{token.type}>, Value: '{token.text}', index: {token.index}")
    
    def printToken(self, index_of_token):
        if index_of_token < len(self.tokens):
            token = self.tokens[index_of_token]
            print(f"Type: <{token.type}>, Value: '{token.text}', index: {token.index}")
        else:
            raise Exception("Index out of tokens list")



class Parser(ABC):
    def __init__(self, input) -> None:
        self.input = input
        self.lookahead = []
        self.k = 2
        self.p = 0
        self.error_msg = ""

        for i in range(1, self.k + 1):
            self.lookahead_buffer()

    def lookahead_buffer(self) -> None:
        token = self.input.nextToken()
        self.lookahead.append(token)
        self.p = (self.p + 1) % self.k

    def consume(self) -> None:
        token = self.input.nextToken()
        self.lookahead[self.p] = token
        self.p = (self.p + 1) % self.k
        
    def LT(self, i) -> Token:
        return self.lookahead[(self.p + i - 1) % self.k]
    
    def LA(self, i):
        return self.LT(i).type
    
    def match(self, x):
        if self.LA(1) == x:
            self.consume()
        else:
            raise Exception("Excepted " + self.input.getTokenName(x) + "; was " + self.LT(1).toString())
            


class ExpressionParser(Parser):
    def __init__(self, input) -> None:
        super().__init__(input)
        self.elema = ""
        self.elemb = ""
        self.total = 0
        self.expression_list = []

    def list(self):
        self.match(Tokenizer.LBRACK)
        print("*** START Parsing ***")
        self.elements()
        self.match(Tokenizer.RBRACK)
        print("*** END Parsing ***")      

    def elements(self):
        self.element()

        while self.LA(1) == Tokenizer.PLUS or self.LA(1) == Tokenizer.MINUS:
            if self.LA(1) == Tokenizer.PLUS:
                print("  -PLUS")
                self.expression_list.append(['+'])
                self.match(Tokenizer.PLUS)
            elif self.LA(1) == Tokenizer.MINUS:
                print("  -MINUS")
                self.expression_list.append(['-'])
                self.match(Tokenizer.MINUS)

            self.element()
    
    def element(self):
        if self.LA(1) == Tokenizer.NAME and self.LA(2) == Tokenizer.DIGIT:
            self.match(Tokenizer.NAME)
            self.elema = '1'
            self.elemb = self.lookahead[self.p].text
            self.match(Tokenizer.DIGIT)
            print(f"  -Roll {self.elema}d{self.elemb}")
            self.expression_list.append([self.elema, self.elemb])    
        elif self.LA(1) == Tokenizer.DIGIT and self.LA(2) == Tokenizer.NAME:
            self.elema = self.lookahead[self.p].text
            self.match(Tokenizer.DIGIT)
            self.match(Tokenizer.NAME)
            self.elemb = self.lookahead[self.p].text
            self.match(Tokenizer.DIGIT)
            print(f"  -Roll {self.elema}d{self.elemb}")
            self.expression_list.append([self.elema, self.elemb])
        elif self.LA(1) == Tokenizer.DIGIT:
            self.elema = self.lookahead[self.p].text
            self.match(Tokenizer.DIGIT)
            print(f"  -Number {self.elema}")
            self.expression_list.append([self.elema])
        elif self.LA(1) == Tokenizer.LBRACK:
            self.list()
        else:
            raise Exception("Excepted NAME or LIST; was " + self.LT(1).toString())
    

    def perform_rolls(self):
        operation = ''

        for tk in self.expression_list:
            if len(tk) > 1:
                self.dice_roll(tk)
            elif '+' in tk or '-' in tk:
                operation = tk[0]
            else:
                if operation == '+':
                    self.total += int(tk[0])
                else:
                    self.total -= int(tk[0])
        
        print(f"\nExpression: {self.expression_list}")
        print(f"Total: {self.total}")

    
    def dice_roll(self, dado):
        d3 = Dice(3)
        d4 = Dice(4)
        d6 = Dice(6)
        d8 = Dice(8)
        d10 = Dice(10)
        d12 = Dice(12)
        d20 = Dice(20)
        d100 = Dice(100)

        if dado[1] == '3':
            self.total += d3.multiRoll(int(dado[0]))
        elif dado[1] == '4':
            self.total += d4.multiRoll(int(dado[0]))
        elif dado[1] == '6':
            self.total += d6.multiRoll(int(dado[0]))
        elif dado[1] == '8':
            self.total += d8.multiRoll(int(dado[0]))
        elif dado[1] == '10':
            self.total += d10.multiRoll(int(dado[0]))
        elif dado[1] == '12':
            self.total += d12.multiRoll(int(dado[0]))
        elif dado[1] == '20':
            self.total += d20.multiRoll(int(dado[0]))
        elif dado[1] == '100':
            self.total += d100.multiRoll(int(dado[0]))
