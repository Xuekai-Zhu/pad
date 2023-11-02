def solution():
    room_height = 8  # feet
    additional_length = 5  # inches

    # Convert room height to inches
    room_height_inches = room_height * 12

    # Add additional length to the room height
    total_length_inches = room_height_inches + additional_length

    # Convert total length to feet
    total_length_feet = total_length_inches / 12
    result = total_length_feet
    return result

print(solution())