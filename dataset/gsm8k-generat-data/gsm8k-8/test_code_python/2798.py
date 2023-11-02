def solution():
    # Calculate John's new hourly wage with the 30% raise
    new_hourly_wage = 20 * 1.3

    # Calculate John's daily earnings with the new hourly wage
    daily_earnings = new_hourly_wage * 12

    # Calculate John's earnings for a 30 day month
    monthly_earnings = daily_earnings * 15  # John works every other day, so 30 days ÷ 2 = 15

    result = monthly_earnings
    return result

print(solution())