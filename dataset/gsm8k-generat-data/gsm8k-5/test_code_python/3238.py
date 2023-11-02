def solution():
    hill_distance = 900  # The hill is 900 feet tall
    uphill_speed = 9  # Jill can run uphill at a speed of 9 feet/second
    downhill_speed = 12  # Jill can run downhill at a speed of 12 feet/second

    # Calculate the time it takes Jill to run uphill
    uphill_time = hill_distance / uphill_speed

    # Calculate the time it takes Jill to run downhill
    downhill_time = hill_distance / downhill_speed

    # Calculate the total time it takes Jill to run up and down the hill
    total_time = uphill_time + downhill_time
    result = total_time
    return result

print(solution())