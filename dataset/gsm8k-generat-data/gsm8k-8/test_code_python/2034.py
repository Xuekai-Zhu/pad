def solution():
    # Define the variables
    walk_time = 15
    train_time = 6 * 60
    total_time = 8 * 60
    wait_time = 2 * walk_time

    # Calculate the time it takes for the bus ride
    bus_time = total_time - train_time - wait_time - walk_time

    # Convert the bus time to minutes
    bus_time_minutes = bus_time % 60

    result = bus_time_minutes
    return result

print(solution())