def solution():
    cost_per_pie = 4.0
    num_pieces_per_pie = 3
    pies_per_hour = 12
    cost_per_pie_creation = 0.5

    # Calculate the total revenue from selling all pie pieces
    revenue = cost_per_pie * num_pieces_per_pie * pies_per_hour

    # Calculate the total cost of creating all pies
    cost = cost_per_pie_creation * pies_per_hour

    # Calculate the profit made by the bakery
    profit = revenue - cost
    result = profit
    return result

print(solution())