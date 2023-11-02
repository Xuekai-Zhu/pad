def solution():
    """Linda is building a new hotel with two wings. The first wing has 9 floors and each floor has 6 halls each with 32 rooms. The second wing has 7 floors each with 9 halls with 40 rooms each. How many rooms are in the hotel total?"""
    # Define the number of floors, halls, and rooms per hall in each wing
    WING1_FLOORS = 9
    WING1_HALLS = 6
    WING1_ROOMS_PER_HALL = 32
    WING2_FLOORS = 7
    WING2_HALLS = 9
    WING2_ROOMS_PER_HALL = 40

    # Calculate the number of rooms in the first wing
    wing1_rooms = WING1_FLOORS * WING1_HALLS * WING1_ROOMS_PER_HALL

    # Calculate the number of rooms in the second wing
    wing2_rooms = WING2_FLOORS * WING2_HALLS * WING2_ROOMS_PER_HALL

    # Calculate the total number of rooms in the hotel
    total_rooms = wing1_rooms + wing2_rooms

    # Display the total number of rooms
    result = total_rooms
    return result

print(solution())