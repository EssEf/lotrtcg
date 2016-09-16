import random

class Deck:
    def __init__(self, cards=None, visible=False):
        if cards:
            self.cards = cards
        else:
            self.cards = []
        self.visible = visible
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self):
        if len(self.cards) == 0:
            return None
        return self.cards.pop(0)

    def add(self, card):
        self.cards.append(card)

    def remove(self, card):
        self.cards.remove(card)

    def __repr__(self):
        if self.visible:
            return '[' + ']['.join(repr(card) for card in self.cards) + ']'
        else:
            return '[' + str(len(self.cards)) + ']'

    def __getitem__(self, k):
        return self.cards[k]

    def __setitem__(self, k, v):
        self.cards[k] = v

    def __iter__(self):
        i = 0
        while i < len(self.cards):
            yield self.cards[i]
            i += 1
