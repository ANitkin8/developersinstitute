import os

def display_board(board):
    print(f"| {board[0][0]} | {board[0][1]} | {board[0][2]} |")
    print(f"| {board[1][0]} | {board[1][1]} | {board[1][2]} |")
    print(f"| {board[2][0]} | {board[2][1]} | {board[2][2]} |")


def player_input(player):
    """Gets row and column input from the player and validates it.

    Accepts 1-9 grid positions for easy typing and converts them to 2D indices.
    """
    mapping = {
        '1': (0, 0), '2': (0, 1), '3': (0, 2),
        '4': (1, 0), '5': (1, 1), '6': (1, 2),
        '7': (2, 0), '8': (2, 1), '9': (2, 2)
    }

    while True:
        choice = input(f"Player {player}, pick a spot (1-9): ").strip()

        if choice in mapping:
            row, col = mapping[choice]
            return row, col
        else:
            print("Invalid input! Please enter a number from 1 to 9.")


def check_win(board, player):
    """Checks if the given player has won horizontally, vertically, or diagonally."""
    # Check Rows
    for row in board:
        if row[0] == row[1] == row[2] == player:
            return True

    # Check Columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == player:
            return True

    # Check Diagonals
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True

    return False


def check_tie(board):
    """Checks if all board spaces are full (no empty spaces left)."""
    for row in board:
        for cell in row:
            if cell == ' ':
                return False
    return True


def play():
    """Main game loop managing board state, turn swapping, and win/tie checks."""
    # Step 1: Represent board as a 2D list initialized with spaces
    board = [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']
    ]

    current_player = 'X'
    game_over = False

    while not game_over:
        os.system('cls' if os.name == 'nt' else 'clear')
        display_board(board)

        # Step 3: Get player move & update board
        row, col = player_input(current_player)

        if board[row][col] == ' ':
            board[row][col] = current_player

            # Step 4: Check for a winner
            if check_win(board, current_player):
                os.system('cls' if os.name == 'nt' else 'clear')
                display_board(board)
                print(f"\nPlayer {current_player} wins!")
                game_over = True
            # Step 5: Check for a tie
            elif check_tie(board):
                os.system('cls' if os.name == 'nt' else 'clear')
                display_board(board)
                print("\nIt's a tie!")
                game_over = True
            else:
                # Switch player
                current_player = 'O' if current_player == 'X' else 'X'
        else:
            input("Spot already taken! Press Enter to try again...")


if __name__ == "__main__":
    play()
