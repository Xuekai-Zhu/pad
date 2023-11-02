def solution():
    hourly_rate = 2  # John gets paid $2 per hour
    hours_per_day = 5  # John works 5 hours per day
    days_per_week = 4  # John works 4 days per week
    total_hours = hours_per_day * days_per_week  # John wants to save $80

    # Calculate the amount of money John will save per week
    savings_per_week = total_hours * hourly_rate

    # Calculate the number of weeks it will take John to save $80
    weeks_to_save = 80 / savings_per_week
    result = weeks_to_save
    return result

print(solution())