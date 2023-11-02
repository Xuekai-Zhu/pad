def solution():
    # Define the total number of students
    total_students = 24

    # Calculate the number of students doing silent reading
    silent_reading_students = total_students / 2

    # Calculate the number of students playing board games
    board_game_students = total_students / 3

    # Calculate the number of students catching up on homework
    homework_students = total_students - silent_reading_students - board_game_students
    result = homework_students
    return result

print(solution())