 import os

def display_board(spots):
    board = (f"|{spots[1]}|{spots[2]}|{spots[3]}|\n"
                f"|{spots[4]}|{spots[5]}|{spots[6]}|\n"
                f"|{spots[7]}|{spots[8]}|{spots[9]}|\n")
    print(board)

def check_win(spots):
#checks all 8 winning lines
    wins = [
    (1,2,3), (4,5,6), (7,8,9),
    (1,4,7),(2,5,8), (3,6,9),
    (1,5,9), (3,5,7)
    ]
    for a,b,c in wins:
        if spots[a] == spots[b] == spots[c] and spots[a] in {"X", "O"}:
            return True
    return False


def play ():
    spots = {1 : '1', 2 : '2', 3 : '3', 4 : '4', 5 : '5', 6 : '6', 7 : '7', 8 : '8', 9 : '9'}
    playing = True
    turn = 0
    winner = None

    while playing:
        os.system('cls' if os.name == 'nt' else 'clear')
        display_board(spots)

        current_symbol = 'X' if turn % 2 == 0 else 'O'
        player_number = 1 if turn % 2 == 0 else 2
        print(f"\nPlayer {player_number}'s turn.({current_symbol})")
        choice = input("pick a spot(1-9) or press 'q' to quit: ").strip()

        if choice.lower() == 'q':
            print("\nGame Over")
            return

        #input validation
        if choice.isdigit() and int(choice) in spots:
            spot_num = int(choice)
            if sports[spot_num] not in {"X", "O"}:
                #apply move
                spots[spot_num] = current_symbol

                #check win
                if check_win(spots):
                    winner = current_symbol
                    playing = False
                #check tie
                elif turn == 8:
                    playing = False
                turn += 1
            else:
                input("spot already taken, enter a new spot and try again")
        else:
            input("invalid inpit, enter a new spot and try again")

    os.system('cls' if os.name == 'nt' else 'clear')
    display_board(spots)

    if winner:
        print(f"\nPlayer ({winner} wins!")
    else:
        print("\n It's a tie!")

if __name__ == "__main__":
    play()
