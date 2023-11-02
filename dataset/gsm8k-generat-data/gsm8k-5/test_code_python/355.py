def solution():
    total_rows = 10
    squares_per_row = 15
    red_rows = 4
    red_squares_per_row = 6
    blue_rows = 4

    # Calculate the total number of squares colored red
    red_squares = red_rows * red_squares_per_row

    # Calculate the total number of squares colored blue
    blue_squares = squares_per_row * blue_rows

    # Calculate the total number of squares colored green
    green_squares = (total_rows * squares_per_row) - red_squares - blue_squares

    result = green_squares
    return result

print(solution())