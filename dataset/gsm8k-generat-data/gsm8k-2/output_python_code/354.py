def solution():
    """Marla has a grid of squares that has 10 rows and 15 squares in each row. She colors 4 rows of 6 squares in the middle of the grid with red. She colors all squares on the first 2 and last 2 rows with blue. Then she colors the rest with green. How many squares does Marla color green?"""
    total_rows = 10
    row_squares = 15
    red_rows = 4
    red_squares_per_row = 6
    blue_rows = 4
    green_rows = total_rows - red_rows - blue_rows
    green_squares_per_row = row_squares - red_squares_per_row
    total_green_squares = green_rows * green_squares_per_row
    result = total_green_squares
    return result

print(solution())