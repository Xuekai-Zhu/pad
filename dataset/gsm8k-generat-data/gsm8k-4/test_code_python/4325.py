def solution():
    """To get to the library, Jill spends 12 minutes waiting for her first bus, 30 minutes riding on her first bus, and half the combined wait and trip time on her second bus. How many minutes does her second bus ride take?"""
    # Define the total time for the first bus
    first_bus_time = 12 + 30

    # Calculate the total time for the second bus
    second_bus_time = (first_bus_time / 2)

    # Display the result
    result = second_bus_time
    return result

print(solution())