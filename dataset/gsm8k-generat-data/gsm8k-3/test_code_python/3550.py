def solution():
    """Porter earns $8 per day and works 5 times a week. His manager is asking him to work an extra day that promises him an extra fifty percent on top of his daily rate. How much money will he earn after a month if he renders overtime every week?"""
    # Define Porter's daily rate and number of workdays per week
    DAILY_RATE = 8
    WORKDAYS_PER_WEEK = 5

    # Calculate Porter's weekly earnings without overtime
    weekly_earnings = DAILY_RATE * WORKDAYS_PER_WEEK

    # Calculate Porter's earnings with overtime for one week
    overtime_earnings = DAILY_RATE * 1.5
    total_earnings_with_overtime = weekly_earnings + overtime_earnings

    # Calculate Porter's monthly earnings with overtime
    monthly_earnings_with_overtime = total_earnings_with_overtime * 4

    # Display Porter's monthly earnings with overtime
    result = monthly_earnings_with_overtime
    return result

print(solution())