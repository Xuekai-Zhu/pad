def solution():
    total_time_minutes = 3 * 60 + 36  # convert hours to minutes
    miles = 24

    # Calculate the average time (in minutes) per mile
    time_per_mile = total_time_minutes / miles
    result = time_per_mile
    return result

print(solution())