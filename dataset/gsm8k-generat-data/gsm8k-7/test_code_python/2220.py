def solution():
    luke_bus_time = 70
    paula_bus_time = 3/5 * luke_bus_time
    luke_bike_time = luke_bus_time * 5

    # Calculate the total time for Luke
    luke_total_time = luke_bus_time + luke_bike_time

    # Calculate the total time for Paula
    paula_total_time = paula_bus_time * 2

    # Calculate the total time for both of them
    total_time = luke_total_time + paula_total_time
    result = total_time
    return result

print(solution())