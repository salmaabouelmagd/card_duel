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

class Qlearning:
    def __init__(self):
        self.q_table = {}
        self.learning_rate = 0.1
        self.discount = 0.9
        self.epsilon = 0.1
    
    def actions(self, state, board):
        empty_positions = [i for i, pos in enumerate(board) if pos is None]
        if not empty_positions:
            return random.choice(empty_positions), random.choice(random(len(state)))
        else:
            return max(self.q_table[state], key = self.q_table[state].get)
    
    def update_table(self, state, action, reward, next_state):
        if state not in self.q_table:
            self.q_table[state] = {}
        if next_state not in self.q_table:
            self.q_table[next_state] = {}
        old_value = self.q_table[state].get(action, 0)
        next_max = max(self.q_table[next_state].values()) if self.q_table[next_state] else 0
        new_value = (1 - self.learning_rate) * old_value + self.learning_rate * (reward + self.discount * next_max)
        self.q_table[state][action] = new_value