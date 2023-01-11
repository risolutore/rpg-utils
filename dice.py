import random as rnd


class Dice():
    def __init__(self, facesNumber) -> None:
        # Numero di facce (number of faces)
        self.diceFaces = facesNumber
        #risultato del lancio (launch result)
        self.result = 0

    def lastRoll(self):
        # Ritorna ultimo risultato (return last result)
        return self.result

    def roll(self) -> int:
        rnd.seed()
        lancio = 0
        launches = []

        # Generate random rolls list
        for i in range(1, 5000):
            launches.append(rnd.randint(1, self.diceFaces))

        # Get random result from list of launces
        lancio = launches[rnd.randint(3000, 4999)]
        self.result = lancio
        launches = []
        # return the result as  dice roll
        return lancio

    def multiRoll(self, launces) -> int:
        self.result = 0
        lanci = ''
        lancio = 0

        for i in range(0, launces):
            lancio = self.roll()
            lanci += f'{lancio}+'
            self.result += lancio
        
        return lanci[0:-1]

"""
# Example use:

# Single Roll
d20 = Dice(20)
print(d20.roll())

# Multi-Roll
thrwos = 3
d10 = Dice(10)
print(d10.multiRoll(throws))
"""
