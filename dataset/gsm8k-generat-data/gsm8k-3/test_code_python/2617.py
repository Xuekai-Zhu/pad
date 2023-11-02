def solution():
    """Mark builds an apartment that is 16 by 10 feet.  There are 6 rooms in total.  All the rooms are the same size except the living room which is as big as 3 other rooms.  How big is the living room?"""
    # Define the total number of rooms
    total_rooms = 6

    # Define the dimensions of the apartment
    width = 16
    length = 10

    # Calculate the area of the apartment
    apartment_area = width * length

    # Calculate the area of all the rooms except the living room
    other_rooms_area = (total_rooms - 1) * (apartment_area / total_rooms)

    # Calculate the area of the living room
    living_room_area = apartment_area - other_rooms_area

    # Display the area of the living room
    result = living_room_area
    return result

print(solution())