def solution():
    """Megan works eight hours a day and earns $7.50 per hour. If she works 20 days a month, how much will be her total earnings for two months of work?"""
    # Define the number of hours Megan works each day and her hourly rate
    hours_per_day = 8
    hourly_rate = 7.5

    # Define the number of days Megan works in a month
    days_per_month = 20

    # Calculate Megan's monthly earnings
    monthly_earnings = hours_per_day * hourly_rate * days_per_month

    # Calculate Megan's total earnings for two months of work
    total_earnings = monthly_earnings * 2

    result = total_earnings
    return result

print(solution())