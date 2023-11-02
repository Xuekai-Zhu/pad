def solution():
    # Calculate John's hourly rate with the 30% raise
    hourly_rate = 20 * 1.3

    # Calculate John's daily earnings
    daily_earnings = hourly_rate * 12

    # Calculate John's earnings in a 30 day month
    monthly_earnings = daily_earnings * 15  # John works every other day, so he works 15 days in a 30 day month

    result = monthly_earnings
    return result

print(solution())