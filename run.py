import random
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

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


def place_battleship(size):
    ship_row = random.randint(0, size - 1)
    ship_col = random.randint(0, size - 1)
    return ship_row, ship_col

# Section 3: Get player's guess
# ------------------------------
# Function to get the players guess for the battleship's location


def get_player_guess(size):
    while True:
        try:
            # Ask the player to enter the row and column numbers
            guess_row = int(input(Fore.YELLOW + f"Guess Row (0-{size-1}): "))
            guess_col = int(input(Fore.YELLOW + f"Guess Column(0-{size-1}): "))
            # Ensure the guess is within the valid range
            if 0 <= guess_row < size and 0 <= guess_col < size:
                return guess_row, guess_col
            else:
                print(Fore.RED + "Oops, that's not even close. Try again.")
        except ValueError:
            print(Fore.RED + "Please enter a valid number.")

# Section 4: Game Rules and Difficulty Selection
# ----------------------------------------------


# Function to display the game rules
def display_rules():
    print(Fore.CYAN + Style.BRIGHT + "Welcome to Battleship!")
    print(Fore.CYAN + "\nGame Rules:")
    print(Fore.CYAN + "1. A battleship is hidden somewhere on the board.")
    print(Fore.CYAN + "2. The board size and number of turns"
          "depend on the difficulty level you choose.")
    print(Fore.CYAN + "3. Your goal is to guess the location of the"
          "battleship within the allowed number of turns.")
    print(Fore.CYAN + "4. Enter the row and column numbers to make a guess.")
    print(Fore.CYAN + "5. If you guess correctly, you win!"
          "If you run out of turns, the game is over.")
    print(Fore.CYAN + "\nGood luck!\n")

# Function to choose the game difficulty


def choose_difficulty():
    while True:
        print(Fore.GREEN + "Choose a difficulty level:")
        print(Fore.GREEN + "1. Easy (5x5 grid, 10 turns)")
        print(Fore.GREEN + "2. Medium (7x7 grid, 7 turns)")
        print(Fore.GREEN + "3. Hard (10x10 grid, 5 turns)")
        choice = input(Fore.YELLOW + "Enter 1, 2, or 3: ")

        if choice == '1':
            return 5, 10
        elif choice == '2':
            return 7, 7
        elif choice == '3':
            return 10, 5
        else:
            print(Fore.RED + "Invalid choice. Please select 1, 2, or 3.")

# Section 5: Main game loop
# -------------------------
# Function to play the game


def play_game():
    # Display the game rules
    display_rules()
    # Choose difficulty level
    board_size, max_turns = choose_difficulty()

    # Create the board and place the battleship
    board = create_board(board_size)
    ship_row, ship_col = place_battleship(board_size)
    # The player has a certain number of turns based on difficulty
    for turn in range(max_turns):
        print(Fore.MAGENTA + f"\nTurn {turn + 1} of {max_turns}")
        # Print the current state of the board
        print_board(board)
        # Get the player's guess
        guess_row, guess_col = get_player_guess(board_size)
        # Check if the guess is correct
        if guess_row == ship_row and guess_col == ship_col:
            print(Fore.GREEN + Style.BRIGHT + "You sunk my battleship!")
            break
        else:
            # If the player has already guessed this spot, let them know
            if board[guess_row][guess_col] == "X":
                print(Fore.RED + "You already guessed that. Try again.")
            else:
                # Mark the missed guess on the board
                print(Fore.BLUE + "You missed my battleship!")
                board[guess_row][guess_col] = "X"
        # If it's the last turn, reveal the location of the battleship
        if turn == max_turns - 1:
            print(Fore.RED + "\nGame Over")
            print(Fore.RED + f"The battleship was at ({ship_row}, {ship_col})")
            print_board(board)

# Section 6: Start the game
# -------------------------
# Call the function to start the game


if __name__ == "__main__":
    play_game()
