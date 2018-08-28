class Cards():
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __str__(self):
        #cardNames = ['Jack', 'Queen', 'King', 'Ace']
        if self.value <= 10:
            return '{} of {}'.format(self.value, self.suit)
        else:
            return '{} of {}'.format(self.value - 11, self.suit)
