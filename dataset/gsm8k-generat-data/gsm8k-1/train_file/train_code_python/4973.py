def solution():
    """John takes 3 days off of streaming per week. On the days he does stream, he streams for 4 hours at a time and makes $10 an hour. How much does he make a week?"""
    days_streaming = 4
    hours_per_day = 4
    wage_per_hour = 10
    days_not_streaming = 3
    total_hours_streaming = days_streaming * hours_per_day
    total_wage = total_hours_streaming * wage_per_hour
    weekly_wage = total_wage * (7 - days_not_streaming)

    return weekly_wage

print(solution())