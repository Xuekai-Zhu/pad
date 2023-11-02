def solution():
    """Janice has been working part-time at a convenience store 5 days a week. She can earn $30 per day and can earn $15 more when she works a 2 hour overtime shift. If she works three overtime shifts this week, how much will she earn this week?"""
    # Define Janice's daily rate and overtime pay
    DAILY_RATE = 30
    OVERTIME_PAY = 15

    # Define the number of work days in a week
    WORK_DAYS = 5

    # Define the number of overtime shifts Janice works
    OVERTIME_SHIFTS = 3

    # Calculate Janice's regular earnings
    regular_earnings = DAILY_RATE * WORK_DAYS

    # Calculate Janice's overtime earnings
    overtime_earnings = OVERTIME_PAY * OVERTIME_SHIFTS * 2

    # Calculate Janice's total earnings for the week
    total_earnings = regular_earnings + overtime_earnings

    # Display Janice's total earnings
    result = total_earnings
    return result

print(solution())