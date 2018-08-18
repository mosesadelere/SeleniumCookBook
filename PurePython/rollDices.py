from random import randint


class Roll():
    def __init__(self):
        #self.sides = input("Input number of sides: ")
        self.volume = []
        self.volume2 = []
        #self.outcome = outcome

    def sixSided(self):
        self.sides = input("input number of sides: ")
        for outcome in range(10):
            value = randint(1, int(self.sides))
            self.volume.append(value)
        print(self.volume)
        outcome = [randint(1, int(self.sides)) for value in range(10)]
        print(outcome)

    def tenSided(self):
        self.sides = input("input number of sides: ")
        for outcome in range(10):
            value = randint(1, int(self.sides))
            self.volume2.append(value)
        outcome = [randint(1, int(self.sides)) for value in range(10)]
        # for i in range(len(outcome)):
        #     for j in range([i + 1], len(outcome)):
        #         if outcome[i] == outcome[j]:
        #             outcome[i] = randint(1, int(self.sides))
        print(self.volume2)
        print(outcome)

myDices = Roll()
myDices.sixSided()
myDices.tenSided()