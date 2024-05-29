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
        if is_ai:
            self.ai = Qlearning()

    def draw_cards(self):
        self.cards = [Card() for _ in range(3)]

    def play_card(self, i, pos):
        card = self.cards.pop(i)
        return pos, card

class Qlearning:
    def __init__(self):
        self.q_table = {}
        self.learning_rate = 0.1
        self.discount = 0.9
        self.epsilon = 0.1
        self.last_state = None
        self.last_action = None
    
    def actions(self, state, board):
        empty_positions = [i for i, pos in enumerate(board) if pos is None]
        if not empty_positions:
            return random.choice(range(3)), random.choice(range(len(state)))        
        if state not in self.q_table or random.random() < self.epsilon:
            return random.choice(empty_positions), random.choice(range(len(state)))
        else:
            return max(self.q_table[state], key = self.q_table[state].get)
    
    def update_qtable(self, state, action, reward, next_state):
        if state not in self.q_table:
            self.q_table[state] = {}
        if next_state not in self.q_table:
            self.q_table[next_state] = {}
        old_value = self.q_table[state].get(action, 0)
        next_max = max(self.q_table[next_state].values()) if self.q_table[next_state] else 0
        new_value = (1 - self.learning_rate) * old_value + self.learning_rate * (reward + self.discount * next_max)
        self.q_table[state][action] = new_value

    def rewards(self, player, opponent):
        reward = 0
        reward += len(opponent.live_cards) * -1
        reward += len(player.live_cards) * -1
        if len(player.live_cards) > len(opponent.live_cards):
            reward += 10
        if len(player.live_cards) >= 5:
            reward += 50

        return reward