def solution():
    """A year ago, the total cost of buying a lawnmower was 2/5 times less than the cost it goes for now. If the cost was $1800 a year ago, calculate how much it would cost Mr. Lucian to buy 4 such lawnmowers."""
    initial_cost = 1800
    cost_increase = 2/5
    current_cost = initial_cost / (1 - cost_increase)
    total_cost = current_cost * 4
    result = total_cost
    return result

print(solution())