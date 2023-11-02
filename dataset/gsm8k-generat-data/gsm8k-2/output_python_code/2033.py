def solution():
    """Luke is planning a trip to London and wants to see how long it will take him to travel there. He decides that he will take a bus to the town center, walk for 15 minutes to the train center, wait twice this long for the train to arrive, and then take the 6-hour train ride to London. If Luke’s entire trip takes him 8 hours, how many minutes does his bus ride take?"""
    total_travel_time = 8*60 # convert hours to minutes
    train_ride_time = 6*60 # convert hours to minutes
    wait_time = 2*15 # twice the time of walking to the train center
    bus_walk_time = 15
    bus_ride_time = total_travel_time - train_ride_time - wait_time - bus_walk_time
    result = bus_ride_time
    return result

print(solution())