def solution():
    """It starts raining at 7:00 and pours heavily until its stops at 17:00  on a particular day. On the second day, the rain takes 2 more hours than it took on the first day to stop. On the third day, the rain pours for twice the amount of time it took on the second day. Calculate the total time it was raining in the three days."""
    # Define the start and end times of the rain on the first day
    start_time = 7
    end_time_first_day = 17

    # Calculate the duration of rain on the first day
    duration_first_day = end_time_first_day - start_time

    # Calculate the end time of the rain on the second day
    end_time_second_day = end_time_first_day + duration_first_day + 2

    # Calculate the duration of rain on the second day
    duration_second_day = end_time_second_day - (start_time + end_time_first_day)

    # Calculate the duration of rain on the third day
    duration_third_day = duration_second_day * 2

    # Calculate the total duration of rain over the three days
    total_duration = duration_first_day + duration_second_day + duration_third_day

    # return the result
    result = total_duration
    return result

print(solution())