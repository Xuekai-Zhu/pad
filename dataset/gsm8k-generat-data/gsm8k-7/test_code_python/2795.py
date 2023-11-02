def solution():
    current_bedroom = 309
    current_bathroom = 150
    new_room_multiplier = 2

    # Calculate the size of the new room
    new_room_size = (current_bedroom + current_bathroom) * new_room_multiplier

    result = new_room_size
    return result

print(solution())