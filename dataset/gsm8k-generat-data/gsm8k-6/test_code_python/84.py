def solution():
    # Calculate the total number of rooms in the hotel
    total_rooms = 10 * 10
    # Calculate the number of rooms on the last floor
    last_floor_rooms = 10
    # Calculate the number of available rooms
    available_rooms = total_rooms - last_floor_rooms
    result = available_rooms
    return result

print(solution())