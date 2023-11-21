# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Names: MICHAEL NGUYEN
# NAME OF TEAM MEMBER 2
# NAME OF TEAM MEMBER 3
# NAME OF TEAM MEMBER 4
# Section: 536
# Assignment: LAB-13
# Date: 20 NOVEMBER 2023

import os

PLAYER_WHITE = f' {chr(9679)} '
PLAYER_BLACK = f' {chr(9675)} '
BOARD_PIECE = f' {chr(9676)} '
# prints the score board
def printScoreBoard(player_one_score, player_two_score):
    print(f'Captures for {PLAYER_WHITE}: {player_one_score}')
    print(f'Captures for {PLAYER_BLACK}: {player_two_score}')
# checks for captures
def checkForCapture(pente_board_list, used_positions, row, column):
    original_piece = pente_board_list[row][column]
    capture_points = 0

    if original_piece == PLAYER_WHITE:
        opposite_piece = PLAYER_BLACK
    elif original_piece == PLAYER_BLACK:
        opposite_piece = PLAYER_WHITE

    # check for horizontal to the right capute
    if original_piece == pente_board_list[row][column + 3]:
        if pente_board_list[row][column + 1] == opposite_piece and pente_board_list[row][column + 2] == opposite_piece:
            pente_board_list[row][column + 1] = BOARD_PIECE
            pente_board_list[row][column + 2] = BOARD_PIECE
            captured_pair_one = (row,  column + 1)
            captured_pair_two = (row, column + 2)
            used_positions .remove(captured_pair_one)
            used_positions.remove(captured_pair_two)
            capture_points += 1

    # check for horizontal to the left capture
    if original_piece == pente_board_list[row][column - 3]:
        if pente_board_list[row][column - 1] == opposite_piece and pente_board_list[row][column - 2] == opposite_piece:
            pente_board_list[row][column - 1] = BOARD_PIECE
            pente_board_list[row][column - 2] = BOARD_PIECE
            captured_pair_one = (row,  column - 1)
            captured_pair_two = (row, column - 2)
            used_positions .remove(captured_pair_one)
            used_positions.remove(captured_pair_two)
            capture_points += 1

    # checks for vertical capture upwards
    if original_piece == pente_board_list[row + 3][column]:
        if pente_board_list[row + 1][column] == opposite_piece and pente_board_list[row + 2][column] == opposite_piece:
            pente_board_list[row + 1][column] = BOARD_PIECE
            pente_board_list[row + 2][column] = BOARD_PIECE
            captured_pair_one = (row+ 1,  column)
            captured_pair_two = (row + 2, column)
            used_positions .remove(captured_pair_one)
            used_positions.remove(captured_pair_two)
            capture_points += 1

    # checks for vertical capture downwards
    if original_piece == pente_board_list[row - 3][column]:
        if pente_board_list[row - 1][column] == opposite_piece and pente_board_list[row - 2][column] == opposite_piece:
            pente_board_list[row - 1][column] = BOARD_PIECE
            pente_board_list[row - 2][column] = BOARD_PIECE
            captured_pair_one = (row- 1,  column)
            captured_pair_two = (row - 2, column)
            used_positions .remove(captured_pair_one)
            used_positions.remove(captured_pair_two)
            capture_points += 1

    # checks for diagonal capture downwards to the right
    if original_piece == pente_board_list[row + 3][column +3]:
        if pente_board_list[row + 1][column + 1] == opposite_piece and pente_board_list[row + 2][
            column + 2] == opposite_piece:
            pente_board_list[row  + 1][column + 1] = BOARD_PIECE
            pente_board_list[row + 2][column + 2] = BOARD_PIECE
            captured_pair_one = (row + 1, column + 1)
            captured_pair_two = (row + 2, column + 2)
            used_positions.remove(captured_pair_one)
            used_positions.remove(captured_pair_two)
            capture_points += 1

    # checks for diagonal capture upwards to the left
    if original_piece == pente_board_list[row - 3][column - 3]:
            if pente_board_list[row - 1][column - 1] == opposite_piece and pente_board_list[row - 2][
                column - 2] == opposite_piece:
                pente_board_list[row - 1][column - 1] = BOARD_PIECE
                pente_board_list[row - 2][column - 2] = BOARD_PIECE
                captured_pair_one = (row - 1, column - 1)
                captured_pair_two = (row - 2, column - 2)
                used_positions.remove(captured_pair_one)
                used_positions.remove(captured_pair_two)
                capture_points += 1

        # checks for diagonal capture downwards to the left
    if original_piece == pente_board_list[row + 3][column - 3]:
        if pente_board_list[row + 1][column - 1] == opposite_piece and pente_board_list[row + 2][
            column - 2] == opposite_piece:
            pente_board_list[row + 1][column - 1] = BOARD_PIECE
            pente_board_list[row + 2][column - 2] = BOARD_PIECE
            captured_pair_one = (row + 1, column - 1)
            captured_pair_two = (row + 2, column - 2)
            used_positions.remove(captured_pair_one)
            used_positions.remove(captured_pair_two)
            capture_points += 1

    # checks for diagonal capture upwards to the right
    if original_piece == pente_board_list[row - 3][column + 3]:
        if pente_board_list[row - 1][column + 1] == opposite_piece and pente_board_list[row - 2][
            column + 2] == opposite_piece:
            pente_board_list[row - 1][column + 1] = BOARD_PIECE
            pente_board_list[row - 2][column + 2] = BOARD_PIECE
            captured_pair_one = (row - 1, column + 1)
            captured_pair_two = (row - 2, column + 2)
            used_positions.remove(captured_pair_one)
            used_positions.remove(captured_pair_two)
            capture_points += 1

    return capture_points
