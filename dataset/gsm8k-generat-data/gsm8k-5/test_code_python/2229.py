def solution():
    hourly_rate = 2  # Zainab earns $2 per hour
    hours_per_day = 4  # Zainab works 4 hours per day
    days_per_week = 3  # Zainab works 3 days per week
    weeks = 4  # Zainab works for 4 weeks

    # Calculate the total number of hours Zainab works
    total_hours = hours_per_day * days_per_week * weeks

    # Calculate Zainab's total earnings
    total_earnings = hourly_rate * total_hours
    result = total_earnings
    return result

print(solution())