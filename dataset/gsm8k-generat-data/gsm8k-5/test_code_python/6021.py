def solution():
    # Calculate total time on the bus
    bus_time = 15 + 25  # 15 minutes waiting time and 25 minutes travel time

    # Calculate walk time
    walk_time = bus_time / 2

    # Calculate total travel time
    total_time = bus_time + walk_time

    # Convert to minutes
    total_minutes = total_time * 60
    result = total_minutes
    return result

print(solution())