def solution():
    num_bridesmaids = 5
    time_per_dress = 12 # in hours
    hours_per_week = 4

    # Calculate the total time to sew all the dresses
    total_time = time_per_dress * num_bridesmaids

    # Calculate the number of weeks it will take Sheena to complete the dresses
    num_weeks = total_time / hours_per_week
    result = num_weeks
    return result

print(solution())