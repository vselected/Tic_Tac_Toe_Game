
# Function that will create a board
def display_board(board):
    print('\n' * 100)

    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('-----------')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('-----------')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])

# Function that will take player input
def player_input():
    pass

# Function that will start a game
def game_start():
    pass

test_board = ['#','X','O','X','O','X','O','X','O','X']
display_board(test_board)