def solution():
    # Calculate the time spent on walking and running in a week
    time_walking_on_monday = 6 / 2  # distance of 6 miles, walking at 2 miles per hour
    time_walking_on_wednesday = 6 / 3  # distance of 6 miles, walking at 3 miles per hour
    time_running_on_friday = 6 / 6  # distance of 6 miles, running at 6 miles per hour
    total_time = time_walking_on_monday + time_walking_on_wednesday + time_running_on_friday
    result = total_time
    return result

print(solution())