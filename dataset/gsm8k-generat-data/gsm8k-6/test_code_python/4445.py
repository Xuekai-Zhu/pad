def solution():
    # Calculate the total area of the walls Matt needs to paint
    living_room_area = 4 * (40*10)  # there are four walls in a square room
    bedroom_area = 2 * (10*10) + 2 * (12*10)  # there are four walls in a rectangular room
    total_area = living_room_area + bedroom_area
    result = total_area
    return result

print(solution())