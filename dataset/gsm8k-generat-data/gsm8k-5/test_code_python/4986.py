def solution():
    # Calculate the total cost of the ingredients
    total_cost = (2 * 4) + (2 * 2) + 0.5 + 2.5  # 2 cups of flour at $4 each, 2 cups of sugar at $2 each, 2 eggs at $0.5 each, and a cup of butter at $2.5

    # Calculate the cost per slice of the cake
    cost_per_slice = total_cost / 6

    # Calculate the cost of the cake that the mother ate
    cost_mother_ate = cost_per_slice * 2

    # Calculate the amount Kevin ate
    amount_kevin_ate = cost_per_slice * 4

    result = amount_kevin_ate
    return result

print(solution())