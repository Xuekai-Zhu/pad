def solution():
    cost_per_pan = 10.0
    sell_price_per_pan = 25.0
    num_pans = 20

    # Calculate the total cost of making all pans of lasagna
    total_cost = cost_per_pan * num_pans

    # Calculate the total revenue from selling all pans of lasagna
    total_revenue = sell_price_per_pan * num_pans

    # Calculate Jenny's profit after factoring in expenses
    profit = total_revenue - total_cost
    result = profit
    return result

print(solution())