# checks all win conditions. Improves redundancy in main game loop
def checkForAllWinConditions(pente_board_list):
    checkHorizontalWinCondition(pente_board_list)
    checkVerticalWinCondition(pente_board_list)
    checkDiagonalDownWinCondition(pente_board_list)
    checkDiagonalUpWinCondition(pente_board_list)
# checks for diagonal bottom left to top right direction
def checkDiagonalUpWinCondition(pente_board_list):
    for row_index, rowlist in enumerate(pente_board_list):
        for column_index, piece in enumerate(rowlist):
            if piece == f'{BOARD_PIECE}':
                continue
            else:
                win_condition = True
                diagonal_count = 1
                current_row = row_index
                current_col = column_index
                piece_type = pente_board_list[row_index][column_index]

                while diagonal_count != 5:
                    try:
                        current_row += 1
                        current_col -=1
                        if piece_type == pente_board_list[current_row][current_col]:
                            diagonal_count += 1
                        else:
                            win_condition = False
                            break
                    except IndexError:
                        break

                if win_condition == True:
                    print(f'{piece_type} wins!')
                    quit()
# checks for diagonal top left to bottom right direction
def checkDiagonalDownWinCondition(pente_board_list):
    for row_index, rowlist in enumerate(pente_board_list):
        for column_index, piece in enumerate(rowlist):
            if piece == f'{BOARD_PIECE}':
                continue
            else:
                win_condition = True
                diagonal_count = 1
                current_row = row_index
                current_col = column_index
                piece_type = pente_board_list[row_index][column_index]

                while diagonal_count != 5:
                    try:
                        current_row += 1
                        current_col +=1
                        if piece_type == pente_board_list[current_row][current_col]:
                            diagonal_count += 1
                        else:
                            win_condition = False
                            break
                    except IndexError:
                        break

                if win_condition == True:
                    print(f'{piece_type} wins!')
                    quit()
# checks vertical for 5 in a row
def checkVerticalWinCondition(pente_board_list):
    '''checks vertical for 5 in a row'''
    for row_index, rowlist in enumerate(pente_board_list):
        for column_index, piece in enumerate(rowlist):
            if piece == f'{BOARD_PIECE}':
                continue
            else:
                win_condition = True
                vertical_count = 1
                current_row = row_index
                current_col = column_index
                piece_type = pente_board_list[row_index][column_index]

                while vertical_count != 5:
                    current_row += 1
                    if piece_type == pente_board_list[current_row][column_index]:
                        vertical_count += 1
                    else:
                        win_condition = False
                        break

                if win_condition == True:
                    print(f'{piece_type} wins!')
                    quit()
