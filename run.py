import random

# Section 1: Set up the game board
# -------------------------------
# Function to create the game board


def create_board(size):
    return [['O'] * size for _ in range(size)]

# Function to print game board


def print_board(board):
    for row in board:
        print(' '.join(row))

# Section 2: Place the battleship
# -------------------------------
# Function to randomly place the battleship on the board


def place_battleship():
    ship_row = random.randint(0, size - 1)
    ship_col = random.randint(0, size - 1)
    return ship_row, ship_col

# Section 3: Get player's guess
# ------------------------------
# Function to get the players guess for the battleship's location


def get_player_guess():
    while True:
        try:
            # Ask the player to enter the row and column numbers
            guess_row = int(input(f"Guess Row (0-{size-1}): "))
            guess_col = int(input(f"Guess Column (0-{size-1}): "))
            # Ensure the guess is within the valid range
            if 0 <= guess_row < size and 0 <= guess_col < size:
                return guess_row, guess_col
            else:
                print("Oops, that's not even in the ocean. Try again.")
        except ValueError:
            print("Please enter a valid number.")


# Section 4: Main game loop
# -------------------------
# Function to play the game

def play_game():
    print("Welcome to Battleship!")
    board = generate_board_size(6)
    # Place the battleship on the board
    ship_row, ship_col = place_battleship()
    # The player has 5 turns to guess the location of the battleship
    for turn in range(5):
        print(f"\nTurn {turn + 1}")
        # Print the current state of the board
        print_board(board)

        # Get the player's guess
        guess_row, guess_col = get_player_guess()

        # Check if the guess is correct
        if guess_row == ship_row and guess_col == ship_col:
            print("Congratulations! You sunk my battleship!")
            break
        else:
            # If the player has already guessed this spot, let them know
            if board[guess_row][guess_col] == "X":
                print("You already guessed that. Try again.")
            else:
                # Mark the missed guess on the board
                print("You missed my battleship!")
                board[guess_row][guess_col] = "X"
            # If it's the last turn, reveal the location of the battleship
        if turn == 4:
            print("\nGame Over")
            print(f"The battleship was at ({ship_row}, {ship_col})")
            print_board(board)

# Section 5: Start the game
# -------------------------
# Call the function to start the game


if __name__ == "__main__":
    play_game()
