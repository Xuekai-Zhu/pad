def solution():
    # Calculate Mitch's earnings for weekdays and weekends separately
    weekday_earnings = 5 * 3 * 5  # 5 hours a day, 5 days a week, $3 per hour
    weekend_earnings = 3 * 2 * 2 * 2  # 3 hours a day, 2 days a week, $3 per hour (doubled on weekends)

    # Calculate the total earnings for the week
    total_earnings = weekday_earnings + weekend_earnings
    result = total_earnings
    return result

print(solution())