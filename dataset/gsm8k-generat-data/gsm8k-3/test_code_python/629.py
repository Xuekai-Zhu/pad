def solution():
    """A teacher teaches 5 periods a day and works 24 days a month. He is paid $5 per period. if he has been working for 6 months now how much has he earned in total?"""
    # Define the number of periods per day, number of working days per month, and monthly pay
    PERIODS_PER_DAY = 5
    WORKING_DAYS_PER_MONTH = 24
    MONTHLY_PAY = PERIODS_PER_DAY * WORKING_DAYS_PER_MONTH * 5

    # Calculate the total earnings over 6 months
    total_earnings = 6 * MONTHLY_PAY

    # Display the total earnings
    result = total_earnings
    return result

print(solution())