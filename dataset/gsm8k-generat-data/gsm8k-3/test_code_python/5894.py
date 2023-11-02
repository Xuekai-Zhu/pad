def solution():
    """An employee makes 30 dollars an hour for the first 40 hours in the workweek and an additional 50% for every hour above 40 in the week.  If he works 6 hours for the first 3 days in the workweek and twice as many hours per day for the remaining 2 days, how much money did he make?"""

    # Define regular rate and overtime rate multiplier
    REGULAR_RATE = 30
    OVERTIME_MULTIPLIER = 1.5

    # Calculate total hours worked
    total_hours = (6 * 3) + (2 * 2 * 8)

    # Calculate total earnings
    if total_hours <= 40:
        earnings = total_hours * REGULAR_RATE
    else:
        regular_hours = 40
        overtime_hours = total_hours - 40
        regular_earnings = regular_hours * REGULAR_RATE
        overtime_earnings = overtime_hours * REGULAR_RATE * OVERTIME_MULTIPLIER
        earnings = regular_earnings + overtime_earnings

    # Display total earnings
    result = earnings
    return result

print(solution())