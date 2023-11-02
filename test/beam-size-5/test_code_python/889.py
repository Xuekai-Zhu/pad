def solution():
    hours_per_day = 8  # Mark works at his job for 8 hours per day
    days_per_week = 5  # Mark works for 5 days per week
    hourly_rate_original = 10  # Mark used to make $10 per hour
    hourly_rate_new = 2  # Mark raised his pay by $2 per hour

    # Calculate Mark's new hourly rate
    new_hourly_rate = hourly_rate_original + hourly_rate_new

    # Calculate Mark's weekly earnings
    weekly_earnings = new_hourly_rate * hours_per_day * days_per_week
    result = weekly_earnings
    return result

print(solution())