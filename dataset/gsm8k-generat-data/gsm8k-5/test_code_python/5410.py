def solution():
    # Calculate the time it takes to hike the 20-mile downhill trail
    time_downhill = 20 / 5  # 20 miles at 5 miles per hour

    # Calculate the time it takes to hike the 6-mile uphill trail
    time_uphill = 4 + (2 * (12 / 3))  # 4 hours hiking uphill, plus 2 one-hour breaks

    # Compare the two times to determine the faster hike
    if time_downhill < time_uphill:
        faster_time = time_downhill
    else:
        faster_time = time_uphill

    # Calculate the time difference between the two hikes
    time_difference = abs(time_downhill - time_uphill)
    result = time_difference
    return result

print(solution())