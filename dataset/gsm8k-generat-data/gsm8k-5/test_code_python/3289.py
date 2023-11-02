def solution():
    # Calculate the number of rooms on each floor in the first wing
    rooms_per_floor_wing1 = 6 * 32  # 6 halls each with 32 rooms

    # Calculate the total number of rooms in the first wing
    total_rooms_wing1 = rooms_per_floor_wing1 * 9  # 9 floors

    # Calculate the number of rooms on each floor in the second wing
    rooms_per_floor_wing2 = 9 * 40  # 9 halls each with 40 rooms

    # Calculate the total number of rooms in the second wing
    total_rooms_wing2 = rooms_per_floor_wing2 * 7  # 7 floors

    # Calculate the total number of rooms in the hotel
    total_rooms = total_rooms_wing1 + total_rooms_wing2
    result = total_rooms
    return result

print(solution())