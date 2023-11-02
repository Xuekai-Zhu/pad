def solution():
    total_squares = 16 * 16
    percent_complete = 0.25
    squares_completed = int(total_squares * percent_complete)

    # Calculate the number of squares left to sew together
    squares_left = total_squares - squares_completed
    result = squares_left
    return result

print(solution())