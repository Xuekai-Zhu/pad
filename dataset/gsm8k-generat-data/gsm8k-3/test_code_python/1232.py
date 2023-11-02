def solution():
    """Megan works eight hours a day and earns $7.50 per hour.  If she works 20 days a month, how much will be her total earnings for two months of work?"""
    # Define the number of hours Megan works per day and her hourly rate
    HOURS_PER_DAY = 8
    HOURLY_RATE = 7.5

    # Define the number of days Megan works per month
    DAYS_PER_MONTH = 20

    # Calculate Megan's earnings for one month
    earnings_per_month = HOURS_PER_DAY * HOURLY_RATE * DAYS_PER_MONTH

    # Calculate Megan's earnings for two months
    total_earnings = earnings_per_month * 2

    # Display Megan's total earnings
    result = total_earnings
    return result

print(solution())