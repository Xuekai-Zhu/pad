def solution():
    """Hans booked a room in a hotel. The hotel has 10 floors with 10 identical rooms on each floor. Because of an accident, the last floor is unavailable for the guests. Considering there are no other guests, in how many different rooms could Hans be checked in?"""
    # Define the total number of rooms in the hotel
    total_rooms = 10 * 10

    # Define the number of unavailable rooms
    unavailable_rooms = 10

    # Calculate the number of available rooms
    available_rooms = total_rooms - unavailable_rooms

    # Return the result
    result = available_rooms
    return result

print(solution())