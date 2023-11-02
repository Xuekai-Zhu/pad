def solution():
    """Porter earns $8 per day and works 5 times a week. His manager is asking him to work an extra day that promises him an extra fifty percent on top of his daily rate. How much money will he earn after a month if he renders overtime every week?"""
    # Define the base pay and overtime pay rates
    BASE_PAY_RATE = 8
    OVERTIME_PAY_RATE = BASE_PAY_RATE * 1.5

    # Define the number of working days in a week and in a month
    WEEKLY_WORKDAYS = 6
    MONTHLY_WORKDAYS = 4 * WEEKLY_WORKDAYS

    # Calculate Porter's total earnings for a week with overtime
    weekly_earnings = (BASE_PAY_RATE * WEEKLY_WORKDAYS) + (OVERTIME_PAY_RATE)

    # Calculate Porter's total earnings for a month with overtime
    monthly_earnings = weekly_earnings * MONTHLY_WORKDAYS

    result = monthly_earnings
    return result

print(solution())