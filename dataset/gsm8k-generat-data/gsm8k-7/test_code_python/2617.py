def solution():
    apartment_length = 16
    apartment_width = 10
    num_rooms = 6

    # Calculate the total area of the apartment
    total_area = apartment_length * apartment_width

    # Calculate the area of one room
    room_area = total_area / num_rooms

    # Calculate the area of the living room
    living_room_area = room_area * 3

    result = living_room_area
    return result

print(solution())