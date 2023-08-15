# Design the game board as a 3x3 list of lists
board = [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']
]

# Create a function to print the game board to the console
def print_board(board):
    for row in board:
        print('|'.join(row))
        print('-' * 5)

# Create a function to handle player moves
def handle_player_move():
    row = int(input("Enter the row (0, 1, 2): "))
    col = int(input("Enter the column (0, 1, 2): "))
    return row, col

def make_move(board, row, col, player_symbol):
    if board[row][col] == ' ':
        board[row][col] = player_symbol
        return True
    else:
        print("That cell is already taken. Pick another cell")
        return False

# Create a function to check for a win
def check_for_win(board, player_symbol):
    for i in range(3):
        if all(board[i][j] == player_symbol for j in range(3)) or \
           all(board[j][i] == player_symbol for j in range(3)):
            return True
    if all(board[i][i] == player_symbol for i in range(3)) or \
       all(board[i][2 - i] == player_symbol for i in range(3)):
        return True
    return False

# Create a function to check for a tie
def check_for_tie(board):
    return all(board[i][j] != ' ' for i in range(3) for j in range(3))


# Create a main game loop that alternates between the two players
def main():
    player_turn = 'X'
    while True:
        print_board(board)
        print(f"Player {player_turn}'s turn.")
        row, col = handle_player_move()
        if make_move(board, row, col, player_turn):
            if check_for_win(board, player_turn):
                print_board(board)
                print(f"Player {player_turn} wins!")
                break
            elif check_for_tie(board):
                print_board(board)
                print("It's a draw!")
                break
            player_turn = 'O' if player_turn == 'X' else 'X'

if __name__ == "__main__":
    main()
