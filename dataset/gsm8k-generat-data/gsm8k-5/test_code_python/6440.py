def solution():
    # Calculate the cost of one uniform without discount
    cost_per_uniform_without_discount = 7.5 + 15 + 4.5  # $7.50 for a shirt, $15 for pants, $4.50 for socks

    # Calculate the cost of one uniform with discount
    cost_per_uniform_with_discount = 6.75 + 13.5 + 3.75  # $6.75 for a shirt, $13.50 for pants, $3.75 for socks

    # Calculate the total cost for the team without discount
    total_cost_without_discount = 12 * cost_per_uniform_without_discount

    # Calculate the total cost for the team with discount
    total_cost_with_discount = 12 * cost_per_uniform_with_discount

    # Calculate the savings with group discount
    savings = total_cost_without_discount - total_cost_with_discount
    result = savings
    return result

print(solution())