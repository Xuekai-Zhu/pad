def solution():
    """John works 12 hours every other day.  He gets a 30% raise from his former $20 an hour job.  How much does he make in a 30 day month?"""
    # Define John's hourly rate and hours worked every other day
    HOURLY_RATE = 20 * 1.3
    HOURS_EVERY_OTHER_DAY = 12

    # Calculate the number of days John works in a 30 day month
    days_worked = 30 / 2

    # Calculate the total number of hours John works in a 30 day month
    total_hours_worked = days_worked * HOURS_EVERY_OTHER_DAY

    # Calculate John's total earnings in a 30 day month
    total_earnings = HOURLY_RATE * total_hours_worked

    # Display John's total earnings
    result = total_earnings
    return result

print(solution())