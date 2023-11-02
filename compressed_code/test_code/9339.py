def solution():
    
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