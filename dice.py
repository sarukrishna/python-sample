import random
class Die(object):
    def __init__(self, sides):
        self.sides = sides
        print(self.roll(self.sides))
    def roll(self, sides):
        value = random.randint(1, sides)
        return value

class Deck(object):
    def __init__(self):
        self.shuffle()
        print(self.deal())
        print(self.deal())
    def shuffle(self):
        suites = ["Spades", "Hearts", "Clubs", "Diamonds"]
        ranks = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
        self.card = []
        for suite in suites:
            for rank in ranks:
                self.card.append(rank + " of " + suite)
        random.shuffle(self.card)
    def deal(self):
        return self.card.pop()
card = Deck()