def solution():
    # Calculate the total time for the first bus
    first_bus_time = 12 + 30

    # Calculate half of the total time for both buses
    half_total_time = (first_bus_time + first_bus_time / 2) / 2

    # Calculate the time for the second bus
    second_bus_time = half_total_time - first_bus_time / 2

    result = second_bus_time
    return result

print(solution())