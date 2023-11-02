def solution():
    """John works 12 hours every other day. He gets a 30% raise from his former $20 an hour job. How much does he make in a 30 day month?"""
    # Define John's work schedule
    work_schedule = 12 * 15  # John works for 15 days in a 30-day month

    # Calculate John's hourly rate with the 30% raise
    hourly_rate = 20 * 1.3

    # Calculate John's total earnings for the month
    total_earnings = work_schedule * hourly_rate

    result = total_earnings
    return result

print(solution())