Card Duel 

The aim is to make digital version of yugioh or inscryption; where the players get to have 3 (or more) cards each round of the game, which will be 3, but they can only place 3 cards on the board to go against the other player; at the end each round the remaining cards that’s on the board will be put to the side to be counted later. 

About the cards: 

The cards have a random amount of health and attacks between 1 and 9. The cards health decrease with each hit from the enemy If the cards health reaches 0 then the card will be removed from board (complete deleted from existing 😊). 

How is the game going to go: 

Each player has 3(more) card/s each round, and they has a turn to either put 1 (or more) card/s down anywhere on the board or skip their turn (they can’t skip in the first turn) (also the first player to start is the ai), then the cards will fight only the card that in front of it; the round ends when both players don’t have cards to put on the board, at the end of a round the remaining cards that’s on the board will be collected in 2 stacks one for each player that will be counted at the end of the game, to see the winner of the game. 

An example of the game: 

Player 1: (1,3), (6,4), (4,9) 

Player 2: (4,9), (6,3), (7,4) 

Cards 1 and 3 from both players 1 and 2 will be removed and cards 2 health will decrease from (6,4) to (3,4) and from (6,3) to (2,3), then the players either add more cards to the board or skip their turn. 

 

How I will go about it: 

I will make classes for the cards, player, qlearning model, and the game. 

In the cards class, I will just define the health and attack in __init__ function. 

In the player class, I will define the player's number and if the player is an ai or not (I want to make so I can use project later, so I make it a 2 players game), then I will make 2 functions, first one is the draw cards, where players get to be assigned 3 cards each, and second one is the play card, where the player determine the card and the position of that card. 

In the qlearning class, it represents the ai deciding which card to use and where to place it on the board; I will use qtable to store estimated rewards, and maybe I will make the ai use epsilon greedy strategy to choose actions with small probability. 

In the game class, this is the game itself, the functions in here will be about players having rounds (is it the player 1 round or player 2 round), resolving (to see if the card survived or not to be put in the players “live card” array), and playing the game (the game keeps on going until there is a certain amount in one of the players “live card” array (might be 5)).  
