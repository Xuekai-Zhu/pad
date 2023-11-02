def solution():
    floors = 10  # The hotel has 10 floors
    rooms_per_floor = 10  # There are 10 identical rooms on each floor
    unavailable_floor = 10  # The last floor is unavailable for the guests

    # Calculate the total number of rooms in the hotel
    total_rooms = (floors - 1) * rooms_per_floor  # The last floor is unavailable, so we subtract it from the total number of floors

    result = total_rooms
    return result

print(solution())