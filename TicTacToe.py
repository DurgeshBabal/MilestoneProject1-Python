ROW_NUMBER = 3
COLUMN_NUMBER = 3
CELL_SIZE = 4
WIN_LENGTH = 3

board = {}
board_elements = {}
input_board = [['Z']*COLUMN_NUMBER for i in range(ROW_NUMBER)]


def generate_board():

    num_row_lines = CELL_SIZE * ROW_NUMBER - 1
    num_col_lines = CELL_SIZE * COLUMN_NUMBER - 1
    loop_var_i = 0

    while loop_var_i < num_row_lines:
        if loop_var_i % CELL_SIZE == CELL_SIZE - 1:
            board[loop_var_i] = ['-']*num_col_lines
        else:
            board[loop_var_i] = ([' ']*(CELL_SIZE - 1) + ['|']) * (COLUMN_NUMBER-1) + [' ']*(CELL_SIZE - 1)
        loop_var_i += 1


def game_start():

    while True:
        xo_choice = input("Player 1 'X' or 'O': ")
        if xo_choice.upper() == 'X':
            board_elements[1] = "X"
            board_elements[2] = "O"
            break
        elif xo_choice.upper() == 'O':
            board_elements[1] = "O"
            board_elements[2] = "X"
            break
        else:
            print("Enter 'X' or 'O' only")


def print_board():

    num_row_lines = CELL_SIZE * ROW_NUMBER - 1
    loop_var_i = 0

    print("")
    while loop_var_i < num_row_lines:
        for board_unit in board[loop_var_i]:
            print(board_unit, end='')
        print("")
        loop_var_i += 1
    print("")


def check_existing(x_coordinate, y_coordinate):
    return input_board[x_coordinate - 1][y_coordinate - 1] in ('X', 'O')


def modify_board(x_coordinate, y_coordinate, current_player):

    row_num = int((CELL_SIZE - 1) / 2) + (x_coordinate - 1) * CELL_SIZE
    col_num = int((CELL_SIZE - 1) / 2) + (y_coordinate - 1) * CELL_SIZE

    board[row_num][col_num] = board_elements[current_player]
    input_board[x_coordinate - 1][y_coordinate - 1] = board_elements[current_player]


def win_check():

    # Horizontal check
    loop_var_i, loop_var_j, win_length = 0, 0, 0
    while loop_var_i < ROW_NUMBER:
        loop_var_j, win_length = 0, 0
        current_element = input_board[loop_var_i][loop_var_j]

        while loop_var_j < COLUMN_NUMBER:
            board_unit = input_board[loop_var_i][loop_var_j]

            if board_unit == 'Z':
                win_length = 0
            elif board_unit == current_element:
                win_length += 1
            else:
                win_length = 1
                current_element = board_unit

            if win_length == WIN_LENGTH:
                return True

            loop_var_j += 1

        loop_var_i += 1

    # Vertical check
    loop_var_i, loop_var_j, win_length = 0, 0, 0
    while loop_var_j < COLUMN_NUMBER:
        loop_var_i, win_length = 0, 0
        current_element = input_board[loop_var_i][loop_var_j]

        while loop_var_i < ROW_NUMBER:
            board_unit = input_board[loop_var_i][loop_var_j]

            if board_unit == 'Z':
                win_length = 0
            elif board_unit == current_element:
                win_length += 1
            else:
                win_length = 1
                current_element = board_unit

            if win_length == WIN_LENGTH:
                return True

            loop_var_i += 1

        loop_var_j += 1

    # Top -> Bottom Right Diagonal check
    row_times = ROW_NUMBER - WIN_LENGTH
    col_times = COLUMN_NUMBER - WIN_LENGTH

    loop_var_i, loop_var_j, win_length = 0, 0, 0
    while loop_var_i <= row_times:
        loop_var_j, win_length = 0, 0
        current_element = input_board[loop_var_i][loop_var_j]

        while loop_var_i + loop_var_j < ROW_NUMBER and loop_var_j < COLUMN_NUMBER:
            board_unit = input_board[loop_var_i + loop_var_j][loop_var_j]

            if board_unit == 'Z':
                win_length = 0
            elif board_unit == current_element:
                win_length += 1
            else:
                win_length = 1
                current_element = board_unit

            if win_length == WIN_LENGTH:
                return True

            loop_var_j += 1

        loop_var_i += 1

    loop_var_i, loop_var_j, win_length = 0, 1, 0
    while loop_var_j < col_times:
        loop_var_i, win_length = 0, 0
        current_element = input_board[loop_var_i][loop_var_j]

        while loop_var_i < ROW_NUMBER and loop_var_j + loop_var_i < COLUMN_NUMBER:
            board_unit = input_board[loop_var_i][loop_var_j + loop_var_i]

            if board_unit == 'Z':
                win_length = 0
            elif board_unit == current_element:
                win_length += 1
            else:
                win_length = 1
                current_element = board_unit

            if win_length == WIN_LENGTH:
                return True

            loop_var_i += 1

        loop_var_j += 1

    # Top -> Bottom Left Diagonal check
    loop_var_i, loop_var_j, win_length = 0, COLUMN_NUMBER - col_times - 1, 0
    while loop_var_j < COLUMN_NUMBER:
        loop_var_i, win_length = 0, 0
        current_element = input_board[loop_var_i][loop_var_j]

        while loop_var_i < ROW_NUMBER and loop_var_j - loop_var_i >= 0:
            board_unit = input_board[loop_var_i][loop_var_j - loop_var_i]

            if board_unit == 'Z':
                win_length = 0
            elif board_unit == current_element:
                win_length += 1
            else:
                win_length = 1
                current_element = board_unit

            if win_length == WIN_LENGTH:
                return True

            loop_var_i += 1

        loop_var_j += 1

    loop_var_i, loop_var_j, win_length = 1, COLUMN_NUMBER - 1, 0
    while loop_var_i <= row_times:
        loop_var_j, win_length = COLUMN_NUMBER - 1, 0
        current_element = input_board[loop_var_i][loop_var_j]

        while loop_var_i < ROW_NUMBER and loop_var_j >= 0:
            board_unit = input_board[loop_var_i][loop_var_j]

            if board_unit == 'Z':
                win_length = 0
            elif board_unit == current_element:
                win_length += 1
            else:
                win_length = 1
                current_element = board_unit

            if win_length == WIN_LENGTH:
                return True

            loop_var_j -= 1

        loop_var_i += 1


if __name__ == "__main__":

    generate_board()
    game_start()
    move_counter = ROW_NUMBER * COLUMN_NUMBER
    current_player = 1

    while True:
        print_board()
        if not move_counter:
            print("It's a draw!")
            break
        if current_player == 3:
            current_player -= 2

        print(f"Player {current_player}'s turn")
        x_coordinate = int(input("Enter the row number: "))
        y_coordinate = int(input("Enter the column number: "))

        if x_coordinate > ROW_NUMBER or y_coordinate > COLUMN_NUMBER:
            print("X and Y coordinates should be upto size of board")
        elif check_existing(x_coordinate, y_coordinate):
            print("This cell is already filled")
        else:
            modify_board(x_coordinate, y_coordinate, current_player)
            if win_check():
                print_board()
                print(f"Player {current_player} wins!")
                break
            current_player += 1
            move_counter -= 1
