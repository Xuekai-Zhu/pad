def solution():
    # Calculate John's new hourly wage after his raise
    new_wage = 20 * 1.3  # 30% raise from $20 per hour

    # Calculate John's daily earnings
    daily_earnings = new_wage * 12  # 12 hours worked every other day

    # Calculate John's earnings for a 30-day month
    earnings_in_month = daily_earnings * 15  # John works 15 days in a 30-day month

    result = earnings_in_month
    return result

print(solution())