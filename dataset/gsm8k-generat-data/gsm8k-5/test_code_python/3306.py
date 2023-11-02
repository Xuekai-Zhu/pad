def solution():
    minutes_per_day = 30  # Larry jogs for 30 minutes each day
    days_in_week_1 = 3  # Larry jogs for 3 days in the first week
    days_in_week_2 = 5  # Larry jogs for 5 days in the second week
    weeks = 2  # Larry is jogging for two weeks

    # Calculate the total time Larry spends jogging in minutes
    total_time_in_minutes = (minutes_per_day * days_in_week_1 * weeks) + (minutes_per_day * days_in_week_2 * weeks)

    # Convert the total time to hours
    total_time_in_hours = total_time_in_minutes / 60
    result = total_time_in_hours
    return result

print(solution())