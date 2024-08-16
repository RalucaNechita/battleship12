import random

# Section 1: Set up the game board
# -------------------------------
# Define the size of the board and create a 5x5 grid filled with 'O'
board_size = 5
board = [['O'] * board_size for _ in range(board_size)]

# Function to print game board

def print_board(board):
    for row in board:
        print(' '.join(row))