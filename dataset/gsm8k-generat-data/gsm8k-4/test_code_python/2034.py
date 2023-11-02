def solution():
    """Luke is planning a trip to London and wants to see how long it will take him to travel there. He decides that he will take a bus to the town center, walk for 15 minutes to the train center, wait twice this long for the train to arrive, and then take the 6-hour train ride to London. If Luke’s entire trip takes him 8 hours, how many minutes does his bus ride take?"""
    # Define the time it takes Luke to walk to the train center
    walk_time = 15

    # Define the time Luke waits for the train to arrive
    train_wait_time = walk_time * 2

    # Define the time it takes for the train ride to London
    train_ride_time = 6 * 60

    # Define the total time of Luke's trip
    total_time = 8 * 60

    # Calculate the time of the bus ride
    bus_ride_time = total_time - walk_time - train_wait_time - train_ride_time

    # return the result
    result = bus_ride_time
    return result

print(solution())