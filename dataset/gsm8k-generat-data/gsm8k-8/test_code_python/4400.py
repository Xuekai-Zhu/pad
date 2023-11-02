def solution():
    # Calculate the distance traveled uphill and downhill
    uphill_distance = 5 * 0.6
    downhill_distance = 5 - uphill_distance

    # Calculate the time taken to travel uphill and downhill
    uphill_time = uphill_distance / 2
    downhill_time = downhill_distance / 3

    # Calculate the total time taken
    total_time = uphill_time + downhill_time

    # Convert the total time to minutes
    total_time_in_minutes = total_time * 60
    result = total_time_in_minutes
    return result

print(solution())