def solution():
    """Marla has a grid of squares that has 10 rows and 15 squares in each row. She colors 4 rows of 6 squares in the middle of the grid with red. She colors all squares on the first 2 and last 2 rows with blue. Then she colors the rest with green. How many squares does Marla color green?"""
    # Define the total number of squares in the grid
    total_squares = 10 * 15

    # Calculate the number of squares colored with red
    red_squares = 4 * 6

    # Calculate the number of squares colored with blue
    blue_squares = 2 * 15 + 2 * 15

    # Calculate the number of squares colored with green
    green_squares = total_squares - red_squares - blue_squares

    # return the result
    result = green_squares
    return result

print(solution())