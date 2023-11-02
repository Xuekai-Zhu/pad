def solution():
    total_distance = 5  # The trail is 5 miles long
    uphill_distance = total_distance * 0.6  # 60% of the trail is uphill
    downhill_distance = total_distance - uphill_distance  # The rest of the trail is downhill

    # Calculate the time it takes Roberto to hike uphill
    time_uphill = uphill_distance / 2

    # Calculate the time it takes Roberto to hike downhill
    time_downhill = downhill_distance / 3

    # Calculate the total time it takes Roberto to complete the hike in minutes
    total_time = (time_uphill + time_downhill) * 60

    result = total_time
    return result

print(solution())