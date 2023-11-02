def solution():
    """Mark builds an apartment that is 16 by 10 feet. There are 6 rooms in total. All the rooms are the same size except the living room which is as big as 3 other rooms. How big is the living room?"""
    # Define the area of the apartment
    apartment_area = 16 * 10

    # Calculate the area of each of the five regular rooms
    regular_room_area = (apartment_area - x) / 5

    # Calculate the area of the living room
    living_room_area = 3 * regular_room_area

    # Return the result
    result = living_room_area
    return result

print(solution())