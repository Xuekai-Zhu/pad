def solution():
    # Calculate the time Tony spends on Sunday, Tuesday, and Thursday
    sunday_time = 4 / 2  # Tony walks on Sunday
    tuesday_time = 4 / 10  # Tony runs on Tuesday
    thursday_time = 4 / 10  # Tony runs on Thursday
    total_time = sunday_time + tuesday_time + thursday_time  # Total time for 3 days
    average_time = (total_time / 3) * 60  # Average time in minutes
    result = average_time
    return result

print(solution())