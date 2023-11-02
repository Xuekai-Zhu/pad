def solution():
    # Calculate the total time Luke spends walking and waiting for the train
    wait_time = 15 * 2  # waiting time is twice the walking time
    total_walk_wait_time = 15 + wait_time

    # Calculate the total time Luke spends on the train journey
    train_time = 6 * 60  # 6 hours converted to minutes

    # Calculate the total time Luke spends on the bus ride
    total_trip_time = total_walk_wait_time + train_time
    bus_ride_time = (8 * 60) - total_trip_time  # total trip time is 8 hours converted to minutes

    result = bus_ride_time
    return result

print(solution())