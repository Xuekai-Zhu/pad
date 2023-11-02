def solution():
    # Calculate the total number of days Tim runs per week now
    running_days = 3 + 2  # Tim used to run 3 times a week but added 2 extra days

    # Calculate the total number of hours Tim runs per day
    daily_hours = 1 + 1  # Tim runs 1 hour in the morning and 1 hour in the evening

    # Calculate the total number of hours Tim runs per week now
    total_hours = running_days * daily_hours

    result = total_hours
    return result

print(solution())