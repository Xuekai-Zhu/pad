def solution():
    # Calculate the total time it takes for Rob to get to the park
    rob_time = 1

    # Calculate the time it takes for Mark to get to the park
    mark_time = 3 * rob_time

    # Calculate the departure time for Mark
    mark_departure = 11 - mark_time
    result = mark_departure
    return result

print(solution())