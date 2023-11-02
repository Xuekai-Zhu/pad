def solution():
    # Define the given information
    checkered_shirts = 7
    total_people = 40
    horizontal_stripes = 4 * checkered_shirts

    # Calculate the number of people wearing vertical stripes
    vertical_stripes = total_people - (checkered_shirts + horizontal_stripes)
    result = vertical_stripes
    return result

print(solution())