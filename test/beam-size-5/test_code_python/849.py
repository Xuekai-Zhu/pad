def solution():
    total_rooms = 90  # There are 90 rooms at the KozyInn Motel
    time_per_room = 20  # It takes housekeeping 20 minutes to clean each room
    total_time = total_rooms * time_per_room  # Calculate the total time it would take to clean one-half of the rooms

    # Calculate the time it would take to clean one-half of the rooms
    time_per_half_room = total_time / 2

    # Convert the time to hours
    time_in_hours = time_per_half_room / 60
    result = time_in_hours
    return result

print(solution())