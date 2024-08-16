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
# Function to get the players guess for the battleship's location


def get_player_guess():
    while True:
        try:
            # Ask the player to enter the row and column numbers
            guess_row = int(input("Guess Row (0-4): "))
            guess_col = int(input("Guess Column (0-4): "))
            # Ensure the guess is within the valid range
            if 0 <= guess_row < board_size and 0 <= guess_col < board_size:
                return guess_row, guess_col
            else:
                print("Oops. Try again.")
        except ValueError:
            print("Please enter a valid number.")


# Section 4: Main game loop
# -------------------------
# Function to play the game

def play_game():
    print("Welcome to Battleship!")
    # Place the battleship on the board
    ship_row, ship_col = place_battleship()
    # The player has 5 turns to guess the location of the battleship
    for turn in range(5):
        print(f"\nTurn {turn + 1}")
        # Print the current state of the board
        print_board(board)