def solution():
    # Define the original width and length of the bathroom
    original_width = 8
    original_length = 96 / original_width

    # Calculate the new width and length of the bathroom
    new_width = original_width + 4  # adding 2 feet on each side
    new_length = original_length + 4

    # Calculate the new area of the bathroom
    new_area = new_width * new_length
    result = new_area
    return result

print(solution())