# checks horizontal for 5 in a row
def checkHorizontalWinCondition(pente_board_list):
    '''checks horizontal for 5 in a row'''
    for row_index, rowlist in enumerate(pente_board_list):
        for column_index, piece in enumerate(rowlist):
            if piece == f'{BOARD_PIECE}':
                continue
            else:
                win_condition = True
                horizontal_count = 1
                current_row = row_index
                current_col = column_index
                piece_type = pente_board_list[row_index][column_index]

                while horizontal_count != 5:
                    current_col += 1
                    if piece_type == pente_board_list[row_index][current_col]:
                        horizontal_count += 1
                    else:
                        win_condition = False
                        break

                if win_condition == True:
                    print(f'{piece_type} wins!')
                    quit()
# collects row or column
def collectRowOrColumn(pente_board_list, row_or_column):
    '''collects row or column'''
    # define valid inputs
    valid_inputs = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10','11','12','13','14','15','16','17','18', 'g', 'q']


    print(f'Pick a {row_or_column}: then [enter] or "g" for instruction grid\n> ', end='')
    position = input()
    print()

    if position == 'q':
        confirmation = input('Are you sure you want to quit? [q] to quit [anything else] to continue:\n> ')
        if confirmation == 'q':
            quit()
        else:
            print(f'Pick a {row_or_column}: then [enter] or "g" for instruction grid\n> ', end='')
            position = input()
            print()

    # checks for valid inputs
    while position not in valid_inputs:
        print('Error: Invalid input')
        print(f'Pick a {row_or_column}: then [enter] or "g" for instruction grid\n> ',end='')
        position = input()
        if position == 'q':
            confirmation = input('Are you sure you want to quit? [q] to quit [anything else] to continue:\n> ')
            if confirmation == 'q':
                quit()
            else:
                print(f'Pick a {row_or_column}: then [enter] or "g" for instruction grid\n> ', end='')
                position = input()
                print()
        print()

    # check for g for instructions
    while position == 'g':
        printInstructions(pente_board_list)
        print()
        print(f'Pick a {row_or_column}: then [enter] or "g" for instruction grid\n> ',end='')
        position = input()
        if position == 'q':
            confirmation = input('Are you sure you want to quit? [q] to quit [anything else] to continue:\n> ')
            if confirmation == 'q':
                quit()
            else:
                print(f'Pick a {row_or_column}: then [enter] or "g" for instruction grid\n> ', end='')
                position = input()
                print()
        print()
        while position not in valid_inputs:
            print('Error: Invalid input')
            print(f'Pick a {row_or_column}: then [enter] or "g" for instruction grid\n> ', end='')
            position = input()
            if position == 'q':
                confirmation = input('Are you sure you want to quit? [q] to quit [anything else] to continue:\n> ')
                if confirmation == 'q':
                    quit()
                else:
                    print(f'Pick a {row_or_column}: then [enter] or "g" for instruction grid\n> ', end='')
                    position = input()
                    print()
            print()

    return int(position)
# instructions grid printing
def printInstructions(pente_board_list):
    '''instructions grid printing'''
    for instruction_row in range(len(pente_board_list)):
        for j in range(19):
            print(f'{instruction_row:02d}-{j:02d}',end='  ')
        print()
# collection position for desired player
def collectPosition(pente_board_list, used_positions_list, player_name):
    '''collection position for desired player'''

    print(f'Player {player_name} turn. (If you would like to see the instruction grid, type "g")', end='\n\n')

    row = collectRowOrColumn(pente_board_list, 'row')
    column = collectRowOrColumn(pente_board_list, 'column')
    new_pair = (row, column)

    # this is to confirm the pair entered is not already used.
    while new_pair in used_positions_list:
        print(f'The pair: {new_pair} has already been placed. Please enter another pair',end='\n\n')
        row = collectRowOrColumn(pente_board_list, 'row')
        column = collectRowOrColumn(pente_board_list, 'column')
        new_pair = (row, column)

    return new_pair
