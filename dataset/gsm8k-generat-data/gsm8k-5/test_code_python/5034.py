def solution():
    # Calculate the total number of hours in a day
    total_hours = 24

    # Calculate the total number of hours Jackie spends on work, exercise, and sleep
    total_used_hours = 8 + 3 + 8

    # Calculate the total free time Jackie has in a day
    free_time = total_hours - total_used_hours
    result = free_time
    return result

print(solution())