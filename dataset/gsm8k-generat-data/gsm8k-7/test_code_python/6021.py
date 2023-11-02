def solution():
    bus_travel_time = 25  # minutes
    bus_waiting_time = 15  # minutes
    walk_time = bus_travel_time / 2  # minutes

    total_travel_time = bus_travel_time + bus_waiting_time + walk_time
    result = total_travel_time
    return result

print(solution())