def solution():
    num_rows = 10
    num_squares_per_row = 15

    # Calculate the total number of squares in the grid
    total_squares = num_rows * num_squares_per_row

    # Calculate the number of squares colored with red
    red_rows = 4
    red_squares_per_row = 6
    red_squares = red_rows * red_squares_per_row

    # Calculate the number of squares colored with blue
    blue_rows = 4
    blue_squares_per_row = num_squares_per_row
    blue_squares = (blue_rows * blue_squares_per_row) * 2

    # Calculate the number of squares colored with green
    green_squares = total_squares - red_squares - blue_squares
    result = green_squares
    return result

print(solution())