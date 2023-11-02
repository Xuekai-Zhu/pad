def solution():
    total_bars = 7  # Gerald brings 7 chocolate bars
    total_bars_with_teacher = total_bars + (2 * total_bars)  # The teacher brings 2 identical bars for each bar Gerald brings
    total_squares = total_bars_with_teacher * 8  # Each bar contains 8 squares

    # Calculate the number of squares each student gets
    squares_per_student = total_squares / 24

    result = squares_per_student
    return result

print(solution())