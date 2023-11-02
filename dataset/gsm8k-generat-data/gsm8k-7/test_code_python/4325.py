def solution():
    first_bus_wait_time = 12
    first_bus_ride_time = 30

    # Calculate the total time for the first bus trip
    total_first_bus_time = first_bus_wait_time + first_bus_ride_time

    # Calculate the time spent waiting and riding for the second bus
    second_bus_wait_ride_time = total_first_bus_time / 2

    # Calculate the total time for the second bus trip
    second_bus_ride_time = second_bus_wait_ride_time

    result = second_bus_ride_time
    return result

print(solution())