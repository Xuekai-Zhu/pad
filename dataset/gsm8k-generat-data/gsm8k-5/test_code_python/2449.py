def solution():
    # Calculate the total cost of the ten shirts
    cost_of_shirts = 10 * 5  # Ten shirts at $5 each

    # Calculate the total cost of the three pairs of sandals
    cost_of_sandals = 3 * 3  # Three pairs of sandals at $3 each

    # Calculate the total cost of the purchase
    total_cost = cost_of_shirts + cost_of_sandals

    # Calculate the change Yanna will receive if she paid with a $100 bill
    change = 100 - total_cost
    result = change
    return result

print(solution())