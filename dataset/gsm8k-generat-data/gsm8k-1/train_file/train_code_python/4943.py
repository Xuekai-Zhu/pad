def solution():
    """Patrick buys a season pass for each of his sons to visit the local amusement park as often as they want. The passes were $100.00 each. The oldest son went to the park 35 times over the summer and the youngest went 15 times. What was the cost per trip to the park?"""
    passes_cost = 100
    oldest_son_visits = 35
    youngest_son_visits = 15
    total_passes_cost = passes_cost * 2
    total_visits = oldest_son_visits + youngest_son_visits
    cost_per_trip = total_passes_cost / total_visits
    result = cost_per_trip
    return result

print(solution())