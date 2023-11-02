def solution():
    """Janice has been working part-time at a convenience store 5 days a week. She can earn $30 per day and can earn $15 more when she works a 2 hour overtime shift. If she works three overtime shifts this week, how much will she earn this week?"""
    # Define the daily wage and overtime wage
    DAILY_WAGE = 30
    OVERTIME_WAGE = 45

    # Define the number of days worked
    days_worked = 5

    # Define the number of overtime shifts worked
    overtime_shifts = 3

    # Calculate the regular earnings
    regular_earnings = days_worked * DAILY_WAGE

    # Calculate the overtime earnings
    overtime_earnings = overtime_shifts * OVERTIME_WAGE

    # Calculate the total earnings
    total_earnings = regular_earnings + overtime_earnings

    # return the result
    result = total_earnings
    return result

print(solution())