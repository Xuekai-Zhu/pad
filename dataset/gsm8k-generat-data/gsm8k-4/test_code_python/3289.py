def solution():
    """Linda is building a new hotel with two wings. The first wing has 9 floors and each floor has 6 halls each with 32 rooms. The second wing has 7 floors each with 9 halls with 40 rooms each. How many rooms are in the hotel total?"""
    # Calculate the number of rooms in the first wing
    first_wing_rooms = 9 * 6 * 32

    # Calculate the number of rooms in the second wing
    second_wing_rooms = 7 * 9 * 40

    # Calculate the total number of rooms in the hotel
    total_rooms = first_wing_rooms + second_wing_rooms

    result = total_rooms
    return result

print(solution())