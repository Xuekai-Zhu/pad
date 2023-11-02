def solution():
    """Luke is planning a trip to London and wants to see how long it will take him to travel there. He decides that he will take a bus to the town center, walk for 15 minutes to the train center, wait twice this long for the train to arrive, and then take the 6-hour train ride to London. If Luke’s entire trip takes him 8 hours, how many minutes does his bus ride take?"""
    total_time = 8 * 60  # convert total time to minutes
    train_time = 6 * 60  # convert train time to minutes
    wait_time = 15 * 2  # calculate wait time for train
    bus_time = total_time - train_time - wait_time - 15  # subtract other times from total time and subtract walking time
    result = bus_time
    return result

print(solution())