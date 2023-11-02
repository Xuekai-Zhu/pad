def solution():
    # Calculate the total time Colin took to run 4 miles
    total_time = 6 + 2*5 + 4  # first mile in 6 minutes, next two miles in 5 minutes each, fourth mile in 4 minutes
    # Calculate the average time it took him to run a mile
    average_time_per_mile = total_time / 4
    result = average_time_per_mile
    return result

print(solution())