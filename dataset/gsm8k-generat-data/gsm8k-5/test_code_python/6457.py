def solution():
    original_area = 13 * 18  # Area of the original room
    new_length = 13 + 2  # Length of the new room
    new_width = 18 + 2  # Width of the new room
    new_area = new_length * new_width  # Area of each new room
    total_area = (new_area * 4) + (new_area * 2)  # Total area of all rooms

    result = total_area
    return result

print(solution())