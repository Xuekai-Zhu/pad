def solution():
    """Your video streaming subscription costs $14 a month. If you're evenly splitting the cost with your friend, how much do you pay in total after the first year for this service?"""
    cost_per_month = 14
    months_per_year = 12
    total_cost = cost_per_month * months_per_year * 0.5
    result = total_cost
    return result

print(solution())