def solution():
    distance = 4  # The store is 4 miles away
    time_walk = distance / 2  # Tony takes 2 hours to walk to the store
    time_run = distance / 10  # Tony takes 0.4 hours (24 minutes) to run to the store
    days = 3  # Tony goes to the store on Sunday, Tuesday, and Thursday

    # Calculate the total time Tony spends getting to the store
    total_time = time_walk + (2 * time_run)  # Tony walks on Sunday and Thursday, and runs on Tuesday

    # Calculate the average time Tony spends getting to the store
    average_time = total_time / days
    result = average_time * 60  # Convert to minutes
    return result

print(solution())