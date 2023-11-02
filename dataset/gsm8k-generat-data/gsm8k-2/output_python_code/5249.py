def solution():
    """7 out of 40 people in a cafeteria are wearing checkered shirts. The rest of the people are wearing vertical stripes and horizontal stripes. The number of people wearing horizontal stripes is 4 times as many as the people wearing checkered shirts. How many people are wearing vertical stripes?"""
    checkered_shirts = 7
    horizontal_stripes = 4 * checkered_shirts
    total_checked_horizontal = checkered_shirts + horizontal_stripes
    vertical_stripes = 40 - total_checked_horizontal
    result = vertical_stripes
    return result

print(solution())