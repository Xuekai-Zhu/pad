def solution():
    """James has a room that is 13 feet by 18 feet.  He increases each dimension by 2 feet.  He then builds 3 more rooms of equal size and 1 room of twice that size.  How much area does he have?"""
    # Define the dimensions of James' original room
    length = 13
    width = 18

    # Increase the dimensions of the room
    new_length = length + 2
    new_width = width + 2

    # Calculate the area of the new room
    new_area = new_length * new_width

    # Calculate the area of all four rooms
    total_area = new_area * 4

    # Calculate the area of the fifth room
    fifth_room_area = 2 * new_area

    # Add the area of all five rooms together
    total_area += fifth_room_area

    # Display the total area
    result = total_area
    return result

print(solution())