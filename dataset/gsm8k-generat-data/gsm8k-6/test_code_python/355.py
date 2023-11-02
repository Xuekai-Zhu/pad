def solution():
    # Calculate the total number of squares in the grid
    total_squares = 10 * 15

    # Calculate the number of squares colored red
    red_squares = 4 * 6

    # Calculate the number of squares colored blue
    blue_squares = 2 * 15 + 2 * 15

    # Calculate the number of squares colored green
    green_squares = total_squares - red_squares - blue_squares

    result = green_squares
    return result

print(solution())