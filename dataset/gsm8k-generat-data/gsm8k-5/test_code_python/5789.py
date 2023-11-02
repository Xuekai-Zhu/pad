def solution():
    # Calculate the time spent walking on Monday
    time_on_monday = 6 / 2  # Distance is 6 miles and speed is 2 miles per hour

    # Calculate the time spent walking on Wednesday
    time_on_wednesday = 6 / 3  # Distance is 6 miles and speed is 3 miles per hour

    # Calculate the time spent running on Friday
    time_on_friday = 6 / 6  # Distance is 6 miles and speed is 6 miles per hour

    # Calculate the total time spent exercising in a week
    total_time = time_on_monday + time_on_wednesday + time_on_friday
    result = total_time
    return result

print(solution())