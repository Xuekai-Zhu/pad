def solution():
    total_time = 8 * 60  # convert total time to minutes
    walk_time = 15  # Luke walks for 15 minutes
    train_time = 6 * 60  # the train ride takes 6 hours or 360 minutes
    wait_time = walk_time * 2  # Luke waits twice the time he walks for the train to arrive
    remaining_time = total_time - (walk_time + train_time + wait_time)  # calculate the time remaining after walking, waiting, and taking the train
    bus_time = remaining_time  # the remaining time is the bus ride time
    result = bus_time
    return result

print(solution())