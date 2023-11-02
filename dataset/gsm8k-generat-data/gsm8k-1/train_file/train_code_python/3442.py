def solution():
    """Hannah is trying to figure out how much she'll get paid this week. She makes $30/hour and works 18 hours per week. Her pay is docked $5 each time she's late. If she was late 3 times this week, how much does she get paid?"""
    hourly_rate = 30
    hours_worked = 18
    late_penalty = 5
    num_late = 3
    total_penalties = num_late * late_penalty
    total_pay = hourly_rate * hours_worked - total_penalties
    result = total_pay
    return result

print(solution())