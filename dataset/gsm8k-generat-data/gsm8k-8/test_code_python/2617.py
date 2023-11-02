def solution():
    # Calculate the size of one room
    total_area = 16 * 10
    one_room_area = total_area / 6

    # Calculate the size of the living room
    living_room_area = one_room_area * 3

    result = living_room_area
    return result

print(solution())