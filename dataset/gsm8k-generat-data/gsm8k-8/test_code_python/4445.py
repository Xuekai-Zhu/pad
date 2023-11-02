def solution():
    # Calculate the area of the living room walls
    living_room_area = 4 * 40 * 10

    # Calculate the area of the bedroom walls
    bedroom_area = 2 * (10 * 10) + 2 * (12 * 10)

    # Calculate the total area to be painted
    total_area = living_room_area + bedroom_area
    result = total_area
    return result

print(solution())