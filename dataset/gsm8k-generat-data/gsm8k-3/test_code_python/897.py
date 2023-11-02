def solution():
    """The perimeter of a square-shaped piece of paper is 20 cm shorter than the height of a computer screen. How many cm is the height of the screen if the side of the square paper is 20 cm?"""
    # Define the length of the side of the square paper
    side_length = 20

    # Calculate the perimeter of the square paper
    paper_perimeter = 4 * side_length

    # Calculate the height of the computer screen
    screen_height = paper_perimeter + 20

    # Display the height of the screen
    result = screen_height
    return result

print(solution())