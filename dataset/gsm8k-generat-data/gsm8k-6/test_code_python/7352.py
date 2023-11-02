def solution():
    total_students = 24
    silent_reading_students = total_students / 2
    board_game_students = total_students / 3
    catching_up_students = total_students - silent_reading_students - board_game_students
    result = catching_up_students
    return result

print(solution())