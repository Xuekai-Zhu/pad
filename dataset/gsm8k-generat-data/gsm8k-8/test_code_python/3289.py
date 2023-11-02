def solution():
    # Calculate the number of rooms in the first wing
    rooms_in_first_wing = 9 * 6 * 32

    # Calculate the number of rooms in the second wing
    rooms_in_second_wing = 7 * 9 * 40

    # Calculate the total number of rooms in the hotel
    total_rooms = rooms_in_first_wing + rooms_in_second_wing
    result = total_rooms
    return result

print(solution())