def solution():
    """Calculate the total amount of money the cab rides cost would be at the end of the event."""
    miles_per_day = 400 # 200 miles to the event and 200 miles back home
    cost_per_mile = 2.5
    total_cost = miles_per_day * cost_per_mile * 7 # event is one week long
    result = total_cost
    return result

print(solution())