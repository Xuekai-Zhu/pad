def solution():
    """Our small city has two buses. Each bus can have a capacity of 1/6 as much as the train, which has a capacity of 120 people. What is the combined capacity of the two buses?"""
    train_capacity = 120
    bus_capacity = train_capacity / 6
    combined_capacity = bus_capacity * 2
    result = combined_capacity
    return result

print(solution())