def solution():
    pieces_per_pie = 3  # Each pie has 3 pieces
    cost_per_pie = 0.5 + (4 * pieces_per_pie)  # Cost of making one pie plus cost of the pie pieces
    pies_per_hour = 12  # The bakery can make 12 pies in one hour

    # Calculate the total cost of making 12 pies
    cost_per_hour = cost_per_pie * pies_per_hour

    # Calculate the revenue of selling all pie pieces
    revenue_per_hour = 4 * pieces_per_pie * pies_per_hour

    # Calculate the profit
    profit_per_hour = revenue_per_hour - cost_per_hour
    result = profit_per_hour
    return result

print(solution())