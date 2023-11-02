def solution():
    # Calculate the area of one room
    room_area = (16*10) / 6  # total area of apartment is 16*10, divided by 6 rooms
    # Calculate the area of the living room
    living_room_area = room_area * 3  # living room is as big as 3 other rooms
    result = living_room_area
    return result

print(solution())