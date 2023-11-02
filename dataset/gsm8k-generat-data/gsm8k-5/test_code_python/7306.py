def solution():
    cost_of_lemonade = 2 * 2  # Roxanne bought 2 cups of lemonade for $2 each
    cost_of_sandwiches = 2 * 2.5  # Roxanne bought 2 sandwiches for $2.50 each
    total_cost = cost_of_lemonade + cost_of_sandwiches  # Total cost of the purchase
    change = 20 - total_cost  # Change from a $20 bill

    result = change
    return result

print(solution())