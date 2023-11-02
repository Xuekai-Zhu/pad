def solution():
    total_trip_time = 8 * 60  # convert total trip time to minutes
    train_ride_time = 6 * 60  # convert train ride time to minutes
    walk_time = 15
    train_wait_time = walk_time * 2
    bus_time = total_trip_time - train_ride_time - walk_time - train_wait_time
    result = bus_time
    return result

print(solution())