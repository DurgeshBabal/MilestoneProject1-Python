ROW_NUMBER = 3
COLUMN_NUMBER = 3
CELL_SIZE = 4
WIN_LENGTH = 3

board = {}
board_elements = {}
input_board = [['Z']*COLUMN_NUMBER for i in range(ROW_NUMBER)]


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


def game_start():

    while True:
        xo_choice = input("Player 1 'X' or 'O': ")
        if xo_choice.upper() == 'X':
            board_elements["1"] = "X"
            board_elements["2"] = "O"
            break
        elif xo_choice.upper() == 'O':
            board_elements["1"] = "O"
            board_elements["2"] = "X"
            break
        else:
            print("Enter 'X' or 'O' only")


def print_board():

    num_row_lines = 3 * ROW_NUMBER + ROW_NUMBER - 1
    loop_var_i = 0

    while loop_var_i < num_row_lines:
        for board_unit in board[loop_var_i]:
            print(board_unit, end='')


def modify_board(x_coordinate, y_coordinate, current_player):

    row_num = int(ROW_NUMBER / 2) + (x_coordinate - 1) * CELL_SIZE
    col_num = int(COLUMN_NUMBER / 2) + (y_coordinate - 1) * CELL_SIZE

    board[row_num][col_num] = board_elements[current_player]
    input_board[x_coordinate - 1][y_coordinate - 1] = board_elements[current_player]


def win_check():

    loop_var_i, loop_var_j, win_length = 0

    # Horizontal check
    while loop_var_i < ROW_NUMBER:
        loop_var_j = 0
        current_element = input_board[loop_var_i][loop_var_j]

        while loop_var_j < COLUMN_NUMBER:
            board_unit = input_board[loop_var_i][loop_var_j]

            if board_unit == 'Z':
                win_length = 0
                continue
            elif board_unit == current_element:
                win_length += 1
            else:
                win_length = 0
                current_element = board_unit

            if win_length == WIN_LENGTH:
                return True

        loop_var_i += 1

    # Vertical check
    while loop_var_j < COLUMN_NUMBER:
        loop_var_i = 0
        current_element = input_board[loop_var_i][loop_var_j]

        while loop_var_i < ROW_NUMBER:
            board_unit = input_board[loop_var_i][loop_var_j]

            if board_unit == 'Z':
                win_length = 0
                continue
            elif board_unit == current_element:
                win_length += 1
            else:
                win_length = 0
                current_element = board_unit

            if win_length == WIN_LENGTH:
                return True

            loop_var_i += 1

        loop_var_j += 1

    # Top -> Bottom Right Diagonal check



def gameplay():

    generate_board()
    game_start()
    current_player = 1

    while True:
        print_board()
        current_player = current_player % 3

        print(f"Player {current_player}'s turn:")
        x_coordinate = int(input("Enter the row number: "))
        y_coordinate = int(input("Enter the column number: "))

        if x_coordinate > ROW_NUMBER or y_coordinate > COLUMN_NUMBER:
            print("X and Y coordinates should be upto size of board")
        else:
            modify_board(x_coordinate, y_coordinate, current_player)
            if win_check():
                print(f"Player {current_player} wins!")
                break
            current_player += 1
