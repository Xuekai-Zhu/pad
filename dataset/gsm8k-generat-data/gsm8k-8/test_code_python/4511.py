def solution():
    # Calculate the total number of bars after the teacher brings in more
    total_bars = 7 + (7 * 2)

    # Calculate the total number of squares of chocolate
    total_squares = total_bars * 8

    # Calculate the number of squares of chocolate each student gets
    squares_per_student = total_squares / 24
    result = squares_per_student
    return result

print(solution())