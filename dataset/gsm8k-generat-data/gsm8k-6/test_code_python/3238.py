def solution():
    # Calculate the time it takes Jill to run up the hill
    time_uphill = 900/9  # distance/speed

    # Calculate the time it takes Jill to run down the hill
    time_downhill = 900/12  # distance/speed

    # Calculate the total time it takes Jill to run up and down the hill
    total_time = time_uphill + time_downhill
    result = total_time
    return result

print(solution())