def solution():
    """The size of a bathroom is 96 sq ft. If the width of the bathroom is 8 feet and the owner wants to extend it by 2 feet on each side, what is the new area of the bathroom?"""
    # Define the initial width and length of the bathroom
    initial_width = 8
    initial_length = 96 / initial_width

    # Define the extended width and length of the bathroom
    extended_width = initial_width + 4
    extended_length = initial_length + 4

    # Calculate the new area of the bathroom
    new_area = extended_width * extended_length

    result = new_area
    return result

print(solution())