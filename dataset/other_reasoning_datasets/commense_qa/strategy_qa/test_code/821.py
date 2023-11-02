def solution():
    chess_board_squares = 64
    shogi_board_squares = 81
    if shogi_board_squares > chess_board_squares:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())