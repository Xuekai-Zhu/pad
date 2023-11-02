def solution():
    """Hans booked a room in a hotel. The hotel has 10 floors with 10 identical rooms on each floor. Because of an accident, the last floor is unavailable for the guests.
    Considering there are no other guests, in how many different rooms could Hans be checked in?"""
    
    available_floors = 9
    rooms_per_floor = 10
    total_rooms = available_floors * rooms_per_floor
    result = total_rooms
    return result

print(solution())