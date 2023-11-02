def solution():
    # Calculate the dimensions of the new room
    new_length = 13 + 2
    new_width = 18 + 2

    # Calculate the area of the new room
    new_area = new_length * new_width

    # Calculate the area of the 3 rooms of equal size
    equal_room_area = new_area * 3

    # Calculate the area of the room that is twice the size of the new room
    big_room_area = new_area * 2

    # Calculate the total area
    total_area = equal_room_area + big_room_area
    result = total_area
    return result

print(solution())