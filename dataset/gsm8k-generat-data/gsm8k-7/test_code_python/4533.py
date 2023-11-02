def solution():
    num_acres = 200
    cost_per_acre = 70
    sale_price_per_acre = 200

    # Calculate the total cost of buying the land
    total_cost = num_acres * cost_per_acre

    # Calculate the revenue from selling half the land
    revenue = (num_acres/2) * sale_price_per_acre

    # Calculate the profit by subtracting the cost from the revenue
    profit = revenue - total_cost
    result = profit
    return result

print(solution())