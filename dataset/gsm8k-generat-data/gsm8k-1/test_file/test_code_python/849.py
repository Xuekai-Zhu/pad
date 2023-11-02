def solution():
    """There are 90 rooms at the KozyInn Motel. It takes housekeeping 20 minutes to clean each room. How many hours would it take to clean one-half of the rooms?"""
    total_rooms = 90
    time_per_room = 20 / 60 #in hours
    half_rooms = total_rooms / 2
    total_time = half_rooms * time_per_room
    result = total_time
    return result

print(solution())