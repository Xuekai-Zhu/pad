def solution():
    living_room_area = 4 * 6  # Area of fabric needed for living room curtains
    bedroom_area = 2 * 4  # Area of fabric needed for bedroom curtains
    total_area = living_room_area + bedroom_area  # Total area of fabric needed

    bolt_area = 16 * 12  # Area of the bolt of fabric
    remaining_area = bolt_area - total_area  # Area of fabric remaining

    result = remaining_area
    return result

print(solution())