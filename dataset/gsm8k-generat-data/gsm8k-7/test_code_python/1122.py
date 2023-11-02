def solution():
    original_days = 3
    added_days = 2
    hours_per_day = 2

    # Calculate the total number of days Tim runs now
    total_days = original_days + added_days

    # Calculate the total hours Tim runs per week
    total_hours = total_days * hours_per_day
    result = total_hours
    return result

print(solution())