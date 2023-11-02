def solution():
    """An employee makes 30 dollars an hour for the first 40 hours in the workweek and an additional 50% for every hour above 40 in the week. If he works 6 hours for the first 3 days in the workweek and twice as many hours per day for the remaining 2 days, how much money did he make?"""
    # Define the regular hourly rate and the overtime hourly rate
    regular_rate = 30
    overtime_rate = regular_rate * 1.5

    # Calculate the total number of hours worked in the week
    total_hours = (6 * 3) + (2 * 2 * 8)

    # Calculate the total earnings for the first 40 hours
    earnings_regular = regular_rate * 40

    # Calculate the total earnings for the overtime hours
    earnings_overtime = (total_hours - 40) * overtime_rate

    # Calculate the total earnings for the week
    total_earnings = earnings_regular + earnings_overtime

    # return the result
    result = total_earnings
    return result

print(solution())