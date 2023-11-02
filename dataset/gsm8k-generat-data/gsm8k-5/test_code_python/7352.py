def solution():
    total_students = 24  # There are 24 students in the class

    # Calculate the number of students doing silent reading and board games
    reading_students = total_students // 2  # Half of the students are doing silent reading
    game_students = total_students // 3  # A third of the students are playing board games

    # Calculate the number of students catching up on homework
    homework_students = total_students - reading_students - game_students
    result = homework_students
    return result

print(solution())