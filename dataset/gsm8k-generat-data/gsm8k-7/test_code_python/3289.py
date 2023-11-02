def solution():
    # Calculate the total number of rooms in the first wing
    first_wing_rooms = 9 * 6 * 32

    # Calculate the total number of rooms in the second wing
    second_wing_rooms = 7 * 9 * 40

    # Calculate the total number of rooms in the hotel
    total_rooms = first_wing_rooms + second_wing_rooms
    result = total_rooms
    return result

print(solution())