def solution():
    mile_time_old = 10 # minutes
    mile_time_new = 13 # minutes
    distance = 5 # miles

    # Calculate the total time it would take to run 5 miles in her old shoes
    time_old = mile_time_old * distance

    # Calculate the total time it would take to run 5 miles in her new shoes
    time_new = mile_time_new * distance

    # Calculate the difference in time between the two scenarios
    time_diff = time_new - time_old
    result = time_diff
    return result

print(solution())