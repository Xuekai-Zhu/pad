def solution():
    daily_earnings_regular = 8 * 5  # Porter earns $8 per day and works 5 times a week regularly
    daily_earnings_overtime = 8 * 1.5  # Porter earns 50% more for one day of overtime
    total_days_in_month = 30  # Assuming a month has 30 days

    # Calculate the total earnings for the month with overtime
    total_earnings_overtime = daily_earnings_regular + (daily_earnings_overtime * 4)  # 4 overtime days in a month
    result = total_earnings_overtime
    return result

print(solution())