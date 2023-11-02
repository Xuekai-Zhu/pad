def solution():
    """John takes 3 days off of streaming per week. On the days he does stream, he streams for 4 hours at a time and makes $10 an hour. How much does he make a week?"""
    # Define constants
    STREAMING_DAYS_PER_WEEK = 7 - 3
    STREAMING_HOURS_PER_DAY = 4
    HOURLY_EARNINGS = 10

    # Calculate the total hours John streams each week
    total_streaming_hours = STREAMING_DAYS_PER_WEEK * STREAMING_HOURS_PER_DAY

    # Calculate John's total weekly earnings
    weekly_earnings = total_streaming_hours * HOURLY_EARNINGS

    # Return the result
    result = weekly_earnings
    return result

print(solution())