def solution():
    """Four kids can wash three whiteboards in 20 minutes. How long would it take, in minutes, for one kid to wash six whiteboards?"""
    num_kids = 4
    num_boards = 3
    time = 20
    boards_per_kid = num_boards / num_kids
    time_per_board = time / boards_per_kid
    time_per_six_boards = time_per_board * 2
    result = time_per_six_boards
    return result

print(solution())