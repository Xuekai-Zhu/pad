def solution():
    train_capacity = 120  # The train has a capacity of 120 people
    bus_capacity = train_capacity / 6  # Each bus has a capacity of 1/6 of the train's capacity
    total_bus_capacity = bus_capacity * 2  # There are two buses in the city

    result = total_bus_capacity
    return result

print(solution())