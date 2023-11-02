def solution():
    """Jeff bought 6 pairs of shoes and 4 jerseys for $560. Jerseys cost 1/4 price of one pair of shoes. Find the shoe's price total price."""
    total_items = 6 + 4
    total_cost = 560
    jersey_cost_ratio = 1/4
    shoe_cost = (total_cost / total_items) / (1 + jersey_cost_ratio)
    shoe_total_price = shoe_cost * 6
    result = shoe_total_price
    return result

print(solution())