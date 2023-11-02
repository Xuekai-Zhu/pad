def solution():
    # Define the length of the side of the square paper
    square_side_length = 20

    # Calculate the perimeter of the square paper
    square_perimeter = 4 * square_side_length

    # Define the difference between the screen height and the square perimeter
    height_difference = 20

    # Calculate the height of the screen
    screen_height = square_perimeter + height_difference
    result = screen_height
    return result

print(solution())