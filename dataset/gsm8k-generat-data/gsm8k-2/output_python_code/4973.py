def solution():
    """John takes 3 days off of streaming per week. On the days he does stream, he streams for 4 hours at a time and makes $10 an hour. How much does he make a week?"""
    days_streaming = 7 - 3
    hours_per_day_streaming = 4
    hourly_rate = 10
    total_earned = days_streaming * hours_per_day_streaming * hourly_rate
    result = total_earned
    return result

print(solution())