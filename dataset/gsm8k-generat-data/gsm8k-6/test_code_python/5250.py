def solution():
    # Calculate the number of people wearing checkered shirts
    checkered_shirts = 7

    # Calculate the number of people wearing horizontal stripes
    horizontal_stripes = 4 * checkered_shirts

    # Calculate the total number of people
    total_people = 40

    # Calculate the number of people wearing vertical stripes
    vertical_stripes = total_people - checkered_shirts - horizontal_stripes

    result = vertical_stripes
    return result

print(solution())