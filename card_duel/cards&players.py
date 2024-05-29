import random

class Card:
    def __init__(self):
        self.health = random.randint(1, 9)
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
        self.learning_rate = 0.6
        self.discount = 0.7
        self.epsilon = 0.1
        self.next_state = None
        self.next_action = None
    
    def actions(self, state, board):
        empty_positions = [i for i, pos in enumerate(board[3:], start=3) if pos is None]
        if not empty_positions:
            return random.choice(range(3, 6)), random.choice(range(3))        
        if state not in self.q_table or random.random() < self.epsilon:
            return random.choice(empty_positions), random.choice(range(3))
        else:
            return max(self.q_table[state], key = self.q_table[state].get)
    
    def update_qtable(self, reward, state):
        if self.next_state is not None and self.next_action is not None:
            if self.next_state not in self.q_table:
                self.q_table[self.next_state] = {}
            if state not in self.q_table:
                self.q_table[state] = {}
            old_value = self.q_table[self.next_state].get(self.next_action, 0)
            next_max = max(self.q_table[state].values()) if self.q_table[state] else 0
            new_value = (1 - self.learning_rate) * old_value + self.learning_rate * (reward + self.discount * next_max)
            self.q_table[self.next_state][self.next_action] = new_value

    def rewards(self, player, opponent):
        reward = 0
        reward += len(opponent.live_cards) * -1
        reward += len(player.live_cards) * -1
        if len(player.live_cards) > len(opponent.live_cards):
            reward += 10
        if len(player.live_cards) >= 5:
            reward += 50
        return reward
    
class Game:
    def __init__(self, player1, player2):
        self.players = [player1, player2]
        self.board = [None] * 6

    def play_round(self):
        for player in self.players:
            player.draw_cards()
            for _ in range(3):
                if player.cards and None in self.board:
                    if player.is_ai:
                        state = tuple(card.health for card in player.cards) + tuple(card.health if card else 0 for card in self.board)
                        action = player.ai.actions(state, self.board)
                        position, card_numbers = action
                        opponent = self.players[0] if player.number == "player 2" else self.players[1]
                        reward = player.ai.rewards(player, opponent)
                        player.ai.update_qtable(reward, state)
                        player.ai.next_state = state
                        player.ai.next_action = action
                    else:
                        print(f"{player.number}, here are your cards:")
                        for i, card in enumerate(player.cards):
                            print(f"card {i}: health = {card.health}, attack = {card.attack}")
                        print("the board:")
                        for i, card in enumerate(self.board):
                            if card:
                                print(f"position {i}: card with health = {card.health}, attack = {card.attack}")
                            else:
                                print(f"position {i}: empty")
                        card_numbers = int(input("enter the card number: "))
                        position = int(input("enter the position number to place the card(0. 1, or 2)"))
                    if self.board[position] is None:
                        position, card = player.play_card(card_numbers, position)
                        self.board[position] = card
            self.resolve_round()
                    
    def resolve_round(self):
        for i in range(3):
            if self.board[i]:
                opponent_index = (i + 1) % 3
                if self.board[opponent_index]:
                    self.board[i].health -= self.board[opponent_index].attack
                    if self.board[i].health <= 0:
                        self.board[i] = None
        for i in range(3):
            if self.board[i]:
                self.players[i % 2].live_cards.append(self.board[i])
                self.board[i] = None

    def end_game(self):
        while len(self.players[0].live_cards) < 5 and len(self.players[1].live_cards) < 5:
            self.play_round()
        for player in self.players:
            print(f"{player.number} has {len(player.live_cards)} surviving cards")

# main:
player1 = Player("player 1")
player2 = Player("player 2")
game = Game(player1, player2)
game.end_game()