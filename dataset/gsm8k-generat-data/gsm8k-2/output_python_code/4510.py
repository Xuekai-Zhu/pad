def solution():
    """Gerald brings chocolate bars to school for his class to share. Each bar contains 8 squares. He brings 7 total bars. His teacher says that for every bar he brings, she will bring two more identical ones. There are 24 students in class. How many squares of chocolate does each student get?"""
    total_bars = 7 + (2 * 7)
    total_squares = total_bars * 8
    squares_per_student = total_squares // 24
    result = squares_per_student
    return result

print(solution())