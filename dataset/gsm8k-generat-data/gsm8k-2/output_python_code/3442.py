def solution():
    """Hannah is trying to figure out how much she'll get paid this week. She makes $30/hour and works 18 hours per week. Her pay is docked $5 each time she's late. If she was late 3 times this week, how much does she get paid?"""
    hourly_pay = 30
    weekly_hours = 18
    late_penalties = 5 * 3
    total_pay = (hourly_pay * weekly_hours) - late_penalties
    result = total_pay
    return result

print(solution())