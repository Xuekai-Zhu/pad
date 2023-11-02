def solution():
    first_bus_total_time = 12 + 30  # Jill spends 12 minutes waiting for her first bus and 30 minutes riding it
    second_bus_half_time = first_bus_total_time / 2  # Jill spends half the combined wait and trip time on her second bus

    # Calculate the total time spent on the second bus
    second_bus_total_time = second_bus_half_time + 12  # Jill spends 12 minutes waiting for her second bus
    result = second_bus_total_time
    return result

print(solution())