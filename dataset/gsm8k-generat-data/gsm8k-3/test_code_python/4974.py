def solution():
    """John takes 3 days off of streaming per week.  On the days he does stream, he streams for 4 hours at a time and makes $10 an hour.  How much does he make a week?"""
    # Define John's hourly rate and hours streamed per day
    HOURLY_RATE = 10
    HOURS_STREAMED = 4

    # Calculate the total hours streamed in a week
    total_hours = (7 - 3) * HOURS_STREAMED

    # Calculate John's weekly earnings
    weekly_earnings = total_hours * HOURLY_RATE

    # Display John's weekly earnings
    result = weekly_earnings
    return result

print(solution())