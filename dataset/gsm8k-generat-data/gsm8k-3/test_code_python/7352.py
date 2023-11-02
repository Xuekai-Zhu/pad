def solution():
    """In the class of 24 students, half are doing silent reading, and a third are playing board games. The rest are catching up on homework. How many students are catching up on homework?"""
    # Define the total number of students in the class
    total_students = 24

    # Calculate the number of students doing silent reading
    reading_students = total_students / 2

    # Calculate the number of students playing board games
    games_students = total_students / 3

    # Calculate the number of students catching up on homework
    homework_students = total_students - reading_students - games_students

    # Display the number of students catching up on homework
    result = homework_students
    return result

print(solution())