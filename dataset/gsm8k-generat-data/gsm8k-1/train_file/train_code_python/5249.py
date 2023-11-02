def solution():
    """7 out of 40 people in a cafeteria are wearing checkered shirts. The rest of the people are wearing vertical stripes and horizontal stripes. The number of people wearing horizontal stripes is 4 times as many as the people wearing checkered shirts. How many people are wearing vertical stripes?"""
    checkered_shirts = 7
    horizontal_stripes = checkered_shirts * 4
    total_people = 40
    vertical_stripes = total_people - checkered_shirts - horizontal_stripes
    result = vertical_stripes
    return result

print(solution())