# printing default empty board
def penteBoardPrint(pente_board_list):
    '''printing default empty board'''
    for row,row_list in enumerate(pente_board_list):
        for column in range(len(row_list)):
            if len(pente_board_list[row][column]) == 0:
                print(f'{BOARD_PIECE}', end='')
            else:
                print(pente_board_list[row][column], end='')
        print()
def main():
    # initialize empty go board
    pente_board = [[], [], [], [], [], [], [], [], [],[], [], [], [], [], [], [], [], [], []]

    #list of used positions
    used_positions = []

    # fill go board with periods
    for row in range(len(pente_board)):
        for i in range(19):
            pente_board[row].append(str(f'{BOARD_PIECE}'))

    print('Welcome to Pente!\n')

    try:
        with open('pente_instructions.txt', 'r') as file:
            instructions = file.readlines()
            for line in instructions:
                print(line, end ='')
    except FileNotFoundError:
        print('No instructions file detected! [missing: pente_instructions.txt]')


    # collect player names
    player_one = input(f'\n\nPlease enter the name of player one (white {PLAYER_WHITE}): \n> ').strip()
    print()
    while len(player_one) > 12:
        print('Error: Exceeds 12 characters. Please input a valid name')
        player_one = input(f'Please enter the name of player one (white {PLAYER_WHITE}): \n> ').strip()
        print()

    player_two = input(f'Please enter the name of player two (black {PLAYER_BLACK}): \n> ').strip()
    print()
    while len(player_two) > 12:
        print('Error: Exceeds 12 characters. Please input a valid name')
        player_two = input(f'Please enter the name of player one (white {PLAYER_WHITE}): \n> ').strip()
        print()

    print (f'Welcome {player_one} and {player_two} to Pente!')
    print(f'Place your piece by providing the row then the column. Here is how they are numberd:\n')
    print('Press q to quit anytime!')

# prints number grid
    printInstructions(pente_board)

    print()
    player_one_captures = 0
    player_two_captures = 0

    # this is the main game loop
    while not (len(used_positions) > (19 * 19)):

        # player one
        new_pair_one = collectPosition(pente_board, used_positions, player_one)
        # append new pair to existing pairs
        used_positions.append(new_pair_one)

        pente_board[ new_pair_one[0] ][new_pair_one[1]] = f'{PLAYER_WHITE}'
        penteBoardPrint(pente_board)
        print('\n')
        current_player_one_captures = checkForCapture(pente_board,used_positions, new_pair_one[0], new_pair_one[1])
        if current_player_one_captures > 0:
            player_one_captures += current_player_one_captures
            print(f'{player_one} captures!')
            penteBoardPrint(pente_board)

        if player_one_captures == 10:
            print(f'{PLAYER_WHITE} wins!')
            quit()

        checkForAllWinConditions(pente_board)

        printScoreBoard(player_one_captures, player_two_captures)
        print('\n')


        # player two
        new_pair_two = collectPosition(pente_board, used_positions, player_two)
        # append new pair to existing pairs
        used_positions.append(new_pair_two)

        pente_board[new_pair_two[0]][new_pair_two[1]] = f'{PLAYER_BLACK}'
        penteBoardPrint(pente_board)
        print('\n')

        current_player_two_captures = checkForCapture(pente_board,used_positions, new_pair_two[0], new_pair_two[1])
        if current_player_two_captures > 0:
            player_two_captures += current_player_two_captures
            print(f'{player_two} captures!')
            penteBoardPrint(pente_board)

        if player_two_captures == 10:
            print(f'{PLAYER_BLACK} wins!')
            quit()

        checkForAllWinConditions(pente_board)


        printScoreBoard(player_one_captures, player_two_captures)
        print('\n')


if __name__ == "__main__":
    main()