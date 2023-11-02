def solution():
    """Luke is planning a trip to London and wants to see how long it will take him to travel there. He decides that he will take a bus to the town center, walk for 15 minutes to the train center, wait twice this long for the train to arrive, and then take the 6-hour train ride to London. If Luke’s entire trip takes him 8 hours, how many minutes does his bus ride take?"""
    # Define the time Luke spends walking and waiting for the train
    WALKING_TIME = 15
    WAITING_TIME = 30

    # Define the time Luke spends on the train
    TRAIN_TIME = 360 # 6 hours * 60 minutes/hour

    # Define the total time of Luke's trip
    TOTAL_TIME = 480 # 8 hours * 60 minutes/hour

    # Calculate the time Luke spends on the bus
    bus_time = TOTAL_TIME - WALKING_TIME - WAITING_TIME - TRAIN_TIME

    # Display the time Luke spends on the bus (in minutes)
    result = bus_time
    return result

print(solution())