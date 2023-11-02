def solution():
    
    # Define the time it takes to break in the new shoes and the number of days Jason can walk in a week
    WALKING_TIME = 240
    DAYS_PER_WEEK = 4

    # Calculate the total time Jason spends walking in three weeks
    total_walk_time = WALKING_TIME * DAYS_PER_WEEK

    # Calculate the time Jason spends walking each day
    walking_time_per_day = total_walk_time / 3

    # Display the time Jason spends walking each day
    result = walking_time_per_day
    return result

print(solution())