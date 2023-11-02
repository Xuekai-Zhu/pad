def solution():
    """Our small city has two buses. Each bus can have a capacity of 1/6 as much as the train, which has a capacity of 120 people. What is the combined capacity of the two buses?"""
    # Define the train's capacity and the ratio of the bus capacity to the train capacity
    train_capacity = 120
    bus_to_train_ratio = 1/6

    # Calculate the capacity of one bus
    bus_capacity = train_capacity * bus_to_train_ratio

    # Calculate the combined capacity of the two buses
    combined_capacity = bus_capacity * 2

    # Return the result
    result = combined_capacity
    return result

print(solution())