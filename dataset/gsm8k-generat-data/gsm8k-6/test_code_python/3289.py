def solution():
    # Calculate the number of rooms in the first wing
    rooms_wing1 = 9 * 6 * 32  # 9 floors, 6 halls/floor, 32 rooms/hall

    # Calculate the number of rooms in the second wing
    rooms_wing2 = 7 * 9 * 40  # 7 floors, 9 halls/floor, 40 rooms/hall

    # Calculate the total number of rooms in the hotel
    total_rooms = rooms_wing1 + rooms_wing2

    result = total_rooms
    return result

print(solution())