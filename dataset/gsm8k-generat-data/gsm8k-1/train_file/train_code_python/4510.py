def solution():
    """Gerald brings chocolate bars to school for his class to share. Each bar contains 8 squares. He brings 7 total bars. His teacher says that for every bar he brings, she will bring two more identical ones. There are 24 students in class. How many squares of chocolate does each student get?"""
    bars_brought = 7
    teacher_bars = bars_brought * 2
    total_bars = bars_brought + teacher_bars
    squares_per_bar = 8
    total_squares = total_bars * squares_per_bar
    students = 24
    squares_per_student = total_squares / students
    result = squares_per_student
    return result

print(solution())