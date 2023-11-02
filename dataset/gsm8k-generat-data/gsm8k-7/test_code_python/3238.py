def solution():
    uphill_rate = 9  # feet/second
    downhill_rate = 12  # feet/second
    hill_distance = 900  # feet

    # Calculate the time it takes Jill to run up the hill
    uphill_time = hill_distance / uphill_rate

    # Calculate the time it takes Jill to run down the hill
    downhill_time = hill_distance / downhill_rate

    # Calculate the total time it takes Jill to run up and down the hill
    total_time = uphill_time + downhill_time
    result = total_time
    return result

print(solution())