def solution():
    """Hans booked a room in a hotel. The hotel has 10 floors with 10 identical rooms on each floor. Because of an accident, the last floor is unavailable for the guests. Considering there are no other guests, in how many different rooms could Hans be checked in?"""
    # Define the number of floors and rooms per floor
    floors = 9
    rooms_per_floor = 10

    # Calculate the total number of available rooms
    total_rooms = floors * rooms_per_floor

    # return the result
    result = total_rooms
    return result

print(solution())