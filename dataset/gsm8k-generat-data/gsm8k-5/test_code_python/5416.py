def solution():
    current_width = 8  # The current width of the bathroom is 8 feet
    current_length = 96 / current_width  # Calculate the current length

    new_width = current_width + 4  # The new width will be 2 feet wider on each side
    new_length = current_length + 4  # The new length will be 2 feet longer on each side

    # Calculate the new area of the bathroom
    new_area = new_width * new_length
    result = new_area
    return result

print(solution())