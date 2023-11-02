def solution():
    total_bars = 7
    teacher_multiplier = 2
    total_bars_including_teacher = total_bars * (teacher_multiplier + 1)
    squares_per_bar = 8
    total_squares = total_bars_including_teacher * squares_per_bar
    student_count = 24
    squares_per_student = total_squares / student_count
    result = squares_per_student
    return result

print(solution())