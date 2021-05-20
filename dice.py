import random as rnd


class Dice():
    def __init__(self, facesNumber) -> None:
        # Numero di facce (number of faces)
        self.diceFaces = facesNumber
        #risultato del lancio (launch result)
        self.result = 1

    def getLastRoll(self):
        return self.result

    def roll(self):
        rnd.seed()
        launches = []

        # generate random rolls list
        for i in range(1, 5000):
            launches.append(rnd.randint(1, self.diceFaces))

        self.result = launches[rnd.randint(3000, 4999)]

        return self.result



"""
# Example use:
d20 = Dice(20)
print(d20.roll())

"""