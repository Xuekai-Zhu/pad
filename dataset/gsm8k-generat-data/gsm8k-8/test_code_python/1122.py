def solution():
    # Define Tim's old and new running schedule
    old_days = 3
    new_days = 5

    # Calculate the total hours of running per day
    hours_per_day = 2

    # Calculate the total hours of running per week
    old_hours = old_days * hours_per_day * 7
    new_hours = new_days * hours_per_day * 7

    # Calculate the difference in hours between the old and new schedule
    diff_hours = new_hours - old_hours
    result = diff_hours
    return result

print(solution())