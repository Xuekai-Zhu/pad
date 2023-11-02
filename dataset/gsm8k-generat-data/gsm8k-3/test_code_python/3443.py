def solution():
    """Hannah is trying to figure out how much she'll get paid this week. She makes $30/hour and works 18 hours per week. Her pay is docked $5 each time she's late. If she was late 3 times this week, how much does she get paid?"""
    # Define Hannah's hourly rate and hours worked
    HOURLY_RATE = 30
    HOURS_WORKED = 18

    # Define the amount docked from Hannah's pay for being late
    DOCKED_AMOUNT = 5

    # Define the number of times Hannah was late this week
    TIMES_LATE = 3

    # Calculate Hannah's total pay
    base_pay = HOURLY_RATE * HOURS_WORKED
    docked_pay = DOCKED_AMOUNT * TIMES_LATE
    total_pay = base_pay - docked_pay

    # Display Hannah's total pay
    result = total_pay
    return result

print(solution())