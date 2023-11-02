def solution():
    """The perimeter of a square-shaped piece of paper is 20 cm shorter than the height of a computer screen. How many cm is the height of the screen if the side of the square paper is 20 cm?"""
    square_side = 20
    paper_perimeter = 4 * square_side
    screen_height = paper_perimeter + 20
    result = screen_height
    return result

print(solution())