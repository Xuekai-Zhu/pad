def solution():
    total_people = 40
    checkered_shirts = 7

    # Calculate the number of people wearing horizontal stripes
    horizontal_stripes = 4 * checkered_shirts

    # Calculate the total number of people not wearing checkered shirts
    other_people = total_people - checkered_shirts

    # Calculate the number of people wearing vertical stripes
    vertical_stripes = other_people - horizontal_stripes
    result = vertical_stripes
    return result

print(solution())