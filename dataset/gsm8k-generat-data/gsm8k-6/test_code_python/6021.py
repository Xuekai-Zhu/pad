def solution():
    # Calculate the total time Harry will spend traveling
    bus_journey_time = 15 + 25  # 15 minutes already passed and 25 minutes remaining
    walk_time = bus_journey_time / 2  # walk time is half the bus journey time
    total_travel_time = bus_journey_time + walk_time  # total travel time is bus journey time + walk time
    result = total_travel_time
    return result

print(solution())