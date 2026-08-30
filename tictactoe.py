def display_board(spots):
    board = (f"|{spots[1]}|{spots[2]}|{spots[3]}|\n"
                f"|{spots[4]}|{spots[5]}|{spots[6]}|\n"
                f"|{spots[7]}|{spots[8]}|{spots[9]}|\n")
    print(board)

def check_turn(turn):
    if turn % 2 == 0: return 'O'
    else: return 'X'

def check_win(spots):
    if (spots[1] == spots[2] == spots[3]) \
        or (spots[4] == spots[5] == spots[6]) \
        or (spots[7] == spots[8] == spots[9]):
        return True
    elif (spots [1] == spots[4] == spots [7])\
        or (spots [2] == spots[5] == spots [8])\
        or (spots [3] == spots[6] == spots [9]):
        return True
    elif (spots [1] ==spots[5] == spots [9])\
        or (spots[3] == spots[5] ==spots [7]):
        return True
    else: return False
import os
spots = {1 : '1', 2 : '2', 3 : '3', 4 : '4', 5 : '5', 6 : '6', 7 : '7', 8 : '8', 9 : '9'}

playing = True
complete = False
turn = 0
prev_turn = -1

def player_input(spots, turn, prev_turn):
    """Handles clearing the screen, displaying the board, getting user input,

    and updating the game state for a single turn.

    """
    os.system("cls" if os.name == "nt" else "clear")
    display_board(spots)

    if prev_turn == turn:
        print("invalid spot, please pick again")

    prev_turn = turn
    print(
        "Player "
        + str((turn % 2) + 1)
        + "'s turn: Pick your spot or press q to quit"
    )

    choice = input("Enter your choice: ")

    playing = True
    complete = False

    if str.isdigit(choice) and int(choice) in spots:
        if spots[int(choice)] not in {"X", "O"}:
            # Update the board if valid input
            turn += 1
            spots[int(choice)] = check_turn(turn)
    elif choice == "q":
        playing = False

    if check_win(spots):
        playing, complete = False, True

    if turn > 8:
        playing = False

    return spots, turn, prev_turn, playing, complete
os.system('cls' if os.name == 'nt' else 'clear')
display_board(spots)

if complete:
    print(check_turn(turn) + " wins")
else:
    print("Draw")
