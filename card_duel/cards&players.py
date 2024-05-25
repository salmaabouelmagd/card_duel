import random

class Card:
    def __init__(self):
        self. health = random.randint(1, 9)
        self.attack = random.randint(1, 9)

class Player:
    def __init__(self, number, is_ai=False):
        self.number = number
        self.cards = []
        self.live_cards = []
        self.is_ai = is_ai