def solution():
    """Our small city has two buses. Each bus can have a capacity of 1/6 as much as the train, which has a capacity of 120 people. What is the combined capacity of the two buses?"""
    # Define the capacity of the train
    TRAIN_CAPACITY = 120

    # Define the capacity of each bus as 1/6 of the train capacity
    BUS_CAPACITY = TRAIN_CAPACITY / 6

    # Calculate the combined capacity of the two buses
    combined_capacity = BUS_CAPACITY * 2

    # Display the combined capacity of the two buses
    result = combined_capacity
    return result

print(solution())