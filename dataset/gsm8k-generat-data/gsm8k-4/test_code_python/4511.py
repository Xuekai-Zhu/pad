def solution():
    """Gerald brings chocolate bars to school for his class to share. Each bar contains 8 squares. He brings 7 total bars. His teacher says that for every bar he brings, she will bring two more identical ones. There are 24 students in class. How many squares of chocolate does each student get?"""
    # Define the number of bars brought by Gerald
    gerald_bars = 7

    # Define the number of bars brought by the teacher
    teacher_bars = 2 * gerald_bars

    # Calculate the total number of bars
    total_bars = gerald_bars + teacher_bars

    # Calculate the total number of chocolate squares
    total_squares = total_bars * 8

    # Calculate the number of squares each student gets
    squares_per_student = total_squares / 24

    # return the result
    result = squares_per_student
    return result

print(solution())