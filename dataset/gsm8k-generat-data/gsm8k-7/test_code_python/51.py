def solution():
    living_room_area = 4 * 6
    bedroom_area = 2 * 4
    bolt_area = 16 * 12

    # Calculate the total area of fabric used
    total_area_used = living_room_area + bedroom_area

    # Calculate the amount of fabric left
    fabric_left = bolt_area - total_area_used
    result = fabric_left
    return result

print(solution())