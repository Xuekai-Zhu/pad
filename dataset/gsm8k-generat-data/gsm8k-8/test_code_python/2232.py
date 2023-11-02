def solution():
    # Calculate time spent on Monday
    monday_time = 6 * 0.5

    # Calculate time spent on Tuesday
    tuesday_time = 3 * 1

    # Calculate time spent on Wednesday
    wednesday_time = 2 * tuesday_time

    # Calculate total time spent
    total_time = monday_time + tuesday_time + wednesday_time

    # Convert total time to hours
    total_time_hours = total_time / 60

    result = total_time_hours
    return result

print(solution())