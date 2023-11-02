def solution():
    
    total_students = 24
    silent_reading_students = total_students / 2
    board_game_students = total_students / 3
    homework_students = total_students - silent_reading_students - board_game_students
    result = homework_students
    return result

print(solution())