def solution():
    num_floors = 4
    num_rooms_per_floor = 10
    time_per_room = 6  # in hours
    payment_per_hour = 15

    # Calculate the total number of rooms in the building
    total_rooms = num_floors * num_rooms_per_floor

    # Calculate the total time it will take Legacy to clean all the rooms
    total_time = total_rooms * time_per_room

    # Calculate the total amount of money Legacy will earn for cleaning all the rooms
    total_earnings = total_time * payment_per_hour
    result = total_earnings
    return result

print(solution())