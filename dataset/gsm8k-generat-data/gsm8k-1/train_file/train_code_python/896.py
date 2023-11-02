def solution():
    """The perimeter of a square-shaped piece of paper is 20 cm shorter than the height of a computer screen. How many cm is the height of the screen if the side of the square paper is 20 cm?"""
    side_length = 20
    square_perimeter = 4 * side_length
    screen_height = square_perimeter + 20
    result = screen_height
    return result

print(solution())