def solution():
    store_distance = 4  # miles
    walk_speed = 2  # MPH
    run_speed = 10  # MPH

    # Calculate the time it takes to walk to the store
    walk_time = store_distance / walk_speed  # hours

    # Calculate the time it takes to run to the store
    run_time = store_distance / run_speed  # hours

    # Calculate the total time spent to get to the store
    total_time = (walk_time * 2) + run_time  # Sunday, Tuesday, and Thursday

    # Convert the total time to minutes and calculate the average
    average_time = (total_time * 60) / 3  # 3 days
    result = average_time
    return result

print(solution())