def solution():
    # Calculate the area of the fabric used for the living room curtains
    living_room_area = 4 * 6

    # Calculate the area of the fabric used for the bedroom curtains
    bedroom_area = 2 * 4

    # Calculate the total area of fabric used
    total_used_area = living_room_area + bedroom_area

    # Calculate the area of the remaining fabric
    remaining_area = (16 * 12) - total_used_area
    result = remaining_area
    return result

print(solution())