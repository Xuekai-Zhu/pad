def solution():
    """In the class of 24 students, half are doing silent reading, and a third are playing board games. The rest are catching up on homework. How many students are catching up on homework?"""
    # Define the total number of students
    total_students = 24

    # Calculate the number of students doing silent reading
    silent_reading = total_students / 2

    # Calculate the number of students playing board games
    board_games = total_students / 3

    # Calculate the number of students catching up on homework
    homework = total_students - silent_reading - board_games

    # return the result
    result = homework
    return result

print(solution())