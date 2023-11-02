def solution():
    trail_length = 5
    uphill_speed = 2
    downhill_speed = 3
    uphill_distance = trail_length * 0.6
    downhill_distance = trail_length - uphill_distance

    # Calculate the time it takes to travel uphill
    uphill_time = uphill_distance / uphill_speed

    # Calculate the time it takes to travel downhill
    downhill_time = downhill_distance / downhill_speed

    # Calculate the total time for the hike in minutes
    total_time = uphill_time + downhill_time
    total_time_minutes = total_time * 60
    result = total_time_minutes
    return result

print(solution())