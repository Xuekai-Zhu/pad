def solution():
    initial_width = 8
    initial_area = 96
    extension = 2

    # Calculate the length of the initial bathroom
    initial_length = initial_area / initial_width

    # Calculate the new width of the bathroom
    new_width = initial_width + (2 * extension)

    # Calculate the new area of the bathroom
    new_area = new_width * initial_length

    result = new_area
    return result

print(solution())