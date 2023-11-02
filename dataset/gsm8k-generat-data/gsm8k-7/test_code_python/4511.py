def solution():
    num_bars = 7
    squares_per_bar = 8
    teacher_multiplier = 2
    num_students = 24

    # Calculate the total number of bars, including the teacher's contribution
    total_bars = num_bars + (num_bars * teacher_multiplier)

    # Calculate the total number of squares of chocolate
    total_squares = total_bars * squares_per_bar

    # Calculate the number of squares each student gets
    squares_per_student = total_squares // num_students
    result = squares_per_student
    return result

print(solution())