def solution():
    # Calculate the time it takes to walk to the store on Sunday
    walk_time_sunday = 4 / 2

    # Calculate the time it takes to run to the store on Tuesday and Thursday
    run_time_weekdays = 4 / 10

    # Calculate the total time Tony spends getting to the store on all three days
    total_time = walk_time_sunday + 2 * run_time_weekdays

    # Calculate the average time in minutes
    average_time = total_time * 60 / 3
    result = average_time
    return result

print(solution())