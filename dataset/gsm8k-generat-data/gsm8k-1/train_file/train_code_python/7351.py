def solution():
    """In the class of 24 students, half are doing silent reading, and a third are playing board games. The rest are catching up on homework. How many students are catching up on homework?"""
    total_students = 24
    silent_reading_students = total_students / 2
    board_game_students = total_students / 3
    catching_up_students = total_students - silent_reading_students - board_game_students
    result = catching_up_students
    return result

print(solution())