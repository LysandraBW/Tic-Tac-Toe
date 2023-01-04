from Player import Player
from Board import Board
from random import randint

# Initializing
board = Board()
players = [Player("H", 0), Player("R", 1)]
player_turn = randint(0, 1)

# Introduction
print("GAME\nTic-Tac-Toe\nH = Human, R = Robot")
board.display()

# Game Loop
while True:
    space_index = int(input("Player " + players[player_turn].get_symbol() + " Turn\nEnter Space: "))

    if not board.add_move(players[player_turn], space_index):
        continue

    board.display()

    if board.update(*players):
        break

    player_turn = 0 if player_turn == 1 else 1

# Fetching Winner (if any)
results = board.check_win()

# Displaying Results
if results[0]:
    print("PLAYER " + players[results[1]].get_symbol() + " WON.\nGAME OVER!")
if board.check_tie():
    print("TIE\nGAME OVER!")