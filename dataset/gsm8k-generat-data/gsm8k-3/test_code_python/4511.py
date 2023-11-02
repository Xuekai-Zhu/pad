def solution():
    """Gerald brings chocolate bars to school for his class to share. Each bar contains 8 squares. He brings 7 total bars. His teacher says that for every bar he brings, she will bring two more identical ones. There are 24 students in class. How many squares of chocolate does each student get?"""
    # Define the number of bars Gerald brings and the number of additional bars the teacher brings per bar
    GERALD_BARS = 7
    TEACHER_BARS_PER_GERALD_BAR = 2

    # Define the number of squares per bar
    SQUARES_PER_BAR = 8

    # Define the number of students in class
    STUDENTS = 24

    # Calculate the total number of bars
    total_bars = GERALD_BARS + (GERALD_BARS * TEACHER_BARS_PER_GERALD_BAR)

    # Calculate the total number of squares
    total_squares = total_bars * SQUARES_PER_BAR

    # Calculate the number of squares per student
    squares_per_student = total_squares // STUDENTS

    # Display the number of squares per student
    result = squares_per_student
    return result

print(solution())