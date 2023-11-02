def solution():
    num_students = 24
    silent_reading = num_students / 2
    board_games = num_students / 3
    catch_up = num_students - silent_reading - board_games
    result = catch_up
    return result

print(solution())