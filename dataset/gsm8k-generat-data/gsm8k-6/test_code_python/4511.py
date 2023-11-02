def solution():
    # Calculate the total number of chocolate bars
    total_bars = 7 + 2 * 7  # for every bar Gerald brings, the teacher brings two more identical ones
    total_squares = total_bars * 8  # each bar contains 8 squares

    # Calculate the number of squares of chocolate each student gets
    squares_per_student = total_squares / 24  # there are 24 students in class
    
    result = squares_per_student
    return result

print(solution())