from helpers import display_board, check_turn, check_win
import os
spots = {1 : '1', 2 : '2', 3 : '3', 4 : '4', 5 : '5', 6 : '6', 7 : '7', 8 : '8', 9 : '9'}

playing = True
complete = False
turn = 0
prev_turn = -1

while playing:
    os.system('cls' if os.name == 'nt' else 'clear')
    display_board(spots)
    if prev_turn == turn:
        print("invalid spot, please pick again")
    prev_turn = turn
    print("Player " + str((turn % 2) + 1 ) + "'s turn: Pick your spot or press q to quit")
    choice = input("Enter your choice: ")
    if str.isdigit(choice) and int(choice) in spots:
        if not spots[int(choice)] in {"X", "O"}:
            #update the board if valid input
            turn += 1
            spots[int(choice)] = check_turn(turn)
    elif choice == 'q':
        playing = False
    if check_win(spots): playing, complete = False, True
    if turn > 8:
        playing = False
os.system('cls' if os.name == 'nt' else 'clear')
display_board(spots)

if complete:
    print(check_turn(turn) + " wins")
else:
    print("Draw")
