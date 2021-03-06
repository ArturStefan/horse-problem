def movement_within_board(movement):
    within_board = True

    if movement[0] < 0 or movement[0] > 7:
        within_board = False

    if movement[1] < 0 or movement[1] > 7:
        within_board = False

    return within_board


def visited_square(movement, visited_squares):
    not_visited_squares = True if movement not in visited_squares else False

    return not_visited_squares


def valid_move(movement, visited_squares):
    within_board = movement_within_board(movement)
    not_visited_squares = visited_square(movement, visited_squares)

    valid_movement = True if within_board and not_visited_squares else False

    return valid_movement
