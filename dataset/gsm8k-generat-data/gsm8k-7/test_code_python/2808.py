def solution():
    rob_time = 1  # in hours
    mark_time = 3 * rob_time
    rob_departure = 11  # in hours
    mark_arrival = rob_departure + rob_time
    mark_departure = mark_arrival - mark_time
    result = mark_departure
    return result

print(solution())