def solution():
    # Define the number of rows and columns in the grid
    rows = 10
    columns = 15

    # Define the number of red squares in each row
    red_squares = 6

    # Define the number of blue rows
    blue_rows = 2

    # Define the number of green rows
    green_rows = rows - (red_squares + blue_rows)

    # Calculate the total number of squares in the grid
    total_squares = rows * columns

    # Calculate the number of squares that Marla colors blue
    blue_squares = 2 * columns + 2 * (columns - red_squares)

    # Calculate the number of squares that Marla colors red
    red_squares_total = red_squares * 4

    # Calculate the number of squares that Marla colors green
    green_squares = total_squares - blue_squares - red_squares_total

    result = green_squares
    return result

print(solution())