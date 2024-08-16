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

# Section 2: Place the battleship
# -------------------------------
# Function to randomly place the battleship on the board


def place_battleship():
    ship_row = random.randint(0, board_size - 1)
    ship_col = random.randint(0, board_size - 1)
    return ship_row, ship_col

# Section 3: Get player's guess
# ------------------------------
# Function to get the player's guess for the battleship's location


def get_player_guess():
    while True:
        try:
            # Prompt the player to enter the row and column numbers
            guess_row = int(input("Guess Row (0-4): "))
            guess_col = int(input("Guess Column (0-4): "))
            # Ensure the guess is within the valid range
            if 0 <= guess_row < board_size and 0 <= guess_col < board_size:
                return guess_row, guess_col
            else:
                print("Oops, that's not even in the ocean. Try again.")
        except ValueError:
            print("Please enter a valid number.")