def solution():
    # Calculate the cost of doing two loads of laundry
    cost_wash = 4 * 2  # each load costs $4
    cost_dry = (3 * 0.25 * 4)  # each dryer costs $0.25 for every 10 minutes
    # or cost_dry = (3 * 0.25 * 4/10 * 4) which is equivalent to 3 quarters per dryer per hour
    total_cost = cost_wash + cost_dry  # total cost of doing laundry
    result = total_cost
    return result

print(solution())