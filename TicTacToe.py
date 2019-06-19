ROW_NUMBER = 3
COLUMN_NUMBER = 3
CELL_SIZE = 4

board = {}
board_elements = {}


def generate_board():
    num_row_lines = 3 * ROW_NUMBER + ROW_NUMBER - 1
    num_col_lines = 3 * COLUMN_NUMBER + COLUMN_NUMBER - 1

    loop_var_i = 0

    while loop_var_i < num_row_lines:
        if loop_var_i % CELL_SIZE == 3:
            board[loop_var_i] = ['-']*num_col_lines
        else:
            board[loop_var_i] = ([' ']*3 + ['|']) * (COLUMN_NUMBER-1) + [' ']*3
        loop_var_i += 1


def modify_board(x_coordinate, y_coordinate, player_no):
    row_num = int(ROW_NUMBER / 2) + (x_coordinate - 1) * CELL_SIZE
    col_num = int(COLUMN_NUMBER / 2) + (y_coordinate - 1) * CELL_SIZE
    board[row_num][col_num] = board_elements[player_no]


def gamestart():
    xo_choice = input("Player 1 'X' or 'O': ")
    if xo_choice.upper() == 'X':
        board_elements["1"] = "X"
        board_elements["2"] = "O"
    elif xo_choice.upper() == 'O':
        board_elements["1"] = "O"
        board_elements["2"] = "X"
    else:
        print("Enter 'X' or 'O' only")


def gameplay():
    player_no = 1
    print(f"Player {player_no}'s turn:")
    x_coordinate = int(input("Enter the row number: "))
    y_coordinate = int(input("Enter the column number: "))