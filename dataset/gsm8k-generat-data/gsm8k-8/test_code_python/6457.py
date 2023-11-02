def solution():
    # Calculate the new dimensions of the first room
    new_length = 13 + 2
    new_width = 18 + 2

    # Calculate the area of the new room
    new_room_area = new_length * new_width

    # Calculate the total area of the four rooms
    total_area = (4 * new_room_area) + (2 * new_room_area)

    result = total_area
    return result

print(solution())