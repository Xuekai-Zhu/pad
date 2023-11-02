def solution():
    hours_per_day = 8  # Megan works 8 hours a day
    hourly_rate = 7.5  # Megan earns $7.50 per hour
    working_days_per_month = 20  # Megan works 20 days a month

    # Calculate Megan's total earnings for one month of work
    total_earnings_per_month = hours_per_day * hourly_rate * working_days_per_month

    # Calculate Megan's total earnings for two months of work
    total_earnings_two_months = 2 * total_earnings_per_month

    result = total_earnings_two_months
    return result

print(solution())