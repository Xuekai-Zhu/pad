def solution():
    """A year ago, the total cost of buying a lawnmower was 2/5 times less than the cost it goes for now. If the cost was $1800 a year ago, calculate how much it would cost Mr. Lucian to buy 4 such lawnmowers."""
    cost_a_year_ago = 1800
    cost_now = cost_a_year_ago / (1 - 2/5)
    num_lawnmowers = 4
    total_cost = cost_now * num_lawnmowers
    result = total_cost
    return result

print(solution())