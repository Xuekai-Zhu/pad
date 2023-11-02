def solution():
    """Bill gets paid $20 every hour he works up to a total of 40 hours, after which he gets paid double that amount per hour.  How much does Bill get paid for a 50-hour workweek?"""
    # Define the regular pay rate and the overtime pay rate
    REGULAR_RATE = 20
    OVERTIME_RATE = 40

    # Define the number of hours worked
    hours_worked = 50

    # Calculate the total pay
    if hours_worked <= 40:
        total_pay = hours_worked * REGULAR_RATE
    else:
        regular_pay = 40 * REGULAR_RATE
        overtime_hours = hours_worked - 40
        overtime_pay = overtime_hours * (2 * REGULAR_RATE)
        total_pay = regular_pay + overtime_pay

    # Display the total pay
    result = total_pay
    return result

print(solution())