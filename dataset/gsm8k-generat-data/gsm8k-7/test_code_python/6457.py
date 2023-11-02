def solution():
    original_length = 13
    original_width = 18
    increase_amount = 2
    num_equal_rooms = 3
    double_room_factor = 2

    # Calculate the new dimensions of James' original room
    new_length = original_length + increase_amount
    new_width = original_width + increase_amount

    # Calculate the area of James' original room
    original_area = original_length * original_width

    # Calculate the area of James' new room
    new_area = new_length * new_width

    # Calculate the total area of all of James' equal-sized rooms
    total_equal_rooms_area = new_area * num_equal_rooms

    # Calculate the area of James' double-sized room
    double_room_area = double_room_factor * new_area

    # Calculate the total area of all of James' rooms
    total_area = original_area + total_equal_rooms_area + double_room_area
    result = total_area
    return result

print(